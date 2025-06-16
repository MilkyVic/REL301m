#!/usr/bin/env python3
#######################################################################
# Copyright (C)                                                       #
# 2016-2018 Shangtong Zhang(zhangshangtong.cpp@gmail.com)             #
# 2016 Kenta Shimada(hyperkentakun@gmail.com)                         #
# Permission given to modify the code as long as you keep this        #
# declaration at the top                                              #
#######################################################################

import numpy as np # Import thư viện NumPy để làm việc với các mảng và phép toán số học.
import matplotlib # Import thư viện Matplotlib để tạo biểu đồ.
matplotlib.use('Agg') # Cấu hình Matplotlib để sử dụng backend 'Agg', cho phép lưu biểu đồ vào file mà không cần hiển thị.
import matplotlib.pyplot as plt # Import module pyplot từ Matplotlib để vẽ biểu đồ.
from tqdm import tqdm # Import tqdm để hiển thị thanh tiến độ cho các vòng lặp dài.
import heapq # Import thư viện heapq để triển khai hàng đợi ưu tiên (min-heap).
from copy import deepcopy # Import deepcopy để tạo bản sao sâu của các đối tượng phức tạp.

# Lớp PriorityQueue: Triển khai một hàng đợi ưu tiên (min-heap).
# Được sử dụng trong thuật toán Prioritized Sweeping để quản lý các cặp (trạng thái, hành động) cần cập nhật.
class PriorityQueue:
    def __init__(self): # Hàm khởi tạo.
        self.pq = [] # Danh sách lưu trữ các phần tử trong heap (priority, counter, item).
        self.entry_finder = {} # Ánh xạ các phần tử tới các mục nhập trong heap để tìm kiếm nhanh.
        self.REMOVED = '<removed-task>' # Đánh dấu các mục đã bị xóa logic khỏi heap.
        self.counter = 0 # Bộ đếm để đảm bảo thứ tự chèn (cho các mục có cùng ưu tiên).

    def add_item(self, item, priority=0): # Thêm một phần tử vào hàng đợi ưu tiên.
        if item in self.entry_finder: # Nếu phần tử đã tồn tại, xóa nó trước.
            self.remove_item(item)
        entry = [priority, self.counter, item] # Tạo một mục nhập mới: [ưu tiên, bộ đếm, phần tử].
        self.counter += 1 # Tăng bộ đếm.
        self.entry_finder[item] = entry # Lưu trữ ánh xạ phần tử tới mục nhập.
        heapq.heappush(self.pq, entry) # Đẩy mục nhập vào heap.

    def remove_item(self, item): # Xóa một phần tử khỏi hàng đợi ưu tiên (logic).
        entry = self.entry_finder.pop(item) # Lấy và xóa mục nhập khỏi entry_finder.
        entry[-1] = self.REMOVED # Đánh dấu mục nhập là đã bị xóa.

    def pop_item(self): # Lấy và xóa phần tử có ưu tiên cao nhất (nhỏ nhất) khỏi hàng đợi.
        while self.pq: # Lặp cho đến khi hàng đợi rỗng.
            priority, count, item = heapq.heappop(self.pq) # Lấy phần tử có ưu tiên cao nhất từ heap.
            if item is not self.REMOVED: # Nếu phần tử chưa bị đánh dấu là đã xóa.
                del self.entry_finder[item] # Xóa nó khỏi entry_finder.
                return item, priority # Trả về phần tử và ưu tiên của nó.
        raise KeyError('pop from an empty priority queue') # Báo lỗi nếu hàng đợi rỗng.

    def empty(self): # Kiểm tra xem hàng đợi ưu tiên có rỗng hay không.
        return not self.entry_finder # Rỗng nếu entry_finder không chứa mục nào.

# Lớp Maze: Một lớp bao bọc cho mê cung, chứa tất cả thông tin về môi trường.
# Mặc định được khởi tạo là DynaMaze, nhưng có thể dễ dàng điều chỉnh.
class Maze:
    def __init__(self): # Hàm khởi tạo.
        # Chiều rộng của mê cung.
        self.WORLD_WIDTH = 9

        # Chiều cao của mê cung.
        self.WORLD_HEIGHT = 6

        # Tất cả các hành động có thể có.
        self.ACTION_UP = 0
        self.ACTION_DOWN = 1
        self.ACTION_LEFT = 2
        self.ACTION_RIGHT = 3
        self.actions = [self.ACTION_UP, self.ACTION_DOWN, self.ACTION_LEFT, self.ACTION_RIGHT]

        # Trạng thái bắt đầu.
        self.START_STATE = [2, 0]

        # Các trạng thái mục tiêu (có thể có nhiều mục tiêu).
        self.GOAL_STATES = [[0, 8]]

        # Tất cả các chướng ngại vật.
        self.obstacles = [[1, 2], [2, 2], [3, 2], [0, 7], [1, 7], [2, 7], [4, 5]]
        self.old_obstacles = None # Chướng ngại vật cũ (dùng cho môi trường thay đổi).
        self.new_obstacles = None # Chướng ngại vật mới (dùng cho môi trường thay đổi).

        # Thời điểm thay đổi chướng ngại vật.
        self.obstacle_switch_time = None

        # Kích thước của mảng Q-value (chiều cao, chiều rộng, số hành động).
        self.q_size = (self.WORLD_HEIGHT, self.WORLD_WIDTH, len(self.actions))

        # Giới hạn số bước tối đa trong một tập (episode).
        self.max_steps = float('inf') # Mặc định là vô hạn.

        # Độ phân giải của mê cung (dùng khi mở rộng mê cung).
        self.resolution = 1

    # Mở rộng một trạng thái sang mê cung có độ phân giải cao hơn.
    # @state: trạng thái trong mê cung độ phân giải thấp hơn.
    # @factor: yếu tố mở rộng, một trạng thái sẽ trở thành factor^2 trạng thái sau khi mở rộng.
    def extend_state(self, state, factor):
        new_state = [state[0] * factor, state[1] * factor]
        new_states = []
        for i in range(0, factor):
            for j in range(0, factor):
                new_states.append([new_state[0] + i, new_state[1] + j])
        return new_states

    # Mở rộng mê cung thành độ phân giải cao hơn.
    # Một trạng thái trong mê cung gốc sẽ trở thành @factor^2 trạng thái trong @return mê cung mới.
    def extend_maze(self, factor):
        new_maze = Maze() # Tạo một mê cung mới.
        new_maze.WORLD_WIDTH = self.WORLD_WIDTH * factor # Cập nhật chiều rộng.
        new_maze.WORLD_HEIGHT = self.WORLD_HEIGHT * factor # Cập nhật chiều cao.
        new_maze.START_STATE = [self.START_STATE[0] * factor, self.START_STATE[1] * factor] # Cập nhật trạng thái bắt đầu.
        new_maze.GOAL_STATES = self.extend_state(self.GOAL_STATES[0], factor) # Mở rộng trạng thái mục tiêu.
        new_maze.obstacles = [] # Khởi tạo danh sách chướng ngại vật mới.
        for state in self.obstacles: # Duyệt qua các chướng ngại vật cũ.
            new_maze.obstacles.extend(self.extend_state(state, factor)) # Mở rộng và thêm vào danh sách mới.
        new_maze.q_size = (new_maze.WORLD_HEIGHT, new_maze.WORLD_WIDTH, len(new_maze.actions)) # Cập nhật kích thước Q-value.
        new_maze.resolution = factor # Cập nhật độ phân giải.
        return new_maze # Trả về mê cung mới đã mở rộng.

    # Thực hiện @action trong @state.
    # @return: [trạng thái mới, phần thưởng].
    def step(self, state, action):
        x, y = state # Lấy tọa độ hiện tại.
        if action == self.ACTION_UP: # Di chuyển lên.
            x = max(x - 1, 0)
        elif action == self.ACTION_DOWN: # Di chuyển xuống.
            x = min(x + 1, self.WORLD_HEIGHT - 1)
        elif action == self.ACTION_LEFT: # Di chuyển sang trái.
            y = max(y - 1, 0)
        elif action == self.ACTION_RIGHT: # Di chuyển sang phải.
            y = min(y + 1, self.WORLD_WIDTH - 1)
        if [x, y] in self.obstacles: # Nếu trạng thái mới là chướng ngại vật.
            x, y = state # Agent vẫn ở trạng thái cũ (không di chuyển được).
        if [x, y] in self.GOAL_STATES: # Nếu trạng thái mới là mục tiêu.
            reward = 1.0 # Nhận phần thưởng 1.0.
        else: # Nếu không phải mục tiêu.
            reward = 0.0 # Phần thưởng là 0.0.
        return [x, y], reward # Trả về trạng thái mới và phần thưởng.

# Lớp DynaParams: Một lớp bao bọc cho các tham số của thuật toán Dyna.
class DynaParams:
    def __init__(self): # Hàm khởi tạo.
        # Hệ số chiết khấu (discount factor).
        self.gamma = 0.95

        # Xác suất khám phá (exploration probability) cho epsilon-greedy.
        self.epsilon = 0.1

        # Tốc độ học (step size) của thuật toán Q-learning.
        self.alpha = 0.1

        # Trọng số cho thời gian trôi qua (sử dụng trong Dyna-Q+).
        self.time_weight = 0 # Mặc định là 0 cho Dyna-Q thường.

        # Số bước lập kế hoạch (planning steps).
        self.planning_steps = 5

        # Số lần chạy độc lập để lấy trung bình kết quả.
        self.runs = 10

        # Tên các thuật toán (dùng cho việc vẽ biểu đồ).
        self.methods = ['Dyna-Q', 'Dyna-Q+']

        # Ngưỡng cho hàng đợi ưu tiên (sử dụng trong Prioritized Sweeping).
        self.theta = 0


# Hàm chọn hành động dựa trên thuật toán epsilon-greedy.
def choose_action(state, q_value, maze, dyna_params):
    if np.random.binomial(1, dyna_params.epsilon) == 1: # Với xác suất epsilon, chọn hành động ngẫu nhiên (khám phá).
        return np.random.choice(maze.actions)
    else: # Với xác suất 1 - epsilon, chọn hành động tốt nhất (khai thác).
        values = q_value[state[0], state[1], :] # Lấy các giá trị Q cho trạng thái hiện tại.
        # Chọn ngẫu nhiên một hành động trong số các hành động có giá trị Q tối đa (để phá vỡ sự ràng buộc).
        return np.random.choice([action for action, value in enumerate(values) if value == np.max(values)])

# Lớp TrivialModel: Mô hình đơn giản cho việc lập kế hoạch trong Dyna-Q.
class TrivialModel:
    # @rand: một đối tượng np.random.RandomState để lấy mẫu ngẫu nhiên.
    def __init__(self, rand=np.random): # Hàm khởi tạo.
        self.model = dict() # Từ điển để lưu trữ mô hình: (trạng thái) -> (hành động) -> [trạng thái_tiếp_theo, phần_thưởng].
        self.rand = rand # Đối tượng random state.

    # Đưa kinh nghiệm vào mô hình.
    def feed(self, state, action, next_state, reward): # Ghi lại kinh nghiệm (s, a, s', r).
        state = deepcopy(state) # Tạo bản sao sâu của trạng thái để tránh thay đổi ngầm định.
        next_state = deepcopy(next_state) # Tạo bản sao sâu của trạng thái tiếp theo.
        if tuple(state) not in self.model.keys(): # Nếu trạng thái chưa có trong mô hình.
            self.model[tuple(state)] = dict() # Khởi tạo một từ điển mới cho trạng thái đó.
        self.model[tuple(state)][action] = [list(next_state), reward] # Lưu trạng thái tiếp theo và phần thưởng cho cặp (trạng thái, hành động).

    # Lấy mẫu ngẫu nhiên từ kinh nghiệm đã có trong mô hình.
    def sample(self): # Lấy mẫu ngẫu nhiên một kinh nghiệm từ mô hình.
        state_index = self.rand.choice(range(len(self.model.keys()))) # Chọn ngẫu nhiên chỉ số của một trạng thái đã thấy.
        state = list(self.model)[state_index] # Lấy trạng thái từ chỉ số.
        action_index = self.rand.choice(range(len(self.model[state].keys()))) # Chọn ngẫu nhiên chỉ số của một hành động từ trạng thái đó.
        action = list(self.model[state])[action_index] # Lấy hành động từ chỉ số.
        next_state, reward = self.model[state][action] # Lấy trạng thái tiếp theo và phần thưởng.
        state = deepcopy(state) # Tạo bản sao sâu.
        next_state = deepcopy(next_state) # Tạo bản sao sâu.
        return list(state), action, list(next_state), reward # Trả về kinh nghiệm.

# Lớp TimeModel: Mô hình dựa trên thời gian cho việc lập kế hoạch trong Dyna-Q+.
class TimeModel:
    # @maze: đối tượng mê cung. Mặc dù không hoàn toàn hợp lý khi cấp quyền truy cập mê cung cho mô hình.
    # @timeWeight: còn gọi là kappa, trọng số cho thời gian trôi qua trong phần thưởng lấy mẫu, cần phải nhỏ.
    # @rand: một đối tượng np.random.RandomState để lấy mẫu ngẫu nhiên.
    def __init__(self, maze, time_weight=1e-4, rand=np.random): # Hàm khởi tạo.
        self.rand = rand # Đối tượng random state.
        self.model = dict() # Từ điển để lưu trữ mô hình.

        # Theo dõi tổng thời gian (tổng số bước đã thực hiện).
        self.time = 0

        self.time_weight = time_weight # Trọng số cho thời gian.
        self.maze = maze # Đối tượng mê cung.

    # Đưa kinh nghiệm vào mô hình.
    def feed(self, state, action, next_state, reward): # Ghi lại kinh nghiệm (s, a, s', r).
        state = deepcopy(state) # Bản sao sâu của trạng thái.
        next_state = deepcopy(next_state) # Bản sao sâu của trạng thái tiếp theo.
        self.time += 1 # Tăng tổng thời gian.
        if tuple(state) not in self.model.keys(): # Nếu trạng thái chưa có trong mô hình.
            self.model[tuple(state)] = dict() # Khởi tạo từ điển cho trạng thái.

            # Các hành động chưa từng được thử trước đó từ một trạng thái được phép xem xét trong bước lập kế hoạch.
            for action_ in self.maze.actions: # Duyệt qua tất cả các hành động có thể.
                if action_ != action: # Nếu hành động chưa được thử từ trạng thái này.
                    # Những hành động như vậy sẽ dẫn trở lại cùng một trạng thái với phần thưởng bằng không.
                    # Lưu ý rằng dấu thời gian tối thiểu là 1 thay vì 0.
                    self.model[tuple(state)][action_] = [list(state), 0, 1] # Thêm kinh nghiệm ảo: về lại s, reward 0, time 1.

        self.model[tuple(state)][action] = [list(next_state), reward, self.time] # Lưu kinh nghiệm thực tế với dấu thời gian.

    # Lấy mẫu ngẫu nhiên từ kinh nghiệm đã có trong mô hình.
    def sample(self): # Lấy mẫu ngẫu nhiên một kinh nghiệm từ mô hình.
        state_index = self.rand.choice(range(len(self.model.keys()))) # Chọn ngẫu nhiên chỉ số trạng thái.
        state = list(self.model)[state_index] # Lấy trạng thái.
        action_index = self.rand.choice(range(len(self.model[state].keys()))) # Chọn ngẫu nhiên chỉ số hành động.
        action = list(self.model[state])[action_index] # Lấy hành động.
        next_state, reward, time = self.model[state][action] # Lấy thông tin kinh nghiệm và dấu thời gian.

        # Điều chỉnh phần thưởng với thời gian đã trôi qua kể từ lần truy cập cuối cùng.
        reward += self.time_weight * np.sqrt(self.time - time) # Cộng thêm phần thưởng khám phá dựa trên thời gian.

        state = deepcopy(state) # Bản sao sâu.
        next_state = deepcopy(next_state) # Bản sao sâu.

        return list(state), action, list(next_state), reward # Trả về kinh nghiệm đã điều chỉnh phần thưởng.

