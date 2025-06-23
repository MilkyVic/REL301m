# Phần 1: Import các thư viện cần thiết
import numpy as np  # Thư viện cho tính toán số học
import matplotlib
matplotlib.use('Agg')  # Sử dụng backend Agg cho matplotlib (phù hợp cho môi trường không có GUI)
import matplotlib.pyplot as plt  # Thư viện vẽ đồ thị
from tqdm import tqdm  # Thư viện hiển thị thanh tiến trình

# Phần 2: Định nghĩa class Interval để biểu diễn khoảng
class Interval:
    def __init__(self, left, right):
        self.left = left  # Giá trị bắt đầu của khoảng
        self.right = right  # Giá trị kết thúc của khoảng

    def contain(self, x):
        # Kiểm tra xem một điểm có nằm trong khoảng không
        return self.left <= x < self.right

    def size(self):
        # Tính độ dài của khoảng
        return self.right - self.left

# Định nghĩa miền xác định của sóng vuông: [0, 2)
DOMAIN = Interval(0.0, 2.0)

# Phần 3: Định nghĩa hàm sóng vuông
def square_wave(x):
    # Trả về 1 nếu x nằm trong khoảng (0.5, 1.5), ngược lại trả về 0
    if 0.5 < x < 1.5:
        return 1
    return 0

# Phần 4: Hàm lấy mẫu ngẫu nhiên
def sample(n):
    samples = []
    for i in range(0, n):
        x = np.random.uniform(DOMAIN.left, DOMAIN.right)  # Tạo điểm ngẫu nhiên trong miền xác định
        y = square_wave(x)  # Tính giá trị sóng vuông tại điểm đó
        samples.append([x, y])
    return samples

# Phần 5: Class ValueFunction để xấp xỉ hàm
class ValueFunction:
    def __init__(self, feature_width, domain=DOMAIN, alpha=0.2, num_of_features=50):
        self.feature_width = feature_width  # Độ rộng của mỗi đặc trưng
        self.num_of_featrues = num_of_features  # Số lượng đặc trưng
        self.features = []  # Danh sách các khoảng đặc trưng
        self.alpha = alpha  # Hệ số học
        self.domain = domain  # Miền xác định

        # Tạo các khoảng đặc trưng
        step = (domain.size() - feature_width) / (num_of_features - 1)
        left = domain.left
        for i in range(0, num_of_features - 1):
            self.features.append(Interval(left, left + feature_width))
            left += step
        self.features.append(Interval(left, domain.right))

        # Khởi tạo trọng số cho mỗi đặc trưng
        self.weights = np.zeros(num_of_features)

    def get_active_features(self, x):
        # Tìm các đặc trưng đang hoạt động tại điểm x
        active_features = []
        for i in range(0, len(self.features)):
            if self.features[i].contain(x):
                active_features.append(i)
        return active_features

    def value(self, x):
        # Ước tính giá trị tại điểm x
        active_features = self.get_active_features(x)
        return np.sum(self.weights[active_features])

    def update(self, delta, x):
        # Cập nhật trọng số dựa trên sai số
        active_features = self.get_active_features(x)
        delta *= self.alpha / len(active_features)
        for index in active_features:
            self.weights[index] += delta

# Phần 6: Hàm xấp xỉ
def approximate(samples, value_function):
    # Huấn luyện value_function với tập mẫu
    for x, y in samples:
        delta = y - value_function.value(x)  # Tính sai số
        value_function.update(delta, x)  # Cập nhật trọng số

# Phần 7: Hàm vẽ đồ thị
def figure_9_8():
    # Các số lượng mẫu khác nhau để thử nghiệm
    num_of_samples = [10, 40, 160, 640, 2560, 10240]
    # Các độ rộng đặc trưng khác nhau
    feature_widths = [0.2, 0.4, 1.0]
    
    plt.figure(figsize=(30, 20))  # Tạo figure với kích thước lớn
    axis_x = np.arange(DOMAIN.left, DOMAIN.right, 0.02)  # Tạo các điểm x để vẽ
    
    # Vẽ đồ thị cho mỗi số lượng mẫu
    for index, num_of_sample in enumerate(num_of_samples):
        print(num_of_sample, 'samples')
        samples = sample(num_of_sample)
        value_functions = [ValueFunction(feature_width) for feature_width in feature_widths]
        
        plt.subplot(2, 3, index + 1)  # Tạo subplot
        plt.title('%d samples' % (num_of_sample))
        
        # Vẽ đường xấp xỉ cho mỗi độ rộng đặc trưng
        for value_function in value_functions:
            approximate(samples, value_function)
            values = [value_function.value(x) for x in axis_x]
            plt.plot(axis_x, values, label='feature width %.01f' % (value_function.feature_width))
        plt.legend()

    plt.savefig('figure_9_8.png')  # Lưu đồ thị
    plt.close()

# Phần 8: Điểm khởi đầu của chương trình
if __name__ == '__main__':
    figure_9_8()