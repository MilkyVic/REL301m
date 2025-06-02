# Ra Quyết Định Tuần Tự (Sequential Decision Making)

## 1. Tổng Quan
Ra quyết định tuần tự là quá trình trong đó một agent (tác nhân) thực hiện một chuỗi các quyết định theo thời gian, mỗi quyết định đều ảnh hưởng đến các quyết định và kết quả trong tương lai.

## 2. Tương Tác Giữa Agent và Môi Trường

### 2.1. Quá Trình Học
- Agent học thông qua việc tương tác với môi trường
- Phải hiểu được hậu quả của các hành động thông qua thử và sai
- Mỗi tương tác cung cấp thông tin mới để cải thiện quyết định

### 2.2. Ví Dụ Thử Nghiệm Y Tế
Giả sử một bác sĩ (agent) đang thử nghiệm 3 phương pháp điều trị:
- **Phương pháp Xanh**: Tỷ lệ thành công 70%
- **Phương pháp Đỏ**: Tỷ lệ thành công 50%
- **Phương pháp Vàng**: Tỷ lệ thành công 30%

## 3. Hàm Giá Trị Hành Động (Action Value Function)

### 3.1. Định Nghĩa
- Mỗi hành động có một giá trị kỳ vọng
- Giá trị này được tính dựa trên phần thưởng trung bình nhận được
- Công thức:
$$Q(a) = \mathbb{E}[R|A=a]$$

### 3.2. Ứng Dụng
- Hướng dẫn agent chọn hành động có giá trị cao nhất
- Giúp tối đa hóa phần thưởng kỳ vọng
- Cân bằng giữa khám phá và khai thác

## 4. Thách Thức Trong Ra Quyết Định

### 4.1. Sự Không Chắc Chắn
- Không biết trước kết quả của mỗi hành động
- Phải dựa vào dữ liệu quan sát được
- Cần thời gian để học và điều chỉnh

### 4.2. Cân Bằng Giữa Khám Phá và Khai Thác
- **Khai thác**: Sử dụng phương pháp điều trị hiệu quả nhất đã biết
- **Khám phá**: Thử các phương pháp khác để thu thập thêm thông tin
- Cần chiến lược để cân bằng hai yếu tố này

## 5. Ví Dụ Thực Tế

### 5.1. Quy Trình Thử Nghiệm
1. Bác sĩ chọn ngẫu nhiên một phương pháp điều trị
2. Quan sát kết quả trên bệnh nhân
3. Cập nhật giá trị ước tính của phương pháp
4. Lặp lại quá trình với bệnh nhân tiếp theo

### 5.2. Ra Quyết Định
- Dựa trên dữ liệu đã thu thập
- Cân nhắc giữa:
  + Sử dụng phương pháp tốt nhất hiện tại
  + Thử phương pháp mới để có thêm thông tin

## 6. Kết Luận
Ra quyết định tuần tự là một quá trình phức tạp đòi hỏi:
- Khả năng học từ kinh nghiệm
- Cân bằng giữa các mục tiêu ngắn hạn và dài hạn
- Xử lý hiệu quả sự không chắc chắn
- Tối ưu hóa quyết định dựa trên dữ liệu

-------------------------------------------------------------------------------------------------------
  ##### 5-14-2025 at 7PM.
  ##### Course: Fundamentals of Reinforcement Learning/Module 2.
  ##### Đọc tài liệu tại: Sequential Decision Making
  ##### Học nội dung từ clip: Sequential Decision Making with Evaluative Feedback
