#######################################################################
# Bản quyền (C)                                                       #
# 2016-2018 Shangtong Zhang(zhangshangtong.cpp@gmail.com)             #
# 2016 Kenta Shimada(hyperkentakun@gmail.com)                         #
# Được phép chỉnh sửa mã nguồn miễn là giữ phần khai báo này           #
#######################################################################

import numpy as np  # Thư viện toán học, đặc biệt là mảng số
import matplotlib
matplotlib.use('Agg')  # Thiết lập backend cho matplotlib để vẽ không cần giao diện
import matplotlib.pyplot as plt  # Thư viện vẽ đồ thị
from tqdm import tqdm  # Hiển thị tiến trình vòng lặp
from mpl_toolkits.mplot3d.axes3d import Axes3D  # Hỗ trợ vẽ 3D (không dùng trong code này)
from math import floor  # Hàm làm tròn xuống
import seaborn as sns  # Thư viện vẽ biểu đồ đẹp

#######################################################################
# Các hàm tiện ích cho tile coding (mã hóa trạng thái-hành động)
# Được lấy từ Rich Sutton, chỉnh sửa lại cho phù hợp
# Tile coding bắt đầu
class IHT:
    "Cấu trúc để xử lý va chạm trong tile coding"
    def __init__(self, size_val):
        self.size = size_val  # Kích thước bảng băm
        self.overfull_count = 0  # Đếm số lần bị đầy
        self.dictionary = {}  # Lưu trữ ánh xạ

    def count(self):
        return len(self.dictionary)  # Số lượng phần tử đã lưu

    def full(self):
        return len(self.dictionary) >= self.size  # Kiểm tra đã đầy chưa

    def get_index(self, obj, read_only=False):
        d = self.dictionary
        if obj in d:
            return d[obj]  # Nếu đã có thì trả về chỉ số
        elif read_only:
            return None
        size = self.size
        count = self.count()
        if count >= size:
            if self.overfull_count == 0: print('IHT full, bắt đầu cho phép va chạm')
            self.overfull_count += 1
            return hash(obj) % self.size  # Nếu đầy thì dùng hash
        else:
            d[obj] = count
            return count  # Thêm mới

def hash_coords(coordinates, m, read_only=False):
    # Hàm băm cho tile coding
    if isinstance(m, IHT): return m.get_index(tuple(coordinates), read_only)
    if isinstance(m, int): return hash(tuple(coordinates)) % m
    if m is None: return coordinates

