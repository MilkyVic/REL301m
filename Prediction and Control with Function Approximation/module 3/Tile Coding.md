# Tile Coding trong Học Tăng Cường

## Giới thiệu
Tile Coding là một phương pháp hiệu quả về mặt tính toán để thực hiện Coarse Coding, sử dụng các lưới chồng lấp để phân chia không gian trạng thái.

## Nguyên Lý Hoạt Động

### Phân Chia Không Gian
- Sử dụng các lưới vuông chồng lấp
- Mỗi lưới được gọi là một "tiling"
- Các lưới được đặt chồng lên nhau với độ lệch nhỏ

### Kích Thước Tile
- Tile lớn: tăng khả năng tổng quát hóa
- Tile nhỏ: tăng khả năng phân biệt
- Kích thước lý tưởng phụ thuộc vào bài toán cụ thể

## Cải Thiện Khả Năng Phân Biệt

### Nhiều Lớp Tiling
- Sử dụng nhiều lưới chồng lấp
- Mỗi lưới được lệch một khoảng nhỏ
- Tạo ra nhiều giao điểm nhỏ
- Cải thiện khả năng phân biệt

### Tổng Quát Hóa
- Một tiling: tổng quát hóa chỉ xảy ra trong hình vuông
- Nhiều tiling: tổng quát hóa theo đường chéo
- Độ lệch ngẫu nhiên: tổng quát hóa hình cầu và đồng nhất

## Kiểm Soát Tính Chất Tổng Quát Hóa

### Sử Dụng Hình Chữ Nhật
- Thay vì hình vuông, sử dụng hình chữ nhật
- Cho phép kiểm soát độ rộng tổng quát hóa theo từng chiều
- Có thể co giãn từng chiều của không gian trạng thái

### Co Giãn Chiều
- Co giãn các chiều của không gian trạng thái
- Đặt các hình vuông lên không gian đã co giãn
- Tương đương với việc đặt hình chữ nhật lên không gian gốc

## Hiệu Quả Tính Toán

### Ưu Điểm
1. **Tính Toán Đơn Giản**
   - Lưới đều đặn
   - Dễ xác định ô chứa trạng thái hiện tại

2. **Thí Nghiệm Sơ Bộ**
   - Phù hợp cho môi trường ít chiều
   - Cho phép chạy thử nghiệm nhanh

### Hạn Chế
1. **Tăng Số Chiều**
   - Số lượng tile tăng theo hàm mũ
   - Cần xử lý riêng từng chiều đầu vào

2. **Phụ Thuộc Bài Toán**
   - Khả năng xử lý độc lập các chiều phụ thuộc vào bài toán cụ thể
   - Cần cân nhắc kỹ khi thiết kế

## Ứng Dụng

### Biểu Diễn Hàm
- Có thể biểu diễn nhiều loại hàm khác nhau
- Linh hoạt trong việc điều chỉnh

### Môi Trường Liên Tục
- Hiệu quả cho không gian trạng thái liên tục
- Cân bằng giữa tổng quát hóa và phân biệt

## Kết luận
- Tile Coding là phương pháp hiệu quả cho Coarse Coding
- Cân bằng tốt giữa tổng quát hóa và phân biệt
- Hiệu quả về mặt tính toán
- Cần lưu ý về số chiều và thiết kế phù hợp