# Lớp Model chứa hàng đợi ưu tiên cho Prioritized Sweeping.
class PriorityModel(TrivialModel):
    def __init__(self, rand=np.random): # Hàm khởi tạo.
        TrivialModel.__init__(self, rand) # Gọi hàm khởi tạo của lớp cha TrivialModel.
        # Duy trì một hàng đợi ưu tiên.
        self.priority_queue = PriorityQueue() # Khởi tạo PriorityQueue.
        # Theo dõi các tiền nhiệm (predecessors) cho mỗi trạng thái.
        self.predecessors = dict() # Từ điển lưu trữ: (trạng thái) -> set of (trạng thái_tiền_nhiệm, hành động_tiền_nhiệm).

    # Thêm một cặp (trạng thái, hành động) vào hàng đợi ưu tiên với độ ưu tiên @priority.
    def insert(self, priority, state, action): # Chèn một mục vào hàng đợi ưu tiên.
        # Lưu ý hàng đợi ưu tiên là một min-heap, vì vậy chúng ta sử dụng -priority.
        self.priority_queue.add_item((tuple(state), action), -priority) # Lưu cặp (s,a) với ưu tiên âm.

    # @return: kiểm tra xem hàng đợi ưu tiên có rỗng hay không.
    def empty(self): # Kiểm tra hàng đợi có rỗng không.
        return self.priority_queue.empty()

    # Lấy phần tử đầu tiên trong hàng đợi ưu tiên (phần tử có ưu tiên cao nhất).
    def sample(self): # Lấy mẫu từ hàng đợi ưu tiên (phần tử có ưu tiên cao nhất).
        (state, action), priority = self.priority_queue.pop_item() # Lấy cặp (s,a) và ưu tiên.
        next_state, reward = self.model[state][action] # Lấy thông tin từ mô hình.
        state = deepcopy(state) # Bản sao sâu.
        next_state = deepcopy(next_state) # Bản sao sâu.
        return -priority, list(state), action, list(next_state), reward # Trả về ưu tiên dương và kinh nghiệm.

    # Đưa kinh nghiệm vào mô hình.
    def feed(self, state, action, next_state, reward): # Ghi lại kinh nghiệm và cập nhật tiền nhiệm.
        state = deepcopy(state) # Bản sao sâu.
        next_state = deepcopy(next_state) # Bản sao sâu.
        TrivialModel.feed(self, state, action, next_state, reward) # Gọi phương thức feed của lớp cha.
        if tuple(next_state) not in self.predecessors.keys(): # Nếu trạng thái tiếp theo chưa có tiền nhiệm.
            self.predecessors[tuple(next_state)] = set() # Khởi tạo tập hợp tiền nhiệm.
        self.predecessors[tuple(next_state)].add((tuple(state), action)) # Thêm (s, a) vào danh sách tiền nhiệm của s'.

    # Lấy tất cả các tiền nhiệm đã thấy của một trạng thái @state.
    def predecessor(self, state): # Lấy các tiền nhiệm của một trạng thái.
        if tuple(state) not in self.predecessors.keys(): # Nếu trạng thái không có tiền nhiệm nào được ghi nhận.
            return [] # Trả về danh sách rỗng.
        predecessors = [] # Danh sách để lưu trữ các tiền nhiệm.
        for state_pre, action_pre, reward_pre in list(self.predecessors[tuple(state)]): # Duyệt qua các tiền nhiệm.
            predecessors.append([list(state_pre), action_pre, self.model[state_pre][action_pre][1]]) # Thêm tiền nhiệm và phần thưởng tương ứng.
        return predecessors # Trả về danh sách các tiền nhiệm.


# Hàm chạy một tập (episode) cho thuật toán Dyna-Q.
# @q_value: Các giá trị cặp trạng thái-hành động, sẽ được cập nhật.
# @model: Đối tượng mô hình để lập kế hoạch.
# @maze: Đối tượng mê cung chứa tất cả thông tin về môi trường.
# @dyna_params: Một số tham số cho thuật toán.
def dyna_q(q_value, model, maze, dyna_params):
    state = maze.START_STATE # Khởi tạo trạng thái bắt đầu.
    steps = 0 # Đếm số bước trong tập.
    while state not in maze.GOAL_STATES: # Lặp cho đến khi đạt được mục tiêu.
        steps += 1 # Tăng số bước.

        action = choose_action(state, q_value, maze, dyna_params) # Chọn hành động.

        next_state, reward = maze.step(state, action) # Thực hiện hành động và nhận s', r.

        # Cập nhật Q-value (Q-Learning update).
        q_value[state[0], state[1], action] += \
            dyna_params.alpha * (reward + dyna_params.gamma * np.max(q_value[next_state[0], next_state[1], :]) - \
                                 q_value[state[0], state[1], action])

        model.feed(state, action, next_state, reward) # Đưa kinh nghiệm thực tế vào mô hình.

        # Lấy mẫu kinh nghiệm từ mô hình (planning steps).
        for t in range(0, dyna_params.planning_steps): # Lặp lại N lần planning steps.
            state_, action_, next_state_, reward_ = model.sample() # Lấy mẫu một kinh nghiệm từ mô hình.
            # Cập nhật Q-value dựa trên kinh nghiệm giả lập từ mô hình.
            q_value[state_[0], state_[1], action_] += \
                dyna_params.alpha * (reward_ + dyna_params.gamma * np.max(q_value[next_state_[0], next_state_[1], :]) - \
                                     q_value[state_[0], state_[1], action_])

        state = next_state # Cập nhật trạng thái hiện tại.

        if steps > maze.max_steps: # Kiểm tra xem đã vượt quá giới hạn bước chưa.
            break # Thoát nếu đã vượt quá.

    return steps # Trả về số bước đã thực hiện trong tập.

# Hàm chạy một tập cho thuật toán Prioritized Sweeping.
# @q_value: Các giá trị cặp trạng thái-hành động, sẽ được cập nhật.
# @model: Đối tượng mô hình để lập kế hoạch.
# @maze: Đối tượng mê cung chứa tất cả thông tin về môi trường.
# @dyna_params: Một số tham số cho thuật toán.
# @return: Số lượng cập nhật (backups) trong tập này.
def prioritized_sweeping(q_value, model, maze, dyna_params):
    state = maze.START_STATE # Khởi tạo trạng thái bắt đầu.

    steps = 0 # Đếm số bước trong tập.

    backups = 0 # Đếm số lượng cập nhật trong giai đoạn lập kế hoạch.

    while state not in maze.GOAL_STATES: # Lặp cho đến khi đạt được mục tiêu.
        steps += 1 # Tăng số bước.

        action = choose_action(state, q_value, maze, dyna_params) # Chọn hành động.

        next_state, reward = maze.step(state, action) # Thực hiện hành động và nhận s', r.

        model.feed(state, action, next_state, reward) # Đưa kinh nghiệm thực tế vào mô hình và cập nhật tiền nhiệm.

        # Tính toán độ ưu tiên cho cặp (trạng thái, hành động) hiện tại.
        priority = np.abs(reward + dyna_params.gamma * np.max(q_value[next_state[0], next_state[1], :]) - \
                          q_value[state[0], state[1], action])

        if priority > dyna_params.theta: # Nếu độ ưu tiên vượt ngưỡng.
            model.insert(priority, state, action) # Chèn cặp (s, a) vào hàng đợi ưu tiên.

        # Bắt đầu lập kế hoạch.
        planning_step = 0 # Đếm số bước lập kế hoạch.

        # Lập kế hoạch cho một số bước, hoặc cho đến khi hàng đợi ưu tiên rỗng.
        # Lưu ý: tiếp tục lập kế hoạch cho đến khi hàng đợi rỗng sẽ hội tụ nhanh hơn nhiều.
        while planning_step < dyna_params.planning_steps and not model.empty():
            # Lấy mẫu với độ ưu tiên cao nhất từ mô hình (từ hàng đợi ưu tiên).
            priority, state_, action_, next_state_, reward_ = model.sample()

            # Cập nhật giá trị cặp trạng thái-hành động cho mẫu đã lấy.
            delta = reward_ + dyna_params.gamma * np.max(q_value[next_state_[0], next_state_[1], :]) - \
                    q_value[state_[0], state_[1], action_]
            q_value[state_[0], state_[1], action_] += dyna_params.alpha * delta

            # Xử lý tất cả các tiền nhiệm của trạng thái mẫu.
            for state_pre, action_pre, reward_pre in model.predecessor(state_): # Duyệt qua các tiền nhiệm của s'.
                # Tính toán độ ưu tiên cho cặp tiền nhiệm.
                priority = np.abs(reward_pre + dyna_params.gamma * np.max(q_value[state_[0], state_[1], :]) - \
                                  q_value[state_pre[0], state_pre[1], action_pre])
                if priority > dyna_params.theta: # Nếu độ ưu tiên vượt ngưỡng.
                    model.insert(priority, state_pre, action_pre) # Chèn tiền nhiệm vào hàng đợi ưu tiên.
            planning_step += 1 # Tăng số bước lập kế hoạch.

        state = next_state # Cập nhật trạng thái hiện tại.

        backups += planning_step + 1 # Cập nhật tổng số lượng cập nhật (1 bước thực tế + planning_step).

    return backups # Trả về tổng số lượng cập nhật.

