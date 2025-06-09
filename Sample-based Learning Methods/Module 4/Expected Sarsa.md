# Expected Sarsa

## 1. Tổng Quan
Expected Sarsa là một phương pháp điều khiển dựa trên sự khác biệt thời gian (TD control) trong học tăng cường. Khác với Sarsa thông thường, Expected Sarsa tính toán trực tiếp kỳ vọng của các giá trị hành động thay vì lấy mẫu hành động tiếp theo từ chính sách.

## 2. Cơ Chế Học

### 2.1. Cập Nhật Giá Trị
Công thức cập nhật của Expected Sarsa:

$$Q(s_t, a_t) \leftarrow Q(s_t, a_t) + \alpha \left[ R_{t+1} + \gamma \sum_a \pi(a|s_{t+1})Q(s_{t+1}, a) - Q(s_t, a_t) \right]$$

Trong đó:
- $\alpha$: Tốc độ học
- $\gamma$: Hệ số chiết khấu
- $\pi(a|s_{t+1})$: Xác suất chọn hành động $a$ trong trạng thái $s_{t+1}$ theo chính sách hiện tại
- $\sum_a \pi(a|s_{t+1})Q(s_{t+1}, a)$: Kỳ vọng của giá trị hành động tiếp theo

### 2.2. So Sánh Với Sarsa Thông Thường
- Sarsa: Sử dụng giá trị của một hành động được lấy mẫu ngẫu nhiên
- Expected Sarsa: Sử dụng trung bình có trọng số của tất cả các hành động có thể
- Expected Sarsa cho kết quả ổn định hơn do giảm phương sai trong quá trình học

## 3. Ưu Điểm và Hạn Chế

### 3.1. Ưu Điểm
- Giảm phương sai trong mục tiêu cập nhật
- Ước tính giá trị chính xác hơn
- Hội tụ tốt hơn trong nhiều trường hợp
- Ít nhạy cảm với nhiễu trong dữ liệu

### 3.2. Hạn Chế
- Chi phí tính toán cao hơn
- Yêu cầu tính toán trung bình cho tất cả các hành động có thể
- Có thể không hiệu quả khi số lượng hành động lớn
- Cần lưu trữ thêm thông tin về xác suất chính sách

## 4. Ứng Dụng Thực Tế

### 4.1. Trong Môi Trường Có Nhiễu
- Phù hợp với các môi trường có nhiều biến động
- Giảm ảnh hưởng của nhiễu trong quá trình học
- Cho kết quả ổn định hơn

### 4.2. Trong Các Bài Toán Phức Tạp
- Hiệu quả trong các bài toán có không gian hành động lớn
- Cải thiện chất lượng học trong các tình huống phức tạp
- Tăng độ tin cậy của các quyết định

## 5. Cài Đặt và Tối Ưu Hóa

### 5.1. Cài Đặt Cơ Bản
- Sử dụng epsilon-greedy cho chính sách
- Tính toán kỳ vọng cho mỗi bước cập nhật
- Lưu trữ và cập nhật xác suất chính sách

### 5.2. Tối Ưu Hóa Hiệu Suất
- Sử dụng các kỹ thuật tính toán song song
- Tối ưu hóa việc tính toán kỳ vọng
- Cân nhắc giữa độ chính xác và tốc độ

## 6. Kết Luận
Expected Sarsa là một cải tiến quan trọng của thuật toán Sarsa, mang lại sự ổn định và độ chính xác cao hơn trong quá trình học. Mặc dù có chi phí tính toán cao hơn, nhưng những lợi ích về mặt hiệu suất và độ tin cậy làm cho nó trở thành một lựa chọn tốt cho nhiều ứng dụng thực tế.
