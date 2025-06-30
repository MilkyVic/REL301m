# Phần 1: Import các thư viện cần thiết
import numpy as np  # Thư viện tính toán số học
import matplotlib
matplotlib.use('Agg')  # Sử dụng backend Agg cho matplotlib
import matplotlib.pyplot as plt  # Thư viện vẽ đồ thị
from tqdm import tqdm  # Thư viện hiển thị thanh tiến trình
from mpl_toolkits.mplot3d.axes3d import Axes3D  # Thư viện vẽ đồ thị 3D
from math import floor  # Hàm làm tròn xuống
import seaborn as sns  # Thư viện vẽ đồ thị thống kê

# Phần 2: Các hằng số và biến toàn cục
PRIORITIES = np.arange(0, 4)  # Các mức độ ưu tiên từ 0 đến 3
REWARDS = np.power(2, np.arange(0, 4))  # Phần thưởng cho mỗi mức độ ưu tiên (2^priority)

# Các hành động có thể thực hiện
REJECT = 0  # Từ chối
ACCEPT = 1  # Chấp nhận
ACTIONS = [REJECT, ACCEPT]

NUM_OF_SERVERS = 10  # Tổng số máy chủ
PROBABILITY_FREE = 0.06  # Xác suất một máy chủ bận sẽ trở nên rảnh
ALPHA = 0.01  # Hệ số học cho giá trị trạng thái-hành động
BETA = 0.01  # Hệ số học cho phần thưởng trung bình
EPSILON = 0.1  # Xác suất khám phá (exploration)

# Phần 3: Class ValueFunction - Hàm giá trị
class ValueFunction:
    def __init__(self, num_of_tilings, alpha=ALPHA, beta=BETA):
        self.num_of_tilings = num_of_tilings  # Số lượng tiling
        self.max_size = 2048  # Kích thước tối đa của bảng băm
        self.hash_table = IHT(self.max_size)  # Bảng băm để xử lý va chạm
        self.weights = np.zeros(self.max_size)  # Trọng số cho mỗi tile

        # Tỷ lệ co giãn cho các đặc trưng
        self.server_scale = self.num_of_tilings / float(NUM_OF_SERVERS)
        self.priority_scale = self.num_of_tilings / float(len(PRIORITIES) - 1)

        self.average_reward = 0.0  # Phần thưởng trung bình
        self.alpha = alpha / self.num_of_tilings  # Chia đều hệ số học cho mỗi tiling
        self.beta = beta  # Hệ số học cho phần thưởng trung bình

    def get_active_tiles(self, free_servers, priority, action):
        # Lấy các tile đang hoạt động cho trạng thái và hành động
        active_tiles = tiles(self.hash_table, self.num_of_tilings,
                            [self.server_scale * free_servers, self.priority_scale * priority],
                            [action])
        return active_tiles

    def value(self, free_servers, priority, action):
        # Ước tính giá trị của trạng thái-hành động
        active_tiles = self.get_active_tiles(free_servers, priority, action)
        return np.sum(self.weights[active_tiles])

    def state_value(self, free_servers, priority):
        # Ước tính giá trị của trạng thái
        values = [self.value(free_servers, priority, action) for action in ACTIONS]
        if free_servers == 0:
            return values[REJECT]
        return np.max(values)

    def learn(self, free_servers, priority, action, new_free_servers, new_priority, new_action, reward):
        # Học từ chuỗi trạng thái-hành động
        active_tiles = self.get_active_tiles(free_servers, priority, action)
        estimation = np.sum(self.weights[active_tiles])
        # Tính delta (sai số)
        delta = reward - self.average_reward + self.value(new_free_servers, new_priority, new_action) - estimation
        # Cập nhật phần thưởng trung bình
        self.average_reward += self.beta * delta
        delta *= self.alpha
        # Cập nhật trọng số
        for active_tile in active_tiles:
            self.weights[active_tile] += delta