# Hàm tạo Hình 8.2: DynaMaze, sử dụng 10 lần chạy thay vì 30 lần chạy.
def figure_8_2():
    dyna_maze = Maze() # Tạo một đối tượng mê cung DynaMaze.
    dyna_params = DynaParams() # Tạo một đối tượng tham số Dyna.

    runs = 10 # Số lần chạy độc lập.
    episodes = 50 # Số tập cho mỗi lần chạy.
    planning_steps = [0, 5, 50] # Các số bước lập kế hoạch khác nhau để so sánh.
    steps = np.zeros((len(planning_steps), episodes)) # Mảng để lưu trữ số bước trên mỗi tập.

    for run in tqdm(range(runs)): # Lặp qua số lần chạy (hiển thị thanh tiến độ).
        for i, planning_step in enumerate(planning_steps): # Lặp qua các số bước lập kế hoạch.
            dyna_params.planning_steps = planning_step # Cập nhật tham số số bước lập kế hoạch.
            q_value = np.zeros(dyna_maze.q_size) # Khởi tạo bảng Q-value.

            model = TrivialModel() # Tạo một đối tượng mô hình Dyna-Q.
            for ep in range(episodes): # Lặp qua số tập.
                # print('run:', run, 'planning step:', planning_step, 'episode:', ep)
                steps[i, ep] += dyna_q(q_value, model, dyna_maze, dyna_params) # Chạy Dyna-Q và cộng dồn số bước.

    steps /= runs # Lấy trung bình số bước trên mỗi tập qua các lần chạy.

    for i in range(len(planning_steps)): # Vẽ biểu đồ cho từng cấu hình planning steps.
        plt.plot(steps[i, :], label='%d planning steps' % (planning_steps[i]))
    plt.xlabel('episodes') # Nhãn trục x.
    plt.ylabel('steps per episode') # Nhãn trục y.
    plt.legend() # Hiển thị chú giải.

    plt.savefig('../images/figure_8_2.png') # Lưu biểu đồ.
    plt.close() # Đóng biểu đồ.

# Hàm bao bọc cho mê cung thay đổi (dùng cho BlockingMaze và ShortcutMaze).
# @maze: đối tượng mê cung.
# @dynaParams: một số tham số cho thuật toán dyna.
def changing_maze(maze, dyna_params):

    max_steps = maze.max_steps # Giới hạn số bước tối đa.

    rewards = np.zeros((dyna_params.runs, 2, max_steps)) # Mảng để lưu trữ phần thưởng tích lũy.

    for run in tqdm(range(dyna_params.runs)): # Lặp qua số lần chạy.
        models = [TrivialModel(), TimeModel(maze, time_weight=dyna_params.time_weight)] # Khởi tạo các mô hình (Dyna-Q và Dyna-Q+).

        q_values = [np.zeros(maze.q_size), np.zeros(maze.q_size)] # Khởi tạo các bảng Q-value.

        for i in range(len(dyna_params.methods)): # Lặp qua các phương pháp (Dyna-Q, Dyna-Q+).
            # print('run:', run, dyna_params.methods[i])

            maze.obstacles = maze.old_obstacles # Đặt lại chướng ngại vật cũ cho mê cung.

            steps = 0 # Đếm số bước đã thực hiện trong lần chạy hiện tại.
            last_steps = steps # Lưu lại số bước trước khi cập nhật phần thưởng tích lũy.
            while steps < max_steps: # Lặp cho đến khi đạt giới hạn số bước tối đa.
                steps += dyna_q(q_values[i], models[i], maze, dyna_params) # Chạy Dyna-Q hoặc Dyna-Q+ và cộng dồn số bước.

                # Cập nhật phần thưởng tích lũy.
                rewards[run, i, last_steps: steps] = rewards[run, i, last_steps] # Giữ nguyên phần thưởng tích lũy.
                rewards[run, i, min(steps, max_steps - 1)] = rewards[run, i, last_steps] + 1 # Cập nhật phần thưởng khi đạt đích.
                last_steps = steps # Cập nhật last_steps.

                if steps > maze.obstacle_switch_time: # Nếu đã đến thời điểm thay đổi chướng ngại vật.
                    maze.obstacles = maze.new_obstacles # Thay đổi chướng ngại vật.

    rewards = rewards.mean(axis=0) # Lấy trung bình phần thưởng tích lũy qua các lần chạy.

    return rewards # Trả về phần thưởng tích lũy.

