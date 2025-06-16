# Episodic Sarsa với Function Approximation

## Giới thiệu
Episodic Sarsa là một thuật toán GPI (Generalized Policy Iteration) sử dụng function approximation để ước lượng giá trị hành động trong các bài toán điều khiển.

## Biểu Diễn Đặc Trưng Phụ Thuộc Hành Động

### Cấu Trúc Cơ Bản
- Vector trọng số
- Vector đặc trưng
- Ước lượng giá trị = tích vô hướng của hai vector

### Stacking Features
1. **Nguyên Tắc**
   - Sử dụng cùng đặc trưng trạng thái cho mỗi hành động
   - Chỉ kích hoạt đặc trưng tương ứng với hành động được chọn
   - Lặp lại đặc trưng cho mỗi hành động

2. **Ví Dụ**
   - 4 đặc trưng, 3 hành động
   - Vector đặc trưng có 12 thành phần
   - Mỗi đoạn 4 đặc trưng tương ứng một hành động

## Tính Toán Giá Trị Hành Động

### Quy Trình
1. **Vector Trọng Số**
   - Chia thành các đoạn tương ứng với mỗi hành động
   - Mỗi đoạn chứa trọng số cho một hành động

2. **Vector Đặc Trưng**
   - Đặt 0 cho đặc trưng của các hành động không được chọn
   - Giữ nguyên đặc trưng của hành động được chọn

3. **Tính Giá Trị**
   - Lấy tích vô hướng giữa đoạn trọng số và đặc trưng tương ứng
   - Kết quả là giá trị hành động cho trạng thái hiện tại

## Mạng Nơ-ron và Tile Coding

### Mạng Nơ-ron
- Đầu vào: trạng thái
- Tầng ẩn: tạo đặc trưng trạng thái
- Đầu ra: nhiều giá trị, mỗi giá trị cho một hành động
- Tương đương với stacking features

### Tile Coding
- Đầu vào: cả trạng thái và hành động
- Đầu ra: một giá trị cho cặp trạng thái-hành động
- Cho phép tổng quát hóa qua hành động

## Thuật Toán Sarsa với Function Approximation

### Khác Biệt với Sarsa Thông Thường
1. **Ước Lượng Giá Trị**
   - Sử dụng hàm giá trị hành động có tham số
   - Thay vì bảng Q-values

2. **Cập Nhật**
   - Sử dụng gradient để cập nhật trọng số
   - Tương tự như semi-gradient TD

### Các Bước Thực Hiện
1. **Khởi Tạo**
   - Khởi tạo vector trọng số
   - Chọn chiến lược khám phá (ví dụ: epsilon-greedy)

2. **Vòng Lặp Episode**
   - Chọn hành động dựa trên chính sách hiện tại
   - Thực hiện hành động, nhận phần thưởng và trạng thái mới
   - Cập nhật trọng số sử dụng gradient

## Kết Luận
- Episodic Sarsa với function approximation cho phép học trong không gian trạng thái lớn
- Stacking features là cách hiệu quả để biểu diễn giá trị hành động
- Có thể áp dụng với nhiều loại function approximator khác nhau
- Duy trì được tính chất on-policy của Sarsa
