# Average Reward: Cách Tiếp Cận Mới trong Bài Toán Điều Khiển

## Giới thiệu
Trong các bài toán liên tục (continuing tasks), chúng ta quan tâm đến hiệu suất dài hạn. Thay vì sử dụng discounting, chúng ta có thể sử dụng cách tiếp cận mới gọi là average reward formulation.

## Ví Dụ MDP Cận Thị (Nearsighted MDP)

### Cấu Trúc
- Hai vòng tròn giao nhau
- Một trạng thái đặc biệt có thể chọn hành động
- Hai chính sách xác định: đi vòng trái hoặc vòng phải

### Phần Thưởng
- Vòng trái: +1 ngay sau trạng thái S
- Vòng phải: +2 ngay trước trạng thái S
- Các trạng thái khác: 0

## So Sánh với Discounting

### Giá Trị Trạng Thái
1. **Chính Sách Trái**
   - V(S) = 1/(1-γ⁵)
   - Với γ = 0.5: V ≈ 1
   - Với γ = 0.9: V ≈ 2.4

2. **Chính Sách Phải**
   - V(S) = 2γ⁴/(1-γ⁵)
   - Với γ = 0.5: V ≈ 0.1
   - Với γ = 0.9: V ≈ 3.2

### Hạn Chế của Discounting
- γ cần đủ lớn (≥ 0.841)
- Phụ thuộc vào kích thước vấn đề
- Không thể đặt γ = 1 trong môi trường liên tục

## Average Reward Formulation

### Định Nghĩa
- R(π): phần thưởng trung bình của chính sách π
- Tính bằng tổng có trọng số của phần thưởng kỳ vọng
- Trọng số là tần suất viếng thăm trạng thái (μ)

### Tính Toán
1. **Vòng Trái**
   - Phần thưởng trung bình = 0.2 (1/5)
   - Các trạng thái được viếng thăm đều nhau

2. **Vòng Phải**
   - Phần thưởng trung bình = 0.4 (2/5)
   - Hiệu quả hơn mà không cần discounting

## Differential Returns

### Định Nghĩa
- Đo lường phần thưởng vượt trội so với trung bình
- Tổng của (phần thưởng - R(π))
- Sử dụng Cesaro sum cho môi trường tuần hoàn

### Tính Chất
1. **Hội Tụ**
   - Chỉ hội tụ khi trừ đúng R(π)
   - Phân kỳ nếu trừ giá trị khác

2. **So Sánh Hành Động**
   - Chỉ so sánh được khi cùng chính sách
   - So sánh chính sách dùng R(π)

## Differential Value Functions

### Định Nghĩa
- Kỳ vọng của differential returns
- Đo lường phần thưởng vượt trội từ trạng thái
- Có thể viết dưới dạng phương trình Bellman

### Phương Trình Bellman
- Tương tự như trường hợp discounting
- Trừ R(π) từ phần thưởng tức thời
- Không có discounting

## Differential Sarsa

### Khác Biệt
1. **Theo Dõi R(π)**
   - Ước lượng phần thưởng trung bình
   - Sử dụng kỹ thuật trung bình gia tăng

2. **Cập Nhật**
   - Trừ R(π) từ phần thưởng mẫu
   - Sử dụng cập nhật có phương sai thấp hơn

## Kết Luận
- Average reward là cách tiếp cận thay thế cho discounting
- Phù hợp cho bài toán liên tục dài hạn
- Có thể áp dụng nhiều thuật toán từ trường hợp discounting
- Cần theo dõi và ước lượng R(π)
- Cung cấp cách so sánh chính sách trực quan hơn