def tiles(iht_or_size, num_tilings, floats, ints=None, read_only=False):
    """Trả về các chỉ số tile cho trạng thái-hành động"""
    if ints is None:
        ints = []
    qfloats = [floor(f * num_tilings) for f in floats]  # Chuẩn hóa giá trị liên tục
    tiles = []
    for tiling in range(num_tilings):
        tilingX2 = tiling * 2
        coords = [tiling]
        b = tiling
        for q in qfloats:
            coords.append((q + b) // num_tilings)
            b += tilingX2
        coords.extend(ints)
        tiles.append(hash_coords(coords, iht_or_size, read_only))
    return tiles
# Kết thúc tile coding
#######################################################################

# Các mức ưu tiên có thể có
PRIORITIES = np.arange(0, 4)
# Phần thưởng cho mỗi mức ưu tiên
REWARDS = np.power(2, np.arange(0, 4))

# Các hành động có thể: từ chối (0), chấp nhận (1)
REJECT = 0
ACCEPT = 1
ACTIONS = [REJECT, ACCEPT]

# Tổng số server
NUM_OF_SERVERS = 10

# Xác suất một server bận sẽ rảnh ở mỗi bước
PROBABILITY_FREE = 0.06

# Tốc độ học cho giá trị trạng thái-hành động
ALPHA = 0.01

# Tốc độ học cho phần thưởng trung bình
BETA = 0.01

# Xác suất chọn ngẫu nhiên (exploration)
EPSILON = 0.1

# Lớp bao bọc cho hàm giá trị trạng thái-hành động (differential semi-gradient Sarsa)
class ValueFunction:
    # Trong ví dụ này sử dụng tile coding với phần mềm có sẵn
    # Tiling chỉ là ánh xạ từ (trạng thái, hành động) sang một loạt chỉ số
    # Không quan trọng ý nghĩa chỉ số, chỉ cần ánh xạ này thỏa mãn tính chất phân biệt
    def __init__(self, num_of_tilings, alpha=ALPHA, beta=BETA):
        self.num_of_tilings = num_of_tilings  # Số lượng tiling
        self.max_size = 2048  # Kích thước bảng băm
        self.hash_table = IHT(self.max_size)  # Bảng băm cho tile coding
        self.weights = np.zeros(self.max_size)  # Trọng số cho các tile

        # Tỉ lệ scale cho trạng thái
        self.server_scale = self.num_of_tilings / float(NUM_OF_SERVERS)
        self.priority_scale = self.num_of_tilings / float(len(PRIORITIES) - 1)

        self.average_reward = 0.0  # Phần thưởng trung bình

        # Chia nhỏ tốc độ học cho từng tiling
        self.alpha = alpha / self.num_of_tilings

        self.beta = beta

    # Lấy chỉ số các tile đang hoạt động cho trạng thái-hành động
    def get_active_tiles(self, free_servers, priority, action):
        active_tiles = tiles(self.hash_table, self.num_of_tilings,
                            [self.server_scale * free_servers, self.priority_scale * priority],
                            [action])
        return active_tiles

    # Ước lượng giá trị trạng thái-hành động
    def value(self, free_servers, priority, action):
        active_tiles = self.get_active_tiles(free_servers, priority, action)
        return np.sum(self.weights[active_tiles])

    # Ước lượng giá trị trạng thái (lấy max theo hành động)
    def state_value(self, free_servers, priority):
        values = [self.value(free_servers, priority, action) for action in ACTIONS]
        # Nếu không còn server rảnh thì chỉ có thể từ chối
        if free_servers == 0:
            return values[REJECT]
        return np.max(values)

    # Học từ một bước chuyển
    def learn(self, free_servers, priority, action, new_free_servers, new_priority, new_action, reward):
        active_tiles = self.get_active_tiles(free_servers, priority, action)
        estimation = np.sum(self.weights[active_tiles])
        delta = reward - self.average_reward + self.value(new_free_servers, new_priority, new_action) - estimation
        # Cập nhật phần thưởng trung bình
        self.average_reward += self.beta * delta
        delta *= self.alpha
        for active_tile in active_tiles:
            self.weights[active_tile] += delta

# Chọn hành động theo epsilon-greedy
# Nếu không còn server rảnh thì chỉ có thể từ chối
# Nếu random nhỏ hơn epsilon thì chọn ngẫu nhiên, ngược lại chọn hành động tốt nhất
# Nếu có nhiều hành động tốt nhất thì chọn ngẫu nhiên trong số đó

def get_action(free_servers, priority, value_function):
    if free_servers == 0:
        return REJECT
    if np.random.binomial(1, EPSILON) == 1:
        return np.random.choice(ACTIONS)
    values = [value_function.value(free_servers, priority, action) for action in ACTIONS]
    return np.random.choice([action_ for action_, value_ in enumerate(values) if value_ == np.max(values)])

# Thực hiện một hành động
# Nếu chấp nhận thì giảm số server rảnh đi 1
# Phần thưởng nhận được phụ thuộc vào mức ưu tiên và hành động
# Một số server bận có thể trở nên rảnh dựa trên xác suất PROBABILITY_FREE
# Trả về trạng thái mới và phần thưởng

def take_action(free_servers, priority, action):
    if free_servers > 0 and action == ACCEPT:
        free_servers -= 1  # Nhận yêu cầu, giảm server rảnh
    reward = REWARDS[priority] * action  # Phần thưởng nếu chấp nhận
    busy_servers = NUM_OF_SERVERS - free_servers  # Số server đang bận
    free_servers += np.random.binomial(busy_servers, PROBABILITY_FREE)  # Một số server bận trở nên rảnh
    return free_servers, np.random.choice(PRIORITIES), reward

# Thuật toán differential semi-gradient Sarsa
# Khởi tạo trạng thái ban đầu, lặp lại max_steps bước
# Ở mỗi bước: thực hiện hành động, cập nhật giá trị, chuyển sang trạng thái mới
# Theo dõi tần suất xuất hiện của từng số lượng server rảnh

def differential_semi_gradient_sarsa(value_function, max_steps):
    current_free_servers = NUM_OF_SERVERS  # Bắt đầu với tất cả server rảnh
    current_priority = np.random.choice(PRIORITIES)  # Chọn ngẫu nhiên mức ưu tiên
    current_action = get_action(current_free_servers, current_priority, value_function)
    freq = np.zeros(NUM_OF_SERVERS + 1)  # Theo dõi số lần mỗi trạng thái server rảnh xuất hiện

    for _ in tqdm(range(max_steps)):
        freq[current_free_servers] += 1
        new_free_servers, new_priority, reward = take_action(current_free_servers, current_priority, current_action)
        new_action = get_action(new_free_servers, new_priority, value_function)
        value_function.learn(current_free_servers, current_priority, current_action,
                             new_free_servers, new_priority, new_action, reward)
        current_free_servers = new_free_servers
        current_priority = new_priority
        current_action = new_action
    print('Tần suất số lượng server rảnh:')
    print(freq / max_steps)

# Hàm vẽ hình 10.5: Kết quả thuật toán Sarsa bán-gradient vi phân trên bài toán xếp hàng access-control
# Vẽ giá trị trạng thái và chính sách tối ưu cho từng mức ưu tiên và số server rảnh

def figure_10_5():
    max_steps = int(1e6)  # Số bước mô phỏng (1 triệu bước)
    num_of_tilings = 8  # Số lượng tiling dùng cho tile coding
    value_function = ValueFunction(num_of_tilings)  # Khởi tạo hàm giá trị với tile coding
    differential_semi_gradient_sarsa(value_function, max_steps)  # Chạy thuật toán Sarsa để học
    values = np.zeros((len(PRIORITIES), NUM_OF_SERVERS + 1))  # Ma trận lưu giá trị trạng thái cho từng mức ưu tiên và số server rảnh
    for priority in PRIORITIES:
        for free_servers in range(NUM_OF_SERVERS + 1):
            values[priority, free_servers] = value_function.state_value(free_servers, priority)  # Lưu giá trị trạng thái

    fig = plt.figure(figsize=(10, 20))  # Tạo figure với kích thước lớn
    plt.subplot(2, 1, 1)  # Vẽ subplot đầu tiên (trên cùng)
    for priority in PRIORITIES:
        plt.plot(range(NUM_OF_SERVERS + 1), values[priority, :], label='priority %d' % (REWARDS[priority]))  # Vẽ đường giá trị cho từng mức ưu tiên
    plt.xlabel('Số lượng server rảnh')  # Nhãn trục x
    plt.ylabel('Giá trị vi phân của hành động tốt nhất')  # Nhãn trục y
    plt.legend()  # Hiển thị chú thích

    ax = fig.add_subplot(2, 1, 2)  # Thêm subplot thứ hai (bên dưới)
    policy = np.zeros((len(PRIORITIES), NUM_OF_SERVERS + 1))  # Ma trận lưu chính sách tối ưu
    for priority in PRIORITIES:
        for free_servers in range(NUM_OF_SERVERS + 1):
            values = [value_function.value(free_servers, priority, action) for action in ACTIONS]  # Giá trị cho từng hành động
            if free_servers == 0:
                policy[priority, free_servers] = REJECT  # Nếu không còn server rảnh thì luôn từ chối
            else:
                policy[priority, free_servers] = np.argmax(values)  # Chọn hành động có giá trị lớn nhất

    fig = sns.heatmap(policy, cmap="YlGnBu", ax=ax, xticklabels=range(NUM_OF_SERVERS + 1), yticklabels=PRIORITIES)  # Vẽ heatmap cho chính sách
    fig.set_title('Chính sách (0: Từ chối, 1: Chấp nhận)')  # Tiêu đề biểu đồ
    fig.set_xlabel('Số lượng server rảnh')  # Nhãn trục x
    fig.set_ylabel('Mức ưu tiên')  # Nhãn trục y

    plt.savefig('figure_10_5.png')  # Lưu hình ngay tại thư mục hiện tại
    plt.close()  # Đóng figure để giải phóng bộ nhớ

# Nếu chạy file này trực tiếp thì sẽ vẽ hình 10.5
if __name__ == '__main__':
    figure_10_5()  # Gọi hàm vẽ hình
