# Actor-Critic với Softmax Policies

## Giới thiệu
Actor-Critic kết hợp tối ưu hóa chính sách trực tiếp, hàm giá trị và học TD. Trong bài này, chúng ta sẽ xem xét một triển khai cụ thể sử dụng:
- Xấp xỉ hàm tuyến tính
- Tham số hóa chính sách Softmax

## Chính Sách Softmax

### Định Nghĩa
$$\pi(a|s) = \frac{e^{h(s,a,\theta)}}{\sum_b e^{h(s,b,\theta)}}$$
Trong đó:
- $h(s,a,\theta)$: hàm ưu tiên hành động
- $\theta$: tham số chính sách
- Đảm bảo xác suất dương và tổng bằng 1

### Chọn Hành Động
1. Tính xác suất cho mỗi hành động
2. Chọn hành động theo phân phối xác suất
3. Phân phối thay đổi theo trạng thái

## Biểu Diễn Hàm

### Critic (Hàm Giá Trị)
- Sử dụng vector đặc trưng trạng thái
- Cập nhật trọng số $w$:
$$\Delta w = \alpha \delta_t \phi(s_t)$$

### Actor (Hàm Ưu Tiên)
- Sử dụng vector đặc trưng trạng thái-hành động
- Stacked features cho mỗi hành động
- Kích thước $\theta$ lớn hơn $w$ (gấp số hành động lần)

## Cập Nhật Gradient

### Critic
$$\nabla_w V(s) = \phi(s)$$
- $\phi(s)$: vector đặc trưng trạng thái
- Cập nhật đơn giản với semi-gradient TD

### Actor
$$\nabla_\theta \log \pi(a|s) = \phi(s,a) - \sum_b \pi(b|s)\phi(s,b)$$
Trong đó:
- $\phi(s,a)$: vector đặc trưng cho hành động được chọn
- $\sum_b \pi(b|s)\phi(s,b)$: kỳ vọng vector đặc trưng theo chính sách

## Thuật Toán

### Khởi Tạo
1. **Tham Số**
   - $\theta$: tham số chính sách
   - $w$: trọng số hàm giá trị
   - $\alpha_\theta$, $\alpha_w$: tốc độ học

2. **Đặc Trưng**
   - $\phi(s)$: đặc trưng trạng thái
   - $\phi(s,a)$: đặc trưng trạng thái-hành động

### Vòng Lặp Học
1. **Chọn Hành Động**
   - Tính xác suất $\pi(a|s)$ cho mỗi hành động
   - Chọn $a \sim \pi(\cdot|s)$

2. **Cập Nhật Critic**
   - Tính TD error
   - Cập nhật $w$

3. **Cập Nhật Actor**
   - Tính gradient
   - Cập nhật $\theta$

## Ưu Điểm
- Kết hợp ưu điểm của cả hai phương pháp
- Biểu diễn đơn giản với xấp xỉ tuyến tính
- Chính sách Softmax đảm bảo tính hợp lệ
- Cập nhật gradient hiệu quả
