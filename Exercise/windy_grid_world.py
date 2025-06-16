# Copyright (C)
# 2016-2018 Shangtong Zhang(zhangshangtong.cpp@gmail.com)
# 2016 Kenta Shimada(hyperkentakun@gmail.com)
# Permission given to modify the code as long as you keep this
# declaration at the top
#######################################################################

import numpy as np # Import thư viện NumPy để làm việc với các mảng và phép toán số học.
import matplotlib # Import thư viện Matplotlib để tạo biểu đồ.
matplotlib.use('Agg') # Cấu hình Matplotlib để sử dụng backend 'Agg', cho phép lưu biểu đồ vào file mà không cần hiển thị.
import matplotlib.pyplot as plt # Import module pyplot từ Matplotlib để vẽ biểu đồ.

# Chiều cao của thế giới lưới (grid world).
WORLD_HEIGHT = 7

# Chiều rộng của thế giới lưới (grid world).
WORLD_WIDTH = 10

# Cường độ gió cho mỗi cột. Gió sẽ đẩy agent lên trên.
WIND = [0, 0, 0, 1, 1, 1, 2, 2, 1, 0]

# Các hành động có thể có của agent.
ACTION_UP = 0
ACTION_DOWN = 1
ACTION_LEFT = 2
ACTION_RIGHT = 3

# Xác suất khám phá (exploration) trong chiến lược epsilon-greedy.
EPSILON = 0.1

# Tốc độ học (step size) của thuật toán Sarsa.
ALPHA = 0.5

# Phần thưởng nhận được cho mỗi bước di chuyển (thường là âm để khuyến khích đường đi ngắn nhất).
REWARD = -1.0

START = [3, 0] # Tọa độ trạng thái bắt đầu (hàng, cột).
GOAL = [3, 7] # Tọa độ trạng thái đích (hàng, cột).
ACTIONS = [ACTION_UP, ACTION_DOWN, ACTION_LEFT, ACTION_RIGHT] # Danh sách tất cả các hành động có thể.

# Hàm mô phỏng một bước di chuyển của agent trong môi trường.
def step(state, action):
    i, j = state # Giải nén tọa độ hàng (i) và cột (j) từ trạng thái hiện tại.
    if action == ACTION_UP: # Nếu hành động là di chuyển lên.
        # Tính toán trạng thái tiếp theo: di chuyển lên 1 ô, trừ đi ảnh hưởng của gió,
        # và đảm bảo không vượt quá biên trên (hàng 0).
        return [max(i - 1 - WIND[j], 0), j]
    elif action == ACTION_DOWN: # Nếu hành động là di chuyển xuống.
        # Tính toán trạng thái tiếp theo: di chuyển xuống 1 ô, trừ đi ảnh hưởng của gió,
        # và đảm bảo không vượt quá biên dưới (WORLD_HEIGHT - 1) hoặc biên trên (0).
        return [max(min(i + 1 - WIND[j], WORLD_HEIGHT - 1), 0), j]
    elif action == ACTION_LEFT: # Nếu hành động là di chuyển sang trái.
        # Tính toán trạng thái tiếp theo: di chuyển sang trái 1 ô, di chuyển theo chiều dọc do gió,
        # và đảm bảo không vượt quá biên trái (cột 0) hoặc biên trên (hàng 0).
        return [max(i - WIND[j], 0), max(j - 1, 0)]
    elif action == ACTION_RIGHT: # Nếu hành động là di chuyển sang phải.
        # Tính toán trạng thái tiếp theo: di chuyển sang phải 1 ô, di chuyển theo chiều dọc do gió,
        # và đảm bảo không vượt quá biên phải (WORLD_WIDTH - 1) hoặc biên trên (hàng 0).
        return [max(i - WIND[j], 0), min(j + 1, WORLD_WIDTH - 1)]
    else: # Nếu hành động không hợp lệ.
        assert False # Dừng chương trình với lỗi nếu hành động không được định nghĩa.

