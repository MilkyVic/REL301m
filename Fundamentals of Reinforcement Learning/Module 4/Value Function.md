# Hàm Giá Trị (Value Function)

## 1. Định Nghĩa Hàm Giá Trị
Hàm giá trị là một công cụ quan trọng trong học tăng cường, giúp agent đánh giá và dự đoán giá trị của các trạng thái và hành động. Có hai loại hàm giá trị chính:

### 1.1. Hàm Giá Trị Trạng Thái (State Value Function)
- Đại diện cho phần thưởng kỳ vọng từ một trạng thái cụ thể
- Cho biết agent có thể mong đợi nhận được bao nhiêu phần thưởng trong tương lai
- Ký hiệu: V(s) - giá trị của trạng thái s

### 1.2. Hàm Giá Trị Hành Động (Action Value Function)
- Mô tả phần thưởng kỳ vọng sau khi thực hiện một hành động cụ thể
- Giúp đánh giá chất lượng của các hành động khác nhau
- Ký hiệu: Q(s,a) - giá trị của hành động a trong trạng thái s

## 2. Tầm Quan Trọng Của Hàm Giá Trị

### 2.1. Đánh Giá Tình Huống
- Cho phép agent đánh giá tình huống hiện tại mà không cần đợi kết quả dài hạn
- Đặc biệt quan trọng trong môi trường có phần thưởng trễ
- Giúp đưa ra quyết định nhanh chóng và hiệu quả

### 2.2. Tổng Hợp Phần Thưởng
- Tóm tắt tất cả các phần thưởng tương lai có thể có
- Tính trung bình trên các return
- Cho phép đánh giá chất lượng của các chính sách khác nhau

## 3. Ví Dụ Trong Bối Cảnh Trò Chơi

### 3.1. Trò Chơi Cờ Vua
- **Hàm Giá Trị Trạng Thái**:
  + Phản ánh xác suất thắng dựa trên vị trí bàn cờ hiện tại
  + Giúp đánh giá lợi thế của mỗi bên
  + Hướng dẫn chiến lược tổng thể

- **Hàm Giá Trị Hành Động**:
  + Đánh giá xác suất thắng cho mỗi nước đi có thể
  + Giúp chọn nước đi tốt nhất
  + Cân nhắc hậu quả ngắn hạn và dài hạn

### 3.2. Ứng Dụng Thực Tế
- Cung cấp thông tin chi tiết về hiệu suất của agent
- Cho phép đánh giá liên tục trong quá trình chơi
- Không chỉ dựa vào kết quả cuối cùng

## 4. Công Thức Toán Học

### 4.1. Hàm Giá Trị Trạng Thái
$$V^\pi(s) = \mathbb{E}_\pi[G_t|S_t=s]$$

Trong đó:
- $V^\pi(s)$: Giá trị của trạng thái s theo chính sách π
- $\mathbb{E}_\pi$: Kỳ vọng theo chính sách π
- $G_t$: Return tại thời điểm t
- $S_t$: Trạng thái tại thời điểm t

### 4.2. Hàm Giá Trị Hành Động
$$Q^\pi(s,a) = \mathbb{E}_\pi[G_t|S_t=s, A_t=a]$$

Trong đó:
- $Q^\pi(s,a)$: Giá trị của hành động a trong trạng thái s theo chính sách π
- $A_t$: Hành động tại thời điểm t

## 5. Kết Luận
Hàm giá trị là công cụ không thể thiếu trong học tăng cường, giúp:
- Đánh giá hiệu quả các trạng thái và hành động
- Hướng dẫn quá trình ra quyết định
- Tối ưu hóa hiệu suất của agent trong dài hạn
