# Tổng Quan Module 2: K-Armed Bandit Problem

## 1. K-Armed Bandit Problem
Bài toán K-Armed Bandit là một ví dụ cơ bản về việc ra quyết định trong điều kiện không chắc chắn. Agent phải chọn giữa K hành động khác nhau, mỗi hành động có phân phối phần thưởng riêng. Mục tiêu là tối đa hóa tổng phần thưởng nhận được theo thời gian.

## 2. Giá Trị Hành Động (Action Values)
- Mỗi hành động có một giá trị kỳ vọng
- Giá trị này được ước tính dựa trên phần thưởng trung bình nhận được
- Công thức: Q(a) = E[R|A=a]
- Giúp agent chọn hành động có giá trị cao nhất

## 3. Ra Quyết Định Tuần Tự (Sequential Decision Making)
- Agent thực hiện chuỗi quyết định theo thời gian
- Mỗi quyết định ảnh hưởng đến các quyết định tương lai
- Cần cân bằng giữa khám phá và khai thác
- Ví dụ: Bác sĩ thử nghiệm các phương pháp điều trị khác nhau

## 4. Upper-Confidence Bound (UCB)
- Phương pháp chọn hành động dựa trên giá trị ước tính và độ không chắc chắn
- Công thức: A_t = argmax_a [Q_t(a) + c * sqrt(ln(t)/N_t(a))]
- Trong đó:
  + Q_t(a): Giá trị ước tính của hành động a
  + N_t(a): Số lần hành động a được chọn
  + c: Tham số kiểm soát mức độ khám phá
  + t: Tổng số bước thời gian

## 5. Giá Trị Ban Đầu Lạc Quan (Optimistic Initial Values)
- Khởi tạo giá trị ước tính cao hơn giá trị thực tế
- Khuyến khích agent khám phá tất cả các hành động
- Giảm dần ảnh hưởng của giá trị ban đầu theo thời gian
- Hiệu quả trong môi trường tĩnh

## 6. Các Thách Thức
- Cân bằng giữa khám phá và khai thác
- Xử lý sự không chắc chắn
- Tối ưu hóa quyết định dựa trên dữ liệu hạn chế
- Thích nghi với môi trường thay đổi

## 7. Ứng Dụng Thực Tế
- Thử nghiệm y tế
- Quảng cáo trực tuyến
- Hệ thống đề xuất
- Tối ưu hóa website

-------------------------------------------------------------------------------------------------------
##### 5-17-2025 at 8PM.
##### Course: Fundamentals of Reinforcement Learning/Module 2.
##### Tổng hợp từ các tài liệu trong Module 2 