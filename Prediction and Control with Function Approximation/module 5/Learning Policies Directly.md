# Học Chính Sách Trực Tiếp

## Giới thiệu
Thay vì ước lượng giá trị hành động, chúng ta có thể học chính sách trực tiếp thông qua các hàm có tham số. Đây là một cách tiếp cận mới, khác với Generalized Policy Iteration.

## Định Nghĩa Chính Sách Trực Tiếp

### Ví Dụ Mountain Car
- Chính sách đơn giản: tăng tốc theo hướng vận tốc hiện tại
- Không cần tính giá trị hành động
- Gần với chính sách tối ưu

### Biểu Diễn Chính Sách
- Sử dụng vector tham số θ
- Ký hiệu: π(s,θ)
- Đầu ra: xác suất chọn hành động

## Yêu Cầu cho Chính Sách Có Tham Số

### Điều Kiện
1. **Xác Suất Không Âm**
   - P(a|s) ≥ 0 với mọi a, s
   - Không thể dùng hàm tuyến tính trực tiếp

2. **Tổng Xác Suất Bằng 1**
   - Σ P(a|s) = 1 với mọi s
   - Cần chuẩn hóa đầu ra

## Softmax Policy

### Định Nghĩa
- Hàm ưu tiên hành động h(s,a,θ)
- Xác suất = e^h / Σ e^h
- Đảm bảo phân phối xác suất hợp lệ

### Tính Chất
1. **Hàm Mũ**
   - Đảm bảo xác suất dương
   - Chuẩn hóa tự động

2. **Ưu Tiên Hành Động**
   - Có thể là hàm tuyến tính của đặc trưng
   - Hoặc đầu ra của mạng nơ-ron
   - Chỉ quan trọng sự khác biệt tương đối

### Đặc Điểm
1. **Xác Suất Cao**
   - Khi ưu tiên lớn hơn nhiều
   - Tiến gần đến 1 nhưng không vượt quá

2. **Xác Suất Thấp**
   - Vẫn có xác suất khác 0
   - Ngay cả khi ưu tiên âm

3. **Xác Suất Tương Đồng**
   - Hành động có ưu tiên gần nhau
   - Được chọn với xác suất gần bằng nhau

## So Sánh với Epsilon-Greedy

### Epsilon-Greedy
1. **Ưu Điểm**
   - Hành động tốt nhất được chọn với xác suất cao
   - Các hành động khác có xác suất thấp

2. **Hạn Chế**
   - Hành động kém vẫn được chọn thường xuyên
   - Do bước khám phá epsilon

### Softmax
1. **Ưu Điểm**
   - Phân phối xác suất mềm dẻo hơn
   - Phản ánh mức độ ưu tiên tương đối

2. **Đặc Điểm**
   - Hành động kém có xác suất thấp hơn
   - Không cần tham số epsilon

## Kết Luận
- Chính sách có tham số cho phép học trực tiếp
- Softmax là cách hiệu quả để tạo phân phối xác suất
- Khác biệt với cách tiếp cận dựa trên giá trị
- Linh hoạt trong việc biểu diễn ưu tiên hành động
- Cung cấp cách tiếp cận mềm dẻo hơn so với epsilon-greedy