# Hàm tạo Hình 8.4: BlockingMaze.
def figure_8_4():
    blocking_maze = Maze() # Tạo một đối tượng mê cung BlockingMaze.
    blocking_maze.START_STATE = [5, 3] # Đặt trạng thái bắt đầu.
    blocking_maze.GOAL_STATES = [[0, 8]] # Đặt trạng thái mục tiêu.
    blocking_maze.old_obstacles = [[3, i] for i in range(0, 8)] # Chướng ngại vật cũ.

    # Chướng ngại vật mới sẽ chặn đường đi tối ưu.
    blocking_maze.new_obstacles = [[3, i] for i in range(1, 9)] # Chướng ngại vật mới.

    blocking_maze.max_steps = 3000 # Giới hạn số bước.

    # Chướng ngại vật sẽ thay đổi sau 1000 bước.
    # Thời điểm chính xác để thay đổi có thể khác nhau.
    # Tuy nhiên, 1000 bước đủ dài để cả hai thuật toán hội tụ, sự khác biệt được đảm bảo rất nhỏ.
    blocking_maze.obstacle_switch_time = 1000

    dyna_params = DynaParams() # Tạo đối tượng tham số Dyna.
    dyna_params.alpha = 1.0 # Tốc độ học.
    dyna_params.planning_steps = 10 # Số bước lập kế hoạch.
    dyna_params.runs = 20 # Số lần chạy.

    # Kappa phải nhỏ, vì phần thưởng khi đạt mục tiêu chỉ là 1.
    dyna_params.time_weight = 1e-4

    rewards = changing_maze(blocking_maze, dyna_params) # Chạy mô phỏng mê cung thay đổi.

    for i in range(len(dyna_params.methods)): # Vẽ biểu đồ phần thưởng tích lũy.
        plt.plot(rewards[i, :], label=dyna_params.methods[i])
    plt.xlabel('time steps') # Nhãn trục x.
    plt.ylabel('cumulative reward') # Nhãn trục y.
    plt.legend() # Hiển thị chú giải.

    plt.savefig('../images/figure_8_4.png') # Lưu biểu đồ.
    plt.close() # Đóng biểu đồ.

# Hàm tạo Hình 8.5: ShortcutMaze.
def figure_8_5():
    shortcut_maze = Maze() # Tạo một đối tượng mê cung ShortcutMaze.
    shortcut_maze.START_STATE = [5, 3] # Đặt trạng thái bắt đầu.
    shortcut_maze.GOAL_STATES = [[0, 8]] # Đặt trạng thái mục tiêu.
    shortcut_maze.old_obstacles = [[3, i] for i in range(1, 9)] # Chướng ngại vật cũ.

    # Chướng ngại vật mới sẽ có một đường đi ngắn hơn.
    shortcut_maze.new_obstacles = [[3, i] for i in range(1, 8)] # Chướng ngại vật mới.

    shortcut_maze.max_steps = 6000 # Giới hạn số bước.

    # Chướng ngại vật sẽ thay đổi sau 3000 bước.
    # Thời điểm chính xác để thay đổi có thể khác nhau.
    # Tuy nhiên, 3000 bước đủ dài để cả hai thuật toán hội tụ, sự khác biệt được đảm bảo rất nhỏ.
    shortcut_maze.obstacle_switch_time = 3000

    dyna_params = DynaParams() # Tạo đối tượng tham số Dyna.

    dyna_params.planning_steps = 50 # Số bước lập kế hoạch.
    dyna_params.runs = 5 # Số lần chạy.
    dyna_params.time_weight = 1e-3 # Trọng số thời gian.
    dyna_params.alpha = 1.0 # Tốc độ học.

    rewards = changing_maze(shortcut_maze, dyna_params) # Chạy mô phỏng mê cung thay đổi.

    for i in range(len(dyna_params.methods)): # Vẽ biểu đồ phần thưởng tích lũy.
        plt.plot( rewards[i, :], label=dyna_params.methods[i])
    plt.xlabel('time steps') # Nhãn trục x.
    plt.ylabel('cumulative reward') # Nhãn trục y.
    plt.legend() # Hiển thị chú giải.

    plt.savefig('../images/figure_8_5.png') # Lưu biểu đồ.
    plt.close() # Đóng biểu đồ.

