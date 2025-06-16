# Thuật Toán Actor-Critic

## Giới thiệu
Actor-Critic là phương pháp kết hợp giữa học chính sách trực tiếp và học hàm giá trị, trong đó:
- Actor: chính sách tham số hóa
- Critic: hàm giá trị đánh giá hành động

## Cấu Trúc Thuật Toán

### Actor (Chính Sách)
- Tham số hóa chính sách $\pi(a|s,\theta)$
- Cập nhật dựa trên gradient
- Tối ưu hóa để tăng xác suất hành động tốt

### Critic (Hàm Giá Trị)
- Ước lượng giá trị trạng thái $V(s)$
- Sử dụng TD learning
- Cung cấp phản hồi tức thì

## Cập Nhật Gradient

### TD Error
$$\delta_t = r_t + \gamma V(s_{t+1}) - V(s_t)$$
Trong đó:
- $r_t$: phần thưởng
- $\gamma$: hệ số chiết khấu
- $V(s)$: giá trị trạng thái

### Cập Nhật Chính Sách
$$\theta_{t+1} = \theta_t + \alpha \delta_t \nabla_\theta \log \pi(a_t|s_t)$$
Trong đó:
- $\alpha$: tốc độ học
- $\nabla_\theta \log \pi$: gradient của log chính sách

### Baseline
$$\theta_{t+1} = \theta_t + \alpha (\delta_t - b(s_t)) \nabla_\theta \log \pi(a_t|s_t)$$
Trong đó:
- $b(s_t)$: giá trị baseline cho trạng thái $s_t$

## Thuật Toán Đầy Đủ

### Khởi Tạo
1. **Tham Số**
   - Chính sách: $\theta$
   - Hàm giá trị: $w$
   - Tốc độ học: $\alpha_\theta$, $\alpha_w$
   - Phần thưởng trung bình: $\bar{R} = 0$

2. **Biểu Diễn**
   - Tile coding cho hàm giá trị
   - Softmax cho chính sách

### Vòng Lặp Học
1. **Chọn Hành Động**
   - $a \sim \pi(\cdot|s,\theta)$
   - Nhận $(s',r)$ từ môi trường

2. **Cập Nhật Critic**
   - Tính TD error
   - Cập nhật $w$

3. **Cập Nhật Actor**
   - Tính gradient
   - Cập nhật $\theta$

4. **Cập Nhật Phần Thưởng**
   $$\bar{R} = \bar{R} + \alpha_{\bar{R}}(r - \bar{R})$$

## Ưu Điểm
- Kết hợp ưu điểm của cả hai phương pháp
- Học liên tục và trực tuyến
- Giảm phương sai cập nhật
- Phản hồi tức thì từ critic

## Ứng Dụng
- Bài toán liên tục
- Môi trường phức tạp
- Cần học nhanh và ổn định
