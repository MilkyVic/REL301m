# Nhiệm Vụ Liên Tục (Continuing Tasks)

## 1. Tổng Quan
Nhiệm vụ liên tục là những nhiệm vụ không có trạng thái kết thúc, trong đó agent và môi trường tương tác liên tục. Khác với nhiệm vụ theo tập (episodic tasks), nhiệm vụ liên tục không có điểm dừng rõ ràng.

## 2. So Sánh Với Nhiệm Vụ Theo Tập

### 2.1. Nhiệm Vụ Theo Tập (Episodic Tasks)
- Có trạng thái kết thúc rõ ràng
- Mỗi tập bắt đầu độc lập
- Ví dụ: Chơi game, mỗi ván game kết thúc khi thắng hoặc thua

### 2.2. Nhiệm Vụ Liên Tục (Continuing Tasks)
- Không có trạng thái kết thúc
- Tương tác liên tục với môi trường
- Ví dụ: Điều khiển nhiệt độ phòng, giao dịch chứng khoán

## 3. Chiết Khấu Phần Thưởng Tương Lai

### 3.1. Công Thức Return
Return tại bước thời gian t được tính bằng:

$$G_t = R_t + \gamma R_{t+1} + \gamma^2 R_{t+2} + \ldots$$

Trong đó:
- $G_t$: Return tại bước thời gian t
- $R_t$: Phần thưởng tại bước thời gian t
- $\gamma$: Hệ số chiết khấu (0 ≤ γ ≤ 1)

### 3.2. Giới Hạn Return
Nếu $R_{max}$ là phần thưởng tối đa, return có thể được giới hạn:

$$G_t \leq R_{max} \left( \frac{1}{1 - \gamma} \right)$$

### 3.3. Công Thức Return Đệ Quy
Return có thể được biểu diễn dưới dạng đệ quy:

$$G_t = R_t + \gamma G_{t+1}$$

## 4. Ví Dụ Thực Tế: Bộ Điều Nhiệt Thông Minh

### 4.1. Trạng Thái
- Nhiệt độ hiện tại
- Thời gian trong ngày
- Thời tiết bên ngoài
- Số người trong phòng

### 4.2. Hành Động
- Bật/tắt máy sưởi
- Điều chỉnh nhiệt độ
- Duy trì nhiệt độ hiện tại

### 4.3. Phần Thưởng
- Dương: Nhiệt độ trong phạm vi mong muốn
- Âm: Điều chỉnh thủ công, tiêu tốn năng lượng

## 5. Ý Nghĩa Của Hệ Số Chiết Khấu (γ)

### 5.1. γ = 0
- Agent chỉ quan tâm đến phần thưởng ngay lập tức
- Bỏ qua hậu quả dài hạn
- Hành động thiển cận

### 5.2. γ ≈ 1
- Agent coi trọng cả phần thưởng ngắn hạn và dài hạn
- Cân nhắc hậu quả tương lai
- Hành động có tầm nhìn xa

### 5.3. 0 < γ < 1
- Cân bằng giữa phần thưởng ngắn hạn và dài hạn
- Phần thưởng càng xa càng giảm giá trị
- Hành động cân bằng

## 6. Kết Luận
Nhiệm vụ liên tục đòi hỏi:
- Xử lý phần thưởng vô hạn
- Chiết khấu phù hợp
- Cân nhắc cả ngắn hạn và dài hạn
- Tối ưu hóa hành động liên tục

-------------------------------------------------------------------------------------------------------
##### 5-17-2025 at 8PM.
##### Course: Fundamentals of Reinforcement Learning/Module 3.
##### Đọc tài liệu tại: Continuing Tasks
##### Học nội dung từ clip: Continuing Tasks 