# Hàm chạy một tập (episode) của agent cho đến khi đạt được mục tiêu.
def episode(q_value):
    # Biến để theo dõi tổng số bước thời gian trong tập này.
    time = 0

    # Khởi tạo trạng thái ban đầu của agent.
    state = START

    # Chọn hành động đầu tiên dựa trên thuật toán epsilon-greedy.
    if np.random.binomial(1, EPSILON) == 1: # Nếu giá trị ngẫu nhiên nhỏ hơn EPSILON (khám phá).
        action = np.random.choice(ACTIONS) # Chọn một hành động ngẫu nhiên.
    else: # Nếu không khám phá (khai thác).
        values_ = q_value[state[0], state[1], :] # Lấy Q-values cho tất cả các hành động từ trạng thái hiện tại.
        # Chọn ngẫu nhiên một hành động trong số các hành động có Q-value cao nhất (để phá vỡ sự ràng buộc).
        action = np.random.choice([action_ for action_, value_ in enumerate(values_) if value_ == np.max(values_)])

    # Vòng lặp chính của tập, tiếp tục cho đến khi agent đạt đến trạng thái đích.
    while state != GOAL:
        next_state = step(state, action) # Thực hiện hành động và nhận trạng thái tiếp theo.
        # Chọn hành động tiếp theo (next_action) từ trạng thái tiếp theo (next_state) theo epsilon-greedy.
        # Đây là đặc điểm của Sarsa (on-policy).
        if np.random.binomial(1, EPSILON) == 1: # Nếu khám phá.
            next_action = np.random.choice(ACTIONS) # Chọn hành động ngẫu nhiên.
        else: # Nếu khai thác.
            values_ = q_value[next_state[0], next_state[1], :] # Lấy Q-values cho trạng thái tiếp theo.
            # Chọn hành động có Q-value cao nhất từ trạng thái tiếp theo.
            next_action = np.random.choice([action_ for action_, value_ in enumerate(values_) if value_ == np.max(values_)])

        # Cập nhật Q-value theo công thức Sarsa.
        q_value[state[0], state[1], action] += \
            ALPHA * (REWARD + q_value[next_state[0], next_state[1], next_action] - \
                     q_value[state[0], state[1], action])
        state = next_state # Cập nhật trạng thái hiện tại thành trạng thái tiếp theo.
        action = next_action # Cập nhật hành động hiện tại thành hành động tiếp theo.
        time += 1 # Tăng số bước thời gian lên 1.
    return time # Trả về tổng số bước thời gian của tập.

# Hàm chính để chạy thuật toán Sarsa, tạo biểu đồ và hiển thị chính sách tối ưu.
def figure_6_3():
    # Khởi tạo bảng Q-value với tất cả các giá trị là 0.
    # Kích thước: (chiều cao thế giới, chiều rộng thế giới, số lượng hành động).
    q_value = np.zeros((WORLD_HEIGHT, WORLD_WIDTH, 4))
    episode_limit = 500 # Đặt giới hạn số lượng tập sẽ chạy.

    steps = [] # Danh sách để lưu trữ số bước thời gian của mỗi tập.
    ep = 0 # Biến đếm số tập đã chạy.
    while ep < episode_limit: # Lặp cho đến khi đạt giới hạn tập.
        steps.append(episode(q_value)) # Chạy một tập và lưu số bước vào danh sách.
        ep += 1 # Tăng số tập đã chạy.

    steps = np.add.accumulate(steps) # Tính tổng tích lũy của các bước thời gian (tổng số bước cho đến cuối mỗi tập).

    # Tạo biểu đồ đường: Trục x là tổng số bước thời gian, trục y là số tập.
    plt.plot(steps, np.arange(1, len(steps) + 1))
    plt.xlabel('Time steps') # Đặt nhãn trục x.
    plt.ylabel('Episodes') # Đặt nhãn trục y.

    plt.savefig('../REL301M/images/figure_6_3.png') # Lưu biểu đồ vào file ảnh.
    plt.close() # Đóng biểu đồ để giải phóng bộ nhớ.

    print("Q-values sau khi học:") # Thêm dòng in để hiển thị Q-values
    print(q_value) # In ra toàn bộ bảng Q-value.

    # Hiển thị chính sách tối ưu đã học được.
    optimal_policy = [] # Danh sách để lưu trữ biểu diễn chính sách.
    for i in range(0, WORLD_HEIGHT): # Duyệt qua từng hàng.
        optimal_policy.append([]) # Thêm một hàng mới vào chính sách.
        for j in range(0, WORLD_WIDTH): # Duyệt qua từng cột.
            if [i, j] == GOAL: # Nếu ô hiện tại là trạng thái đích.
                optimal_policy[-1].append('G') # Thêm 'G' (Goal) vào chính sách.
                continue # Bỏ qua các bước còn lại và chuyển sang ô tiếp theo.
            bestAction = np.argmax(q_value[i, j, :]) # Tìm hành động có Q-value cao nhất cho trạng thái (i, j).
            if bestAction == ACTION_UP: # Nếu hành động tốt nhất là lên.
                optimal_policy[-1].append('U') # Thêm 'U' (Up).
            elif bestAction == ACTION_DOWN: # Nếu hành động tốt nhất là xuống.
                optimal_policy[-1].append('D') # Thêm 'D' (Down).
            elif bestAction == ACTION_LEFT: # Nếu hành động tốt nhất là trái.
                optimal_policy[-1].append('L') # Thêm 'L' (Left).
            elif bestAction == ACTION_RIGHT: # Nếu hành động tốt nhất là phải.
                optimal_policy[-1].append('R') # Thêm 'R' (Right).
    print('Optimal policy is:') # In tiêu đề.
    for row in optimal_policy: # Duyệt qua từng hàng trong chính sách tối ưu.
        print(row) # In ra hàng chính sách.
    print('Wind strength for each column:\n{}'.format([str(w) for w in WIND])) # In cường độ gió.

# Đảm bảo rằng hàm figure_6_3() chỉ được gọi khi script được chạy trực tiếp.
if __name__ == '__main__':
    figure_6_3() # Gọi hàm chính để bắt đầu quá trình mô phỏng và học.

