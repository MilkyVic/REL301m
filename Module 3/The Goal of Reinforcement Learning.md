# Mục Tiêu Của Học Tăng Cường (The Goal of Reinforcement Learning)

## 1. Mục Tiêu Chính
Mục tiêu cốt lõi của một agent trong học tăng cường là tối đa hóa tổng phần thưởng tương lai. Điều này bao gồm:

### 1.1. Đánh Giá Hành Động
- Agent phải đánh giá hậu quả dài hạn của các hành động
- Không chỉ tập trung vào phần thưởng ngay lập tức
- Cân nhắc tác động của mỗi quyết định đến tương lai

### 1.2. Phần Thưởng Kỳ Vọng
- Agent hướng đến tối đa hóa phần thưởng kỳ vọng
- Tổng hợp các phần thưởng có thể đạt được theo thời gian
- Đảm bảo quyết định tốt nhất cho tương lai

## 2. Hậu Quả Của Quyết Định Ngắn Hạn

### 2.1. Quyết Định Thiển Cận
- Chỉ tập trung vào phần thưởng ngay lập tức
- Bỏ qua hậu quả dài hạn
- Dẫn đến hiệu suất không tối ưu

### 2.2. Ví Dụ Thực Tế
- **Robot Học Đi Bộ**:
  + Hành động ngắn hạn: Lao về phía trước để đạt khoảng cách ngay lập tức
  + Hậu quả: Có thể ngã và thất bại trong việc học đi bộ
  + Giải pháp tốt hơn: Tập trung vào chuyển động tổng thể, học cách đi bộ cẩn thận và hiệu quả

- **Trò Chơi Cờ Vua**:
  + Hành động ngắn hạn: Ăn quân đối phương ngay lập tức
  + Hậu quả: Có thể dẫn đến thế cờ yếu hơn
  + Giải pháp tốt hơn: Lập kế hoạch chiến lược dài hạn

## 3. Hậu Quả Dài Hạn Của Quyết Định Thiển Cận

### 3.1. Thất Bại Trong Việc Đạt Mục Tiêu
- Không đạt được mục tiêu dự kiến
- Hành động ngay lập tức có thể phản tác dụng
- Mất cơ hội đạt được kết quả tốt hơn

### 3.2. Tăng Rủi Ro Thất Bại
- Gặp phải trở ngại có thể tránh được
- Tạo ra tình huống khó khăn không cần thiết
- Giảm khả năng thành công

### 3.3. Học Tập Không Hiệu Quả
- Không phát triển kỹ năng cần thiết
- Không xây dựng được chiến lược phù hợp
- Trì trệ trong quá trình học

### 3.4. Phân Bổ Nguồn Lực Không Hiệu Quả
- Lãng phí thời gian và tài nguyên
- Tập trung vào hành động không đóng góp cho thành công
- Giảm hiệu suất tổng thể

### 3.5. Vòng Lặp Phản Hồi Tiêu Cực
- Tiếp tục đưa ra quyết định không tối ưu
- Dựa trên lợi ích ngắn hạn trước đó
- Khó thoát khỏi chu kỳ thất bại

## 4. Kết Luận
Học tăng cường đòi hỏi agent phải:
- Cân nhắc hậu quả dài hạn của mỗi hành động
- Tối ưu hóa tổng phần thưởng theo thời gian
- Tránh các quyết định thiển cận
- Phát triển chiến lược hiệu quả cho tương lai

## 5. Công Thức Return

### 5.1. Định Nghĩa Return
Return tại bước thời gian t, ký hiệu là $G_t$, được định nghĩa là tổng các phần thưởng nhận được sau bước thời gian t:

$$G_t = R_{t+1} + R_{t+2} + R_{t+3} + \ldots + R_T$$

Trong đó:
- $G_t$: Return tại bước thời gian t
- $R_{t+1}, R_{t+2}, \ldots, R_T$: Các phần thưởng nhận được tại các bước thời gian tiếp theo
- $T$: Bước thời gian kết thúc (terminal time step)

### 5.2. Ý Nghĩa
- Return đại diện cho tổng phần thưởng mà agent có thể nhận được từ thời điểm hiện tại
- Giúp đánh giá hiệu suất của agent trong dài hạn
- Là cơ sở để agent học cách tối ưu hóa hành động

### 5.3. Ví Dụ
Giả sử một agent đang chơi game:
- $R_{t+1} = 10$ (ăn được quả táo)
- $R_{t+2} = 5$ (nhận được điểm thưởng)
- $R_{t+3} = -2$ (bị mất máu)
- $R_T = 20$ (hoàn thành level)

Khi đó:
$$G_t = 10 + 5 + (-2) + 20 = 33$$

### 5.4. Tầm Quan Trọng
- Return giúp agent đánh giá giá trị của mỗi trạng thái
- Là cơ sở để học chính sách tối ưu
- Cho phép cân nhắc giữa phần thưởng ngắn hạn và dài hạn

-------------------------------------------------------------------------------------------------------
##### 5-15-2025 at 3PM.
##### Course: Fundamentals of Reinforcement Learning/Module 3.
##### Đọc tài liệu tại: The Goal of Reinforcement Learning
##### Học nội dung từ clip: The Goal of Reinforcement Learning
