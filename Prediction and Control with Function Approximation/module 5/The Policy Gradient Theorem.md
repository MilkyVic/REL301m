# Policy Gradient Theorem

## Giới thiệu
Policy Gradient Theorem là kết quả lý thuyết quan trọng, cho phép biểu diễn gradient của phần thưởng trung bình để dễ dàng ước lượng từ kinh nghiệm.

## Quy Trình Tối Ưu Hóa

### Các Bước
1. **Xác Định Mục Tiêu**
   - Tối đa hóa phần thưởng trung bình
   - Sử dụng gradient ascent
   - Điều chỉnh tham số θ

2. **Ước Lượng Gradient**
   - Áp dụng quy tắc tích
   - Tránh tính gradient của phân phối trạng thái
   - Sử dụng Policy Gradient Theorem

## Policy Gradient Theorem

### Biểu Thức
- Gradient = Σ μ(s) Σ ∇π(a|s) × Q(s,a)
- Không chứa gradient của μ(s)
- Dễ dàng ước lượng từ kinh nghiệm

### Thành Phần
1. **Gradient của Chính Sách**
   - Cho biết cách điều chỉnh tham số
   - Tăng xác suất chọn hành động
   - Phụ thuộc vào cách biểu diễn chính sách

2. **Hàm Giá Trị Hành Động**
   - Đánh giá chất lượng hành động
   - Trọng số cho gradient
   - Hướng dẫn điều chỉnh tham số

## Ví Dụ Minh Họa

### Grid World
1. **Tham Số Chính Sách**
   - Hai tham số điều khiển
   - Xác định xác suất hành động
   - Gradient khác nhau cho mỗi hành động

2. **Điều Chỉnh Tham Số**
   - Tăng xác suất hành động có giá trị dương
   - Giảm xác suất hành động có giá trị âm
   - Tối ưu hóa phần thưởng trung bình

## Ứng Dụng

### Actor-Critic Methods
1. **Actor**
   - Cập nhật chính sách
   - Sử dụng Policy Gradient Theorem
   - Điều chỉnh tham số

2. **Critic**
   - Ước lượng hàm giá trị
   - Cung cấp phản hồi
   - Hướng dẫn cập nhật

### Tối Ưu Hóa Robot
1. **Học Tập**
   - Thử và sai
   - Điều chỉnh hành động
   - Cải thiện hiệu suất

2. **Điều Chỉnh**
   - Dựa trên phần thưởng
   - Sử dụng gradient
   - Tối ưu hóa chính sách

## Kết Luận
- Policy Gradient Theorem cung cấp cách tính gradient đơn giản
- Cho phép tối ưu hóa chính sách trực tiếp
- Dễ dàng ước lượng từ kinh nghiệm
- Áp dụng được trong nhiều bài toán
- Cơ sở cho nhiều thuật toán học tăng cường
