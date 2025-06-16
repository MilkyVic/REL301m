# Semi-Gradient TD cho Đánh Giá Chính Sách

## Giới thiệu
Semi-Gradient TD là một phương pháp kết hợp giữa Temporal Difference (TD) learning và function approximation, cho phép cập nhật ước lượng giá trị dựa trên chính các ước lượng hiện tại.

## Cập Nhật TD với Function Approximation

### Công thức Cập Nhật
$$w_{t+1} = w_t + \alpha[U_t - \hat{v}(s_t,w_t)]\nabla_w \hat{v}(s_t,w_t)$$

Trong đó:
- $U_t$: mục tiêu cập nhật (target)
- $\hat{v}(s_t,w_t)$: giá trị ước lượng hiện tại
- $\alpha$: tốc độ học

### Các Loại Mục Tiêu

1. **Mục Tiêu Không Thiên Vị (Unbiased Target)**
   - Ví dụ: Return $G_t$
   - Đảm bảo hội tụ đến cực tiểu cục bộ
   - Công thức: $U_t = G_t$

2. **Mục Tiêu Bootstrap**
   - Ví dụ: TD target
   - Có thể thiên vị
   - Công thức: $U_t = R_{t+1} + \gamma \hat{v}(s_{t+1},w_t)$

## Semi-Gradient TD

### Đặc Điểm
- Không phải là gradient descent thực sự
- Bỏ qua gradient của mục tiêu
- Vẫn hội tụ trong nhiều trường hợp thực tế

### Lý Do Gọi là "Semi-Gradient"
- Gradient đầy đủ:
$$\nabla_w \frac{1}{2}[U_t - \hat{v}(s_t,w_t)]^2 = [U_t - \hat{v}(s_t,w_t)]\nabla_w \hat{v}(s_t,w_t) - [U_t - \hat{v}(s_t,w_t)]\nabla_w U_t$$

- Semi-gradient (bỏ qua $\nabla_w U_t$):
$$\nabla_w \frac{1}{2}[U_t - \hat{v}(s_t,w_t)]^2 \approx [U_t - \hat{v}(s_t,w_t)]\nabla_w \hat{v}(s_t,w_t)$$

## Thuật Toán

### Bước 1: Khởi Tạo
- Chọn hàm xấp xỉ $\hat{v}(s,w)$ khả vi theo w
- Khởi tạo vector trọng số w
- Chọn tốc độ học $\alpha$

### Bước 2: Cập Nhật Trực Tuyến
Với mỗi bước thời gian:
1. Chọn hành động $A_t$ trong trạng thái $S_t$
2. Nhận phần thưởng $R_{t+1}$ và trạng thái tiếp theo $S_{t+1}$
3. Tính TD target: $U_t = R_{t+1} + \gamma \hat{v}(S_{t+1},w_t)$
4. Cập nhật trọng số:
   $$w_{t+1} = w_t + \alpha[U_t - \hat{v}(S_t,w_t)]\nabla_w \hat{v}(S_t,w_t)$$

## So Sánh với Monte Carlo

### Ưu Điểm của TD
1. **Cập Nhật Trực Tuyến**
   - Không cần đợi kết thúc episode
   - Học nhanh hơn

2. **Phương Sai Thấp**
   - Sử dụng bootstrap
   - Ít biến động hơn

### Hạn Chế
1. **Thiên Vị**
   - Mục tiêu phụ thuộc vào ước lượng hiện tại
   - Không đảm bảo hội tụ đến cực tiểu

2. **Phức Tạp Hơn**
   - Cần xử lý gradient một phần
   - Có thể không ổn định

## Kết luận
- Semi-Gradient TD là phương pháp hiệu quả cho function approximation
- Kết hợp ưu điểm của TD và gradient descent
- Phù hợp cho các bài toán cần cập nhật trực tuyến
- Cần lưu ý về tính thiên vị và điều kiện hội tụ
