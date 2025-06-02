# Action Values trong K-Armed Bandit

## 1. Định nghĩa Action Values
Action Values (giá trị hành động) là giá trị kỳ vọng của phần thưởng khi thực hiện một hành động cụ thể. Trong ngữ cảnh của bài toán K-Armed Bandit, mỗi hành động (arm) có một giá trị thực (true value) được ký hiệu là $q_*(a)$.

### Công thức toán học:
$$q_*(a) = \mathbb{E}[R_t \mid A_t = a], \quad \forall a \in \{1, \ldots, k\}$$

Trong đó:
- $q_*(a)$: giá trị thực của hành động a
- $R_t$: phần thưởng tại thời điểm t
- $A_t$: hành động được chọn tại thời điểm t
- $a$: hành động bất kỳ trong tập k hành động

## 2. Phương pháp Sample-Average
Đây là phương pháp đơn giản nhất để ước tính giá trị của các hành động dựa trên dữ liệu quan sát được.

### Công thức tính:
$$
Q_t(a) = \frac{\text{Tổng phần thưởng nhận được khi chọn a trước t}}{\text{Số lần chọn a trước t}}
$$

### Ví dụ thực tế:
Giả sử một bác sĩ đang thử nghiệm 3 phương pháp điều trị khác nhau:

1. **Phương pháp A**:
   - Lần 1: Thành công (reward = 1)
   - Lần 2: Thành công (reward = 1)
   - Giá trị ước tính: $Q(A) = \frac{1 + 1}{2} = 1.0$

2. **Phương pháp B**:
   - Lần 1: Thành công (reward = 1)
   - Lần 2: Thất bại (reward = 0)
   - Giá trị ước tính: $Q(B) = \frac{1 + 0}{2} = 0.5$

3. **Phương pháp C**:
   - Lần 1: Thất bại (reward = 0)
   - Giá trị ước tính: $Q(C) = \frac{0}{1} = 0.0$

## 3. Ứng dụng trong Ra quyết định

### Greedy Action (Hành động tham lam)
- Chọn hành động có giá trị ước tính cao nhất
- Trong ví dụ trên: Chọn Phương pháp A vì có $Q(A) = 1.0$

### Exploration (Khám phá)
- Thử các hành động khác để thu thập thêm thông tin
- Quan trọng khi chưa có đủ dữ liệu về các hành động

## 4. Ưu và Nhược điểm

### Ưu điểm:
- Đơn giản, dễ hiểu và triển khai
- Ước tính ngày càng chính xác khi số lần thử tăng
- Phù hợp với các bài toán có phân phối phần thưởng tĩnh

### Nhược điểm:
- Không hiệu quả với phân phối phần thưởng thay đổi theo thời gian
- Cần lưu trữ toàn bộ lịch sử phần thưởng
- Có thể bị ảnh hưởng bởi nhiễu trong dữ liệu

## 5. Kết luận
Action Values là khái niệm cốt lõi trong bài toán K-Armed Bandit, giúp chúng ta:
- Đánh giá hiệu quả của các hành động
- Ra quyết định dựa trên dữ liệu
- Cân bằng giữa khám phá và khai thác
-------------------------------------------------------------------------------------------------------
  ##### 5-14-2025 at 3PM.
  ##### Course: Fundamentals of Reinforcement Learning/Module 2.
  ##### Đọc tài liệu tại: Action Values
  ##### Học nội dung từ clip: Learning Action Values 
