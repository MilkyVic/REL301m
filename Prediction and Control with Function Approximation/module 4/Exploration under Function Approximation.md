# Khám Phá trong Function Approximation

## Giới thiệu
Cân bằng giữa khám phá và khai thác là đặc trưng quan trọng trong bài toán ra quyết định tuần tự. Trong function approximation, việc khám phá có những đặc điểm riêng cần được xem xét.

## Giá Trị Ban Đầu Lạc Quan (Optimistic Initial Values)

### Trong Môi Trường Bảng
1. **Nguyên Tắc**
   - Khởi tạo giá trị lớn hơn giá trị thực
   - Agent tin rằng có thể đạt phần thưởng cao hơn
   - Hệ thống khám phá không gian trạng thái-hành động

2. **Đặc Điểm**
   - Cập nhật độc lập cho mỗi cặp trạng thái-hành động
   - Ảnh hưởng giảm dần khi giá trị chính xác hơn

### Trong Function Approximation
1. **Khởi Tạo Trọng Số**
   - Đặt trọng số để tạo giá trị lạc quan
   - Đơn giản với đặc trưng nhị phân
   - Phức tạp với mạng nơ-ron

2. **Thách Thức**
   - Mối quan hệ phức tạp giữa đặc trưng và giá trị
   - Mạng nơ-ron có thể cho giá trị âm ngay cả với trọng số dương
   - Tổng quát hóa ảnh hưởng đến tính lạc quan

## Chiến Lược Epsilon Greedy

### Đặc Điểm
1. **Tính Phổ Dụng**
   - Áp dụng được với mọi function approximation
   - Chỉ cần ước lượng giá trị hành động
   - Không phụ thuộc vào cách khởi tạo

2. **Hạn Chế**
   - Không phải phương pháp khám phá có định hướng
   - Dựa vào ngẫu nhiên để tìm hành động tốt hơn
   - Ít có hệ thống hơn so với phương pháp dựa trên lạc quan

## Thách Thức trong Function Approximation

### Cập Nhật Có Tính Hệ Thống
1. **Vấn Đề**
   - Cập nhật phụ thuộc lẫn nhau giữa các trạng thái
   - Giá trị có thể giảm trước khi khám phá đầy đủ
   - Cần cập nhật cục bộ hơn

2. **Giải Pháp**
   - Tile coding: tạo cập nhật cục bộ
   - Mạng nơ-ron: có thể cập nhật cục bộ
   - Cần kiểm soát mức độ tổng quát hóa

### Tổng Quát Hóa
1. **Mạng Nơ-ron**
   - Có thể tổng quát hóa quá mạnh
   - Mất tính lạc quan nhanh chóng
   - Cần cân nhắc đặc biệt

2. **Tile Coding**
   - Cập nhật cục bộ tốt hơn
   - Duy trì tính lạc quan lâu hơn
   - Phù hợp cho khám phá có hệ thống

## Kết Luận
- Khám phá trong function approximation phức tạp hơn môi trường bảng
- Cần cân nhắc đặc điểm của function approximator
- Epsilon greedy là lựa chọn đơn giản và phổ dụng
- Cải thiện khám phá vẫn là vấn đề nghiên cứu mở
- Cần kết hợp nhiều chiến lược khác nhau
