# Quá Trình Quyết Định Markov (Markov Decision Processes - MDPs)

## 1. Tổng Quan
Quá trình Quyết định Markov là một khuôn khổ toán học mở rộng từ Ra quyết định tuần tự, trong đó:
- Mỗi quyết định phụ thuộc vào trạng thái hiện tại của môi trường
- Tương lai chỉ phụ thuộc vào trạng thái hiện tại và hành động được chọn
- Không phụ thuộc vào lịch sử các trạng thái và hành động trước đó

## 2. Các Thành Phần Chính của MDPs

### 2.1. Trạng Thái (States)
- Mô tả tình huống hiện tại của môi trường
- Đại diện cho toàn bộ thông tin cần thiết để ra quyết định
- Ví dụ: Vị trí của thỏ trong môi trường, tình trạng sức khỏe của bệnh nhân

### 2.2. Hành Động (Actions)
- Các lựa chọn mà agent có thể thực hiện trong mỗi trạng thái
- Dẫn đến sự thay đổi trạng thái và nhận phần thưởng
- Ví dụ: Di chuyển trái/phải, chọn phương pháp điều trị

### 2.3. Phần Thưởng (Rewards)
- Giá trị số học thể hiện lợi ích của mỗi kết quả
- Có thể dương (phần thưởng) hoặc âm (hình phạt)
- Ví dụ: +10 cho việc tìm thấy cà rốt, -100 cho việc gặp hổ

### 2.4. Hàm Chuyển Trạng Thái (Transition Function)
- Xác suất chuyển từ trạng thái này sang trạng thái khác
- Phụ thuộc vào hành động được chọn
- Mô tả tính ngẫu nhiên của môi trường

## 3. Tính Chất Markov

### 3.1. Định Nghĩa
- Trạng thái và phần thưởng tương lai chỉ phụ thuộc vào:
  + Trạng thái hiện tại
  + Hành động được chọn
- Không phụ thuộc vào lịch sử các trạng thái và hành động trước đó

### 3.2. Ý Nghĩa
- Đơn giản hóa việc mô hình hóa và tính toán
- Cho phép tập trung vào trạng thái hiện tại
- Giảm độ phức tạp của bài toán

## 4. Ví Dụ Thực Tế: Thỏ và Cà Rốt

### 4.1. Các Trạng Thái
- Vị trí của thỏ trong môi trường
- Vị trí của thức ăn (cà rốt, bông cải)
- Vị trí của mối nguy hiểm (hổ)

### 4.2. Các Hành Động
- Di chuyển sang trái
- Di chuyển sang phải
- Đứng yên

### 4.3. Phần Thưởng
- +10: Tìm thấy cà rốt
- +3: Tìm thấy bông cải
- -100: Gặp hổ

## 5. Hàm Giá Trị và Chính Sách

### 5.1. Hàm Giá Trị Trạng Thái (State Value Function)
- Ước tính giá trị kỳ vọng của một trạng thái
- Dựa trên phần thưởng tương lai
- Công thức: 
$$V(s) = \mathbb{E}\left[\sum_{k=0}^{\infty} \gamma^k R_{t+k+1} \mid S_t = s\right]$$

Trong đó:
- $V(s)$: Giá trị của trạng thái s
- $\mathbb{E}$: Kỳ vọng toán học
- $\gamma$: Hệ số chiết khấu (0 ≤ γ ≤ 1)
- $R_{t+k+1}$: Phần thưởng tại bước thời gian t+k+1
- $S_t = s$: Điều kiện trạng thái hiện tại là s

### 5.2. Hàm Giá Trị Hành Động (Action Value Function)
- Ước tính giá trị kỳ vọng của một hành động trong trạng thái
- Công thức:
$$Q(s,a) = \mathbb{E}\left[\sum_{k=0}^{\infty} \gamma^k R_{t+k+1} \mid S_t = s, A_t = a\right]$$

Trong đó:
- $Q(s,a)$: Giá trị của hành động a trong trạng thái s
- $\mathbb{E}$: Kỳ vọng toán học
- $\gamma$: Hệ số chiết khấu
- $R_{t+k+1}$: Phần thưởng tại bước thời gian t+k+1
- $S_t = s, A_t = a$: Điều kiện trạng thái hiện tại là s và hành động là a

### 5.3. Chính Sách (Policy)
- Quy tắc chọn hành động trong mỗi trạng thái
- Mục tiêu: Tối đa hóa phần thưởng kỳ vọng
- Có thể là xác định hoặc ngẫu nhiên
- Công thức chính sách xác định:
$$\pi(s) = \arg\max_a Q(s,a)$$

Trong đó:
- $\pi(s)$: Hành động được chọn trong trạng thái s
- $\arg\max_a$: Tìm hành động a tối ưu
- $Q(s,a)$: Giá trị của hành động a trong trạng thái s

### 5.4. Phương Trình Bellman
- Mô tả mối quan hệ giữa giá trị của trạng thái hiện tại và các trạng thái tiếp theo
- Công thức:
$$V(s) = \sum_{a} \pi(a|s) \sum_{s'} P(s'|s,a) \left[R(s,a,s') + \gamma V(s')\right]$$

Trong đó:
- $V(s)$: Giá trị của trạng thái s
- $\pi(a|s)$: Xác suất chọn hành động a trong trạng thái s
- $P(s'|s,a)$: Xác suất chuyển từ trạng thái s sang s' khi thực hiện hành động a
- $R(s,a,s')$: Phần thưởng khi chuyển từ s sang s' bằng hành động a
- $\gamma$: Hệ số chiết khấu
- $V(s')$: Giá trị của trạng thái tiếp theo s'

## 6. Ứng Dụng

### 6.1. Học Tăng Cường (Reinforcement Learning)
- Agent học từ kinh nghiệm
- Cải thiện chính sách theo thời gian
- Tối ưu hóa quyết định dài hạn

### 6.2. Các Lĩnh Vực Ứng Dụng
- Điều khiển robot
- Trò chơi trí tuệ nhân tạo
- Lập kế hoạch tự động
- Tối ưu hóa hệ thống

## 7. Kết Luận
MDPs cung cấp một khuôn khổ mạnh mẽ để:
- Mô hình hóa các bài toán ra quyết định tuần tự
- Tối ưu hóa quyết định dài hạn
- Cân bằng giữa khám phá và khai thác
- Xử lý sự không chắc chắn trong môi trường

-------------------------------------------------------------------------------------------------------
##### 5-14-2025 at 7PM.
##### Course: Fundamentals of Reinforcement Learning/Module 3.
##### Đọc tài liệu tại: Markov Decision Processes
##### Học nội dung từ clip: Introduction to Markov Decision Processes
