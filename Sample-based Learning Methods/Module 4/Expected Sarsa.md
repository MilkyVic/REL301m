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

# Đánh giá về Expected Sarsa và Q-learning với Function Approximation

Nội dung này tập trung vào khái niệm Expected Sarsa với function approximation trong học tăng cường, cũng như mối liên hệ với Q-learning.

## Expected Sarsa với Function Approximation

- Expected Sarsa với function approximation cập nhật trọng số (weight vector) dựa trên kỳ vọng giá trị hành động ở trạng thái tiếp theo, thay vì chỉ sử dụng giá trị của một hành động được chọn ngẫu nhiên.
- Kỳ vọng này được tính bằng tổng các giá trị hành động, mỗi giá trị được nhân với xác suất chọn hành động đó theo chính sách mục tiêu (target policy).

**Phương trình cập nhật:**
$$
W \leftarrow W + \alpha \left( R + \gamma \sum_{a} \pi(a|s') Q(s', a; W) - Q(s, a; W) \right)
$$

Trong đó:
- $W$: vector trọng số cho function approximation.
- $\alpha$: tốc độ học.
- $R$: phần thưởng nhận được.
- $\gamma$: hệ số chiết khấu.
- $s'$: trạng thái tiếp theo.
- $\pi(a|s')$: xác suất chọn hành động $a$ ở trạng thái $s'$ theo chính sách mục tiêu.
- $Q(s', a; W)$: giá trị hành động ước lượng ở trạng thái $s'$, hành động $a$ với trọng số $W$.

## Q-learning với Function Approximation

- Q-learning là một trường hợp đặc biệt của Expected Sarsa, trong đó chính sách mục tiêu là greedy (tham lam) với các giá trị hành động xấp xỉ.
- Phương trình cập nhật của Q-learning sử dụng giá trị hành động lớn nhất ở trạng thái tiếp theo thay vì kỳ vọng:

$$
W \leftarrow W + \alpha \left( R + \gamma \max_{a} Q(s', a; W) - Q(s, a; W) \right)
$$

## Chuyển tiếp từ Sarsa sang Expected Sarsa

- Cập nhật của Sarsa với function approximation tương tự như trường hợp bảng (tabular), sử dụng hệ số trọng số và gradient.
- Expected Sarsa cũng theo cấu trúc này, nhưng tính giá trị hành động từ vector trọng số cho mọi hành động ở trạng thái tiếp theo.

## Kết luận

- Expected Sarsa và Q-learning với function approximation đều mở rộng khả năng áp dụng của các thuật toán TD control sang các không gian trạng thái lớn hoặc liên tục.
- Sự khác biệt chính nằm ở cách tính mục tiêu cập nhật: Expected Sarsa dùng kỳ vọng theo chính sách, còn Q-learning dùng giá trị lớn nhất.
