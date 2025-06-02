# Hàm Giá Trị Tối Ưu (Optimal Value Function)

## 1. Tổng Quan
Hàm giá trị tối ưu là khái niệm cốt lõi trong học tăng cường, đại diện cho giá trị tốt nhất có thể đạt được trong mỗi trạng thái. Nó liên quan trực tiếp đến chính sách tối ưu và các phương trình Bellman tối ưu.

## 2. Chính Sách Tối Ưu

### 2.1. Định Nghĩa
- Chính sách tối ưu (π*) là chính sách tốt hơn hoặc bằng mọi chính sách khác
- Dẫn đến giá trị cao nhất trong mọi trạng thái
- Được ký hiệu là π*

### 2.2. Đặc Điểm
- Giá trị của chính sách tối ưu là giá trị lớn nhất có thể đạt được
- Được tính toán trên tất cả các chính sách có thể
- Đảm bảo hiệu suất tốt nhất trong mọi trạng thái

## 3. Phương Trình Bellman Tối Ưu

### 3.1. Cho Hàm Giá Trị Trạng Thái (v*)
$$v^*(s) = \max_a \mathbb{E}[R_{t+1} + \gamma v^*(S_{t+1})|S_t=s,A_t=a]$$

Hoặc dạng đầy đủ:
$$v^*(s) = \max_a \sum_{s'} P(s'|s,a)[R(s,a,s') + \gamma v^*(s')]$$

Trong đó:
- $v^*(s)$: Giá trị tối ưu của trạng thái s
- $\max_a$: Lấy giá trị lớn nhất trên tất cả các hành động có thể
- $P(s'|s,a)$: Xác suất chuyển đến trạng thái s' từ s khi thực hiện hành động a
- $R(s,a,s')$: Phần thưởng nhận được khi chuyển từ s sang s' bằng hành động a

### 3.2. Cho Hàm Giá Trị Hành Động (q*)
$$q^*(s,a) = \mathbb{E}[R_{t+1} + \gamma \max_{a'} q^*(S_{t+1},a')|S_t=s,A_t=a]$$

Hoặc dạng đầy đủ:
$$q^*(s,a) = \sum_{s'} P(s'|s,a)[R(s,a,s') + \gamma \max_{a'} q^*(s',a')]$$

## 4. Giải Phương Trình Bellman Tối Ưu

### 4.1. Thách Thức
- Hệ phương trình phi tuyến do có phép lấy max
- Không thể giải bằng các phương pháp đại số tuyến tính thông thường
- Chính sách tối ưu π* ban đầu chưa biết

### 4.2. Phương Pháp Giải
- Sử dụng các kỹ thuật lặp
- Phương pháp giá trị (Value Iteration)
- Phương pháp chính sách (Policy Iteration)
- Học tăng cường (Reinforcement Learning)

## 5. Ví Dụ Minh Họa

### 5.1. Trò Chơi Đơn Giản
Giả sử một trò chơi với:
- 2 hành động có thể: a1, a2
- Phần thưởng ngay lập tức: R(s,a1) = 5, R(s,a2) = 3
- Giá trị trạng thái tiếp theo: v*(s') = 10
- Hệ số chiết khấu: γ = 0.9

Khi đó:
$$v^*(s) = \max[5 + 0.9 \times 10, 3 + 0.9 \times 10] = \max[14, 12] = 14$$

### 5.2. Ý Nghĩa
- Hành động a1 được chọn vì mang lại giá trị cao hơn
- Giá trị tối ưu của trạng thái s là 14
- Chính sách tối ưu sẽ chọn a1 trong trạng thái s

## 6. Kết Luận
Hàm giá trị tối ưu và phương trình Bellman tối ưu:
- Cung cấp cơ sở lý thuyết cho học tăng cường
- Cho phép tìm ra chính sách tốt nhất
- Hướng dẫn việc thiết kế các thuật toán học hiệu quả
