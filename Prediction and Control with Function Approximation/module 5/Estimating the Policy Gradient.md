# Ước Lượng Policy Gradient

## Giới thiệu
Sau khi có Policy Gradient Theorem, chúng ta cần ước lượng gradient từ kinh nghiệm của agent tương tác với môi trường.

## Quy Trình Ước Lượng

### Gradient Descent
1. **Mục Tiêu**
   - Tối ưu hóa chính sách
   - Sử dụng gradient descent
   - Cập nhật tham số θ

2. **Ước Lượng Gradient**
   - Lấy mẫu từ trạng thái quan sát được
   - Sử dụng chính sách π
   - Đảm bảo hội tụ đến điểm dừng

## Biểu Thức Gradient

### Dạng Ban Đầu
- Gradient = Σ μ(s) Σ ∇π(a|s) × Q(s,a)
- Khó tính toán trực tiếp
- Cần ước lượng từ mẫu

### Chuyển Đổi
1. **Kỳ Vọng Theo Trạng Thái**
   - Viết lại dưới dạng kỳ vọng
   - Sử dụng phân phối μ
   - Lấy mẫu từ trạng thái quan sát

2. **Kỳ Vọng Theo Hành Động**
   - Nhân và chia cho π(a|s)
   - Chuyển thành kỳ vọng theo π
   - Lấy mẫu từ hành động thực hiện

## Cập Nhật Tham Số

### Công Thức
- θ = θ + α × ∇logπ(a|s) × Q(s,a)
- α: tốc độ học
- ∇logπ: gradient của log chính sách

### Lý Do Sử Dụng Log
1. **Đơn Giản Hóa**
   - Dễ tính gradient
   - Viết gọn hơn
   - Tương đương về mặt toán học

2. **Tính Chất**
   - ∇π = π × ∇logπ
   - Không thay đổi thuật toán
   - Chỉ là kỹ thuật toán học

## Tính Toán Gradient

### Thành Phần
1. **Gradient của Chính Sách**
   - Phụ thuộc vào cách biểu diễn
   - Có thể tính trực tiếp
   - Đơn giản với softmax

2. **Giá Trị Hành Động**
   - Có thể ước lượng bằng TD
   - Sử dụng differential values
   - Nhiều cách ước lượng khác nhau

## Kết Luận
- Có thể ước lượng gradient từ kinh nghiệm
- Sử dụng mẫu ngẫu nhiên
- Cập nhật tham số theo hướng gradient
- Cần ước lượng giá trị hành động
- Áp dụng được trong nhiều bài toán
