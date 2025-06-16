# Xấp Xỉ Phi Tuyến với Mạng Nơ-ron

## Giới thiệu
Mạng nơ-ron cung cấp một chiến lược để học tập các đặc trưng hữu ích, khác với các phương pháp có bộ đặc trưng cố định như tile coding.

## Cấu Trúc Mạng Nơ-ron

### Khởi Tạo
- Cần xác định trọng số ban đầu
- Thường được khởi tạo ngẫu nhiên
- Cách khởi tạo ảnh hưởng đến quá trình học

### Xử Lý Đầu Vào
- Mỗi đầu vào được nhân với trọng số tương ứng
- Tổng có trọng số được đưa qua hàm kích hoạt phi tuyến
- Kết quả là một hàm phi tuyến của đầu vào

## Tạo Đặc Trưng

### Quá Trình
1. **Tầng Ẩn**
   - Mỗi nơ-ron có bộ trọng số riêng
   - Tạo ra các đặc trưng khác nhau
   - Tập hợp các đặc trưng tạo thành biểu diễn mới

2. **Hàm Kích Hoạt**
   - Tạo tính phi tuyến
   - Cho phép học các mối quan hệ phức tạp
   - Ví dụ: sigmoid, ReLU, tanh

## So Sánh với Tile Coding

### Điểm Tương Đồng
1. **Tham Số Cố Định**
   - Tile coding: kích thước và số lượng tile
   - Mạng nơ-ron: số tầng, số nơ-ron, hàm kích hoạt

2. **Tạo Biểu Diễn**
   - Đều tạo ánh xạ phi tuyến từ đầu vào
   - Đều sử dụng tổ hợp tuyến tính để tạo đầu ra

### Điểm Khác Biệt
1. **Khả Năng Học**
   - Mạng nơ-ron: có thể điều chỉnh đặc trưng trong quá trình học
   - Tile coding: đặc trưng cố định

2. **Biên Giới**
   - Mạng nơ-ron: biên giới mềm, thay đổi mượt mà
   - Tile coding: biên giới cứng

## Biểu Diễn Trực Quan

### Vùng Tiếp Nhận
- Hiển thị cách đặc trưng tổng quát hóa
- Màu tối hơn: kích hoạt mạnh hơn
- Màu trắng: không kích hoạt

### Ví Dụ Thực Tế
- Môi trường 2D với hành lang hẹp
- Đặc trưng học được phản ánh vị trí tường
- Tổng quát hóa khác nhau cho các trạng thái khác nhau

## Ưu Điểm

1. **Linh Hoạt**
   - Có thể học các mối quan hệ phức tạp
   - Tự động điều chỉnh đặc trưng

2. **Tổng Quát Hóa**
   - Biên giới mềm
   - Thích ứng với dữ liệu mới

3. **Khả Năng Học**
   - Cải thiện đặc trưng trong quá trình học
   - Tận dụng thông tin từ dữ liệu

## Hạn Chế

1. **Độ Phức Tạp**
   - Cần nhiều dữ liệu để học
   - Có thể bị overfitting

2. **Tính Toán**
   - Yêu cầu tài nguyên tính toán lớn
   - Cần tối ưu hóa siêu tham số

## Kết luận
- Mạng nơ-ron cung cấp cách tiếp cận linh hoạt cho xấp xỉ phi tuyến
- Cho phép học và điều chỉnh đặc trưng
- Tạo ra biểu diễn phong phú và thích ứng
- Cần cân nhắc kỹ về thiết kế và huấn luyện
