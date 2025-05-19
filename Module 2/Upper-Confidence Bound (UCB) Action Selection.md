# Upper-Confidence Bound (UCB) Action Selection

## 1. Tổng Quan
Upper-Confidence Bound (UCB) là một phương pháp lựa chọn hành động trong học tăng cường, cải tiến từ phương pháp Epsilon-greedy bằng cách sử dụng khoảng tin cậy để cân bằng giữa khám phá và khai thác một cách thông minh hơn.

## 2. Công Thức UCB

### 2.1. Công Thức Cơ Bản
$$\text{Action} = \hat{Q}(A) + c \cdot \sqrt{\frac{\ln(n)}{n_A}}$$

Trong đó:
- $\hat{Q}(A)$: giá trị ước tính của hành động A
- $c$: tham số điều khiển mức độ khám phá
- $n$: tổng số lần thực hiện hành động
- $n_A$: số lần hành động A được chọn

### 2.2. Thành Phần Công Thức
1. **Giá trị ước tính** ($\hat{Q}(A)$):
   - Phản ánh hiệu quả hiện tại của hành động
   - Dựa trên kinh nghiệm đã có

2. **Hệ số khám phá** ($c \cdot \sqrt{\frac{\ln(n)}{n_A}}$):
   - Tăng khi hành động ít được chọn
   - Giảm khi hành động được chọn nhiều lần
   - Khuyến khích khám phá các hành động chưa được thử nhiều

## 3. So Sánh với Epsilon-greedy

### 3.1. Ưu Điểm của UCB
- **Khám phá thông minh hơn**:
  - Dựa trên độ không chắc chắn của ước tính
  - Tự động điều chỉnh mức độ khám phá
  - Không cần tham số epsilon cố định

- **Hiệu suất tốt hơn**:
  - Tập trung vào các hành động có tiềm năng
  - Giảm dần khám phá theo thời gian
  - Thích ứng với môi trường thay đổi

### 3.2. Hạn Chế
- **Phức tạp hơn**:
  - Cần tính toán khoảng tin cậy
  - Điều chỉnh tham số c
  - Theo dõi số lần thực hiện mỗi hành động

## 4. Ví Dụ Thực Tế

### 4.1. Thử Nghiệm Y Tế
Giả sử có 3 phương pháp điều trị:
- **Phương pháp A**: 100 lần thử, hiệu quả cao
- **Phương pháp B**: 10 lần thử, hiệu quả trung bình
- **Phương pháp C**: 5 lần thử, hiệu quả thấp

UCB có thể chọn Phương pháp B hoặc C để khám phá thêm, ngay cả khi giá trị ước tính hiện tại thấp hơn.

### 4.2. Quá Trình Ra Quyết Định
1. **Giai đoạn đầu**:
   - Khám phá nhiều hành động khác nhau
   - Thu thập dữ liệu về hiệu quả

2. **Giai đoạn sau**:
   - Tập trung vào hành động tốt nhất
   - Vẫn duy trì khám phá có chọn lọc

## 5. Ứng Dụng

### 5.1. Trong Y Tế
- Thử nghiệm lâm sàng
- Tối ưu hóa phác đồ điều trị
- Đánh giá hiệu quả thuốc

### 5.2. Trong Công Nghệ
- Tối ưu hóa quảng cáo
- Hệ thống đề xuất
- Tự động hóa quyết định

## 6. Kết Luận
UCB là một phương pháp hiệu quả để:
- Cân bằng khám phá và khai thác
- Tối ưu hóa quyết định dựa trên dữ liệu
- Thích ứng với môi trường thay đổi

Tuy nhiên, cần lưu ý việc điều chỉnh tham số và theo dõi hiệu suất để đạt kết quả tốt nhất.

-------------------------------------------------------------------------------------------------------
  ##### 5-15-2025 at 9PM.
  ##### Course: Fundamentals of Reinforcement Learning/Module 2.
  ##### Đọc tài liệu tại: Upper-Confidence Bound (UCB) Action Selection
  ##### Học nội dung từ clip: UCB Action Selection