# Hàm kiểm tra xem các giá trị trạng thái-hành động đã tối ưu hay chưa.
def check_path(q_values, maze):
    # Lấy độ dài của đường đi tối ưu.
    # 14 là độ dài đường đi tối ưu của mê cung gốc.
    # 1.2 có nghĩa là một đường đi tối ưu đã được nới lỏng.
    max_steps = 14 * maze.resolution * 1.2 # Số bước tối đa cho phép để đạt được mục tiêu.
    state = maze.START_STATE # Trạng thái bắt đầu.
    steps = 0 # Đếm số bước.
    while state not in maze.GOAL_STATES: # Lặp cho đến khi đạt mục tiêu.
        action = np.argmax(q_values[state[0], state[1], :]) # Chọn hành động tốt nhất.
        state, _ = maze.step(state, action) # Thực hiện bước.
        steps += 1 # Tăng số bước.
        if steps > max_steps: # Nếu vượt quá số bước tối đa.
            return False # Trả về False (chưa tối ưu).
    return True # Trả về True (đã đạt tối ưu).

# Ví dụ 8.4: Mê cung với độ phân giải khác nhau.
def example_8_4():
    original_maze = Maze() # Lấy mê cung gốc 6 * 9.

    # Thiết lập các tham số cho mỗi thuật toán.
    params_dyna = DynaParams() # Tham số cho Dyna-Q.
    params_dyna.planning_steps = 5
    params_dyna.alpha = 0.5
    params_dyna.gamma = 0.95

    params_prioritized = DynaParams() # Tham số cho Prioritized Sweeping.
    params_prioritized.theta = 0.0001 # Ngưỡng ưu tiên.
    params_prioritized.planning_steps = 5
    params_prioritized.alpha = 0.5
    params_prioritized.gamma = 0.95

    params = [params_prioritized, params_dyna] # Danh sách các bộ tham số.

    # Thiết lập các mô hình cho lập kế hoạch.
    models = [PriorityModel, TrivialModel] # Các lớp mô hình tương ứng.
    method_names = ['Prioritized Sweeping', 'Dyna-Q'] # Tên các phương pháp.

    # Do giới hạn máy của tôi, tôi chỉ có thể thực hiện thí nghiệm cho 5 mê cung.
    # Giả sử mê cung thứ nhất có w * h trạng thái, thì mê cung thứ k có w * h * k * k trạng thái.
    num_of_mazes = 5 # Số lượng mê cung với độ phân giải khác nhau.

    # Xây dựng tất cả các mê cung (từ độ phân giải 1 đến num_of_mazes).
    mazes = [original_maze.extend_maze(i) for i in range(1, num_of_mazes + 1)]
    methods = [prioritized_sweeping, dyna_q] # Các hàm thuật toán tương ứng.

    # Máy của tôi không thể chạy quá nhiều lần...
    runs = 5 # Số lần chạy độc lập.

    backups = np.zeros((runs, 2, num_of_mazes)) # Mảng để lưu trữ tổng số cập nhật (backups).

    for run in range(0, runs): # Lặp qua số lần chạy.
        for i in range(0, len(method_names)): # Lặp qua các phương pháp.
            for mazeIndex, maze in zip(range(0, len(mazes)), mazes): # Lặp qua các mê cung.
                print('run %d, %s, maze size %d' % (run, method_names[i], maze.WORLD_HEIGHT * maze.WORLD_WIDTH))

                q_value = np.zeros(maze.q_size) # Khởi tạo bảng Q-value.

                steps = [] # Danh sách để lưu trữ số bước/backups cho mỗi tập.

                model = models[i]() # Tạo đối tượng mô hình.

                while True: # Vòng lặp cho đến khi tìm thấy đường đi tối ưu.
                    steps.append(methods[i](q_value, model, maze, params[i])) # Chạy thuật toán và lưu số bước/backups.

                    # print best actions w.r.t. current state-action values
                    # printActions(currentStateActionValues, maze)

                    if check_path(q_value, maze): # Kiểm tra xem đường đi tối ưu (nới lỏng) đã được tìm thấy chưa.
                        break # Thoát nếu đã tìm thấy.

                backups[run, i, mazeIndex] = np.sum(steps) # Cập nhật tổng số bước/backups cho mê cung này.

    backups = backups.mean(axis=0) # Lấy trung bình số cập nhật qua các lần chạy.

    # Dyna-Q thực hiện một số cập nhật trên mỗi bước (planning steps).
    backups[1, :] *= params_dyna.planning_steps + 1 # Điều chỉnh số cập nhật cho Dyna-Q.

    for i in range(0, len(method_names)): # Vẽ biểu đồ.
        plt.plot(np.arange(1, num_of_mazes + 1), backups[i, :], label=method_names[i])
    plt.xlabel('maze resolution factor') # Nhãn trục x.
    plt.ylabel('backups until optimal solution') # Nhãn trục y.
    plt.yscale('log') # Đặt trục y theo tỷ lệ log.
    plt.legend() # Hiển thị chú giải.

    plt.savefig('../images/example_8_4.png') # Lưu biểu đồ.
    plt.close() # Đóng biểu đồ.

# Khối thực thi chính: Gọi các hàm tạo hình ảnh.
if __name__ == '__main__':
    figure_8_2()
    figure_8_4()
    figure_8_5()
    example_8_4()