# Phần 4: Các hàm phụ trợ
def get_action(free_servers, priority, value_function):
    # Lấy hành động dựa trên chính sách epsilon-greedy
    if free_servers == 0:
        return REJECT
    if np.random.binomial(1, EPSILON) == 1:
        return np.random.choice(ACTIONS)
    values = [value_function.value(free_servers, priority, action) for action in ACTIONS]
    return np.random.choice([action_ for action_, value_ in enumerate(values) if value_ == np.max(values)])

def take_action(free_servers, priority, action):
    # Thực hiện hành động và nhận phần thưởng
    if free_servers > 0 and action == ACCEPT:
        free_servers -= 1
    reward = REWARDS[priority] * action
    # Một số máy chủ bận có thể trở nên rảnh
    busy_servers = NUM_OF_SERVERS - free_servers
    free_servers += np.random.binomial(busy_servers, PROBABILITY_FREE)
    return free_servers, np.random.choice(PRIORITIES), reward

# Phần 5: Thuật toán Differential Semi-gradient Sarsa
def differential_semi_gradient_sarsa(value_function, max_steps):
    # Khởi tạo trạng thái và hành động ban đầu
    current_free_servers = NUM_OF_SERVERS
    current_priority = np.random.choice(PRIORITIES)
    current_action = get_action(current_free_servers, current_priority, value_function)
    freq = np.zeros(NUM_OF_SERVERS + 1)  # Theo dõi tần suất số máy chủ rảnh

    for _ in tqdm(range(max_steps)):
        freq[current_free_servers] += 1
        # Thực hiện hành động và nhận phần thưởng
        new_free_servers, new_priority, reward = take_action(current_free_servers, current_priority, current_action)
        new_action = get_action(new_free_servers, new_priority, value_function)
        # Học từ trải nghiệm
        value_function.learn(current_free_servers, current_priority, current_action,
                             new_free_servers, new_priority, new_action, reward)
        # Cập nhật trạng thái và hành động
        current_free_servers = new_free_servers
        current_priority = new_priority
        current_action = new_action

# Phần 6: Hàm vẽ đồ thị
def figure_10_5():
    max_steps = int(1e6)  # Số bước học
    num_of_tilings = 8  # Số lượng tiling
    value_function = ValueFunction(num_of_tilings)
    differential_semi_gradient_sarsa(value_function, max_steps)
    
    # Tính toán và vẽ giá trị
    values = np.zeros((len(PRIORITIES), NUM_OF_SERVERS + 1))
    for priority in PRIORITIES:
        for free_servers in range(NUM_OF_SERVERS + 1):
            values[priority, free_servers] = value_function.state_value(free_servers, priority)

    # Vẽ đồ thị giá trị
    fig = plt.figure(figsize=(10, 20))
    plt.subplot(2, 1, 1)
    for priority in PRIORITIES:
        plt.plot(range(NUM_OF_SERVERS + 1), values[priority, :], label='priority %d' % (REWARDS[priority]))
    plt.xlabel('Số máy chủ rảnh')
    plt.ylabel('Giá trị vi phân của hành động tốt nhất')
    plt.legend()

    # Vẽ đồ thị chính sách
    ax = fig.add_subplot(2, 1, 2)
    policy = np.zeros((len(PRIORITIES), NUM_OF_SERVERS + 1))
    for priority in PRIORITIES:
        for free_servers in range(NUM_OF_SERVERS + 1):
            values = [value_function.value(free_servers, priority, action) for action in ACTIONS]
            if free_servers == 0:
                policy[priority, free_servers] = REJECT
            else:
                policy[priority, free_servers] = np.argmax(values)

    # Vẽ heatmap chính sách
    fig = sns.heatmap(policy, cmap="YlGnBu", ax=ax, xticklabels=range(NUM_OF_SERVERS + 1), yticklabels=PRIORITIES)
    fig.set_title('Chính sách (0 Từ chối, 1 Chấp nhận)')
    fig.set_xlabel('Số máy chủ rảnh')
    fig.set_ylabel('Mức độ ưu tiên')

    plt.savefig('../REL301M/Exercise/images/figure_10_5.png')
    plt.close()