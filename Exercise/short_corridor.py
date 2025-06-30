#######################################################################
# Copyright (C)                                                       #
# 2018 Sergii Bondariev (sergeybondarev@gmail.com)                    #
# 2018 Shangtong Zhang(zhangshangtong.cpp@gmail.com)                  #
# Permission given to modify the code as long as you keep this        #
# declaration at the top                                              #
#######################################################################

import numpy as np  # Thư viện toán học cho mảng, ma trận
import matplotlib   # Thư viện vẽ đồ thị
matplotlib.use('Agg')  # Sử dụng backend 'Agg' để vẽ không cần giao diện đồ họa
import matplotlib.pyplot as plt  # Module vẽ đồ thị
from tqdm import tqdm  # Thư viện tạo thanh tiến trình

# Hàm tính giá trị thực của trạng thái đầu tiên dựa trên xác suất đi phải p
# Công thức này được giải từ phương trình Bellman cho môi trường này
# Trả về giá trị thực của trạng thái đầu tiên

def true_value(p):
    return (2 * p - 4) / (p * (1 - p))

# Định nghĩa môi trường "Short Corridor" (Hành lang ngắn)
class ShortCorridor:
    """
    Short corridor environment, xem Example 13.1
    """
    def __init__(self):
        self.reset()  # Đặt lại trạng thái khi khởi tạo

    def reset(self):
        self.state = 0  # Trạng thái bắt đầu là 0

    # Hàm thực hiện một bước trong môi trường
    # go_right: True nếu chọn đi phải, False nếu đi trái
    # Trả về (phần thưởng, đã kết thúc episode chưa)
    def step(self, go_right):
        if self.state == 0 or self.state == 2:
            if go_right:
                self.state += 1  # Nếu đi phải, tăng trạng thái lên 1
            else:
                self.state = max(0, self.state - 1)  # Nếu đi trái, giảm trạng thái nhưng không nhỏ hơn 0
        else:
            if go_right:
                self.state -= 1  # Ở trạng thái 1, đi phải thì giảm trạng thái
            else:
                self.state += 1  # Ở trạng thái 1, đi trái thì tăng trạng thái

        if self.state == 3:
            # Nếu đến trạng thái 3 thì kết thúc episode
            return 0, True  # Phần thưởng 0, kết thúc
        else:
            return -1, False  # Nếu chưa kết thúc, phần thưởng -1

# Hàm softmax để chuẩn hóa xác suất chọn hành động
# Trả về vector xác suất

def softmax(x):
    t = np.exp(x - np.max(x))
    return t / np.sum(t)

# Định nghĩa tác nhân REINFORCE không baseline
class ReinforceAgent:
    """
    Tác nhân REINFORCE theo thuật toán Monte-Carlo Policy-Gradient Control (episodic)
    """
    def __init__(self, alpha, gamma):
        # Khởi tạo tham số chính sách theta, ban đầu ưu tiên đi trái
        self.theta = np.array([-1.47, 1.47])
        self.alpha = alpha  # Tốc độ học
        self.gamma = gamma  # Hệ số chiết khấu
        # x: đặc trưng cho từng hành động (cột 0: trái, cột 1: phải)
        self.x = np.array([[0, 1],
                           [1, 0]])
        self.rewards = []  # Lưu phần thưởng từng bước trong episode
        self.actions = []  # Lưu hành động từng bước trong episode

    # Hàm tính xác suất chọn từng hành động theo softmax
    def get_pi(self):
        h = np.dot(self.theta, self.x)  # Tính giá trị cho từng hành động
        t = np.exp(h - np.max(h))
        pmf = t / np.sum(t)  # Xác suất chọn từng hành động
        # Đảm bảo xác suất không quá nhỏ để tránh chính sách trở nên quyết định tuyệt đối
        imin = np.argmin(pmf)
        epsilon = 0.05

        if pmf[imin] < epsilon:
            pmf[:] = 1 - epsilon
            pmf[imin] = epsilon

        return pmf

    # Trả về xác suất chọn hành động "đi phải"
    def get_p_right(self):
        return self.get_pi()[1]

    # Chọn hành động dựa trên xác suất softmax, lưu lại phần thưởng và hành động
    def choose_action(self, reward):
        if reward is not None:
            self.rewards.append(reward)  # Lưu phần thưởng của bước trước

        pmf = self.get_pi()  # Lấy xác suất chọn hành động
        go_right = np.random.uniform() <= pmf[1]  # Chọn đi phải với xác suất pmf[1]
        self.actions.append(go_right)  # Lưu hành động

        return go_right  # Trả về hành động vừa chọn

    # Khi kết thúc một episode, cập nhật tham số chính sách theta
    def episode_end(self, last_reward):
        self.rewards.append(last_reward)  # Lưu phần thưởng cuối cùng

        # Tính tổng phần thưởng cộng dồn G cho từng bước
        G = np.zeros(len(self.rewards))
        G[-1] = self.rewards[-1]

        for i in range(2, len(G) + 1):
            G[-i] = self.gamma * G[-i + 1] + self.rewards[-i]

        gamma_pow = 1  # Lưu giá trị gamma^t

        for i in range(len(G)):
            j = 1 if self.actions[i] else 0  # 1 nếu đi phải, 0 nếu đi trái
            pmf = self.get_pi()  # Xác suất hiện tại
            grad_ln_pi = self.x[:, j] - np.dot(self.x, pmf)  # Gradient của log xác suất
            update = self.alpha * gamma_pow * G[i] * grad_ln_pi  # Tính giá trị cập nhật

            self.theta += update  # Cập nhật tham số chính sách
            gamma_pow *= self.gamma  # Nhân gamma cho bước tiếp theo

        self.rewards = []  # Reset lại phần thưởng cho episode mới
        self.actions = []  # Reset lại hành động cho episode mới

# Định nghĩa tác nhân REINFORCE có baseline
class ReinforceBaselineAgent(ReinforceAgent):
    def __init__(self, alpha, gamma, alpha_w):
        super(ReinforceBaselineAgent, self).__init__(alpha, gamma)
        self.alpha_w = alpha_w  # Tốc độ học cho baseline
        self.w = 0  # Baseline (ước lượng giá trị trung bình)

    # Khi kết thúc episode, cập nhật cả baseline w và tham số chính sách theta
    def episode_end(self, last_reward):
        self.rewards.append(last_reward)

        # Tính tổng phần thưởng cộng dồn G cho từng bước
        G = np.zeros(len(self.rewards))
        G[-1] = self.rewards[-1]

        for i in range(2, len(G) + 1):
            G[-i] = self.gamma * G[-i + 1] + self.rewards[-i]

        gamma_pow = 1

        for i in range(len(G)):
            self.w += self.alpha_w * gamma_pow * (G[i] - self.w)  # Cập nhật baseline

            j = 1 if self.actions[i] else 0
            pmf = self.get_pi()
            grad_ln_pi = self.x[:, j] - np.dot(self.x, pmf)
            update = self.alpha * gamma_pow * (G[i] - self.w) * grad_ln_pi  # Cập nhật theta dựa trên phần thưởng trừ baseline

            self.theta += update
            gamma_pow *= self.gamma

        self.rewards = []
        self.actions = []

# Hàm chạy thử nghiệm một tác nhân trong môi trường qua nhiều episode
# Trả về mảng tổng phần thưởng mỗi episode

def trial(num_episodes, agent_generator):
    env = ShortCorridor()  # Tạo môi trường
    agent = agent_generator()  # Tạo tác nhân

    rewards = np.zeros(num_episodes)  # Mảng lưu tổng phần thưởng mỗi episode
    for episode_idx in range(num_episodes):
        rewards_sum = 0  # Tổng phần thưởng của episode hiện tại
        reward = None
        env.reset()  # Đặt lại môi trường

        while True:
            go_right = agent.choose_action(reward)  # Tác nhân chọn hành động
            reward, episode_end = env.step(go_right)  # Thực hiện hành động trong môi trường
            rewards_sum += reward  # Cộng dồn phần thưởng

            if episode_end:
                agent.episode_end(reward)  # Cập nhật chính sách khi kết thúc episode
                break

        rewards[episode_idx] = rewards_sum  # Lưu tổng phần thưởng của episode

    return rewards  # Trả về mảng tổng phần thưởng

# Hàm vẽ hình ví dụ 13.1: giá trị thực của trạng thái đầu tiên theo xác suất đi phải

def example_13_1():
    epsilon = 0.05  # Xác suất cho chính sách epsilon-greedy
    fig, ax = plt.subplots(1, 1)  # Tạo figure và trục

    p = np.linspace(0.01, 0.99, 100)  # Mảng xác suất đi phải từ 0.01 đến 0.99
    y = true_value(p)  # Tính giá trị thực cho từng p
    ax.plot(p, y, color='red')  # Vẽ đường cong giá trị thực

    imax = np.argmax(y)  # Tìm chỉ số giá trị lớn nhất
    pmax = p[imax]  # Giá trị p tại cực đại
    ymax = y[imax]  # Giá trị y tại cực đại
    ax.plot(pmax, ymax, color='green', marker="*", label="optimal point: f({0:.2f}) = {1:.2f}".format(pmax, ymax))  # Đánh dấu cực đại

    ax.plot(epsilon, true_value(epsilon), color='magenta', marker="o", label="epsilon-greedy left")  # Đánh dấu epsilon-greedy trái
    ax.plot(1 - epsilon, true_value(1 - epsilon), color='blue', marker="o", label="epsilon-greedy right")  # Đánh dấu epsilon-greedy phải

    ax.set_ylabel("Value of the first state")  # Nhãn trục tung
    ax.set_xlabel("Probability of the action 'right'")  # Nhãn trục hoành
    ax.set_title("Short corridor with switched actions")  # Tiêu đề
    ax.set_ylim(ymin=-105.0, ymax=5)  # Giới hạn trục tung
    ax.legend()  # Hiển thị chú thích

    plt.savefig('example_13_1.png')  # Lưu hình ra file
    plt.close()  # Đóng figure

# Hàm vẽ hình 13.1: so sánh tác động của các giá trị alpha khác nhau

def figure_13_1():
    num_trials = 100  # Số lần thử nghiệm độc lập
    num_episodes = 1000  # Số tập mỗi lần thử
    gamma = 1  # Hệ số chiết khấu
    agent_generators = [
        lambda : ReinforceAgent(alpha=2e-4, gamma=gamma),  # alpha = 2e-4
        lambda : ReinforceAgent(alpha=2e-5, gamma=gamma),  # alpha = 2e-5
        lambda : ReinforceAgent(alpha=2e-3, gamma=gamma)   # alpha = 2e-3
    ]
    labels = [
        'alpha = 2e-4',
        'alpha = 2e-5',
        'alpha = 2e-3'
    ]

    rewards = np.zeros((len(agent_generators), num_trials, num_episodes))  # Mảng lưu tổng phần thưởng

    for agent_index, agent_generator in enumerate(agent_generators):
        for i in tqdm(range(num_trials)):
            reward = trial(num_episodes, agent_generator)  # Chạy thử nghiệm
            rewards[agent_index, i, :] = reward  # Lưu kết quả

    plt.plot(
        np.arange(num_episodes) + 1,              # Trục x: số tập
        -11.6 * np.ones(num_episodes),            # Trục y: giá trị tối ưu
        ls='dashed', color='red', label='-11.6'   # Đường tham chiếu
    )
    for i, label in enumerate(labels):
        plt.plot(
            np.arange(num_episodes) + 1,          # Trục x
            rewards[i].mean(axis=0),              # Trung bình phần thưởng
            label=label                           # Nhãn
        )
    plt.ylabel('total reward on episode')  # Nhãn trục tung
    plt.xlabel('episode')  # Nhãn trục hoành
    plt.legend(loc='lower right')  # Chú thích

    plt.savefig('figure_13_1.png')  # Lưu hình
    plt.close()  # Đóng figure

# Hàm vẽ hình 13.2: so sánh tác nhân có baseline và không baseline

def figure_13_2():
    num_trials = 100  # Số lần thử nghiệm độc lập
    num_episodes = 1000  # Số tập mỗi lần thử
    alpha = 2e-4  # Giá trị alpha
    gamma = 1  # Hệ số chiết khấu
    agent_generators = [lambda : ReinforceAgent(alpha=alpha, gamma=gamma),
                        lambda : ReinforceBaselineAgent(alpha=alpha*10, gamma=gamma, alpha_w=alpha*100)]
    labels = ['Reinforce without baseline',
              'Reinforce with baseline']

    rewards = np.zeros((len(agent_generators), num_trials, num_episodes))  # Mảng lưu tổng phần thưởng

    for agent_index, agent_generator in enumerate(agent_generators):
        for i in tqdm(range(num_trials)):
            reward = trial(num_episodes, agent_generator)  # Chạy thử nghiệm
            rewards[agent_index, i, :] = reward  # Lưu kết quả

    plt.plot(np.arange(num_episodes) + 1, -11.6 * np.ones(num_episodes), ls='dashed', color='red', label='-11.6')  # Đường tham chiếu
    for i, label in enumerate(labels):
        plt.plot(np.arange(num_episodes) + 1, rewards[i].mean(axis=0), label=label)  # Vẽ đường trung bình
    plt.ylabel('total reward on episode')  # Nhãn trục tung
    plt.xlabel('episode')  # Nhãn trục hoành
    plt.legend(loc='lower right')  # Chú thích

    plt.savefig('figure_13_2.png')  # Lưu hình
    plt.close()  # Đóng figure

# Khi chạy file này trực tiếp, sẽ tự động vẽ và lưu 3 hình minh họa
if __name__ == '__main__':
    example_13_1()  # Vẽ và lưu hình ví dụ 13.1
    figure_13_1()   # Vẽ và lưu hình 13.1 (so sánh alpha)
    figure_13_2()   # Vẽ và lưu hình 13.2 (so sánh baseline)
