# Gradient Monte Carlo cho Đánh Giá Chính Sách

## Giới thiệu
Gradient Monte Carlo là một thuật toán kết hợp giữa phương pháp Monte Carlo và gradient descent để ước lượng hàm giá trị trong học tăng cường.

## Mục Tiêu
Tối thiểu hóa sai số bình phương trung bình của giá trị:
$$J(w) = \frac{1}{2} \sum_{s \in \mathcal{S}} \mu(s)[v_{\pi}(s) - \hat{v}(s,w)]^2$$

Trong đó:
- $\mu(s)$: phân phối trạng thái
- $v_{\pi}(s)$: giá trị thực
- $\hat{v}(s,w)$: giá trị ước lượng

## Gradient của Hàm Mục Tiêu

### Công thức Gradient
$$\nabla_w J(w) = \sum_{s \in \mathcal{S}} \mu(s)[v_{\pi}(s) - \hat{v}(s,w)]\nabla_w \hat{v}(s,w)$$

### Xấp Xỉ Tuyến Tính
- Với $\hat{v}(s,w) = w^T \phi(s)$
- Gradient: $\nabla_w \hat{v}(s,w) = \phi(s)$

## Stochastic Gradient Descent

### Cập Nhật Trọng Số
$$w_{t+1} = w_t + \alpha[v_{\pi}(s_t) - \hat{v}(s_t,w_t)]\nabla_w \hat{v}(s_t,w_t)$$

Trong đó:
- $\alpha$: tốc độ học
- $s_t$: trạng thái tại bước thời gian t

### Ưu Điểm
- Không cần tính toán gradient đầy đủ
- Cập nhật hiệu quả trên từng mẫu
- Hướng đến cực tiểu toàn cục

## Thuật Toán Gradient Monte Carlo

### Bước 1: Khởi Tạo
- Chọn hàm xấp xỉ $\hat{v}(s,w)$ khả vi theo w
- Khởi tạo vector trọng số w
- Chọn tốc độ học $\alpha$

### Bước 2: Tạo Episode
- Tương tác với môi trường theo chính sách $\pi$
- Thu thập chuỗi trạng thái và phần thưởng
- Tính toán giá trị trả về (return) cho mỗi trạng thái

### Bước 3: Cập Nhật Trọng Số
- Với mỗi trạng thái trong episode:
  - Tính gradient của hàm xấp xỉ
  - Cập nhật trọng số theo công thức:
  $$w_{t+1} = w_t + \alpha[G_t - \hat{v}(s_t,w_t)]\nabla_w \hat{v}(s_t,w_t)$$
  Trong đó $G_t$ là giá trị trả về mẫu

## Tính Chất

### Ưu Điểm
1. **Hiệu Quả Tính Toán**
   - Không cần lưu trữ toàn bộ dữ liệu
   - Cập nhật trực tuyến

2. **Khả Năng Tổng Quát Hóa**
   - Áp dụng được cho không gian trạng thái lớn
   - Học từ dữ liệu mẫu

3. **Đơn Giản**
   - Dễ hiểu và triển khai
   - Không yêu cầu mô hình môi trường

### Hạn Chế
1. **Tính Ngẫu Nhiên**
   - Cập nhật có thể không giảm sai số ngay lập tức
   - Cần nhiều episode để hội tụ

2. **Phụ Thuộc vào Mẫu**
   - Chất lượng ước lượng phụ thuộc vào chất lượng mẫu
   - Có thể không ổn định với dữ liệu nhiễu

## Kết luận
- Gradient Monte Carlo là phương pháp hiệu quả để ước lượng hàm giá trị
- Kết hợp ưu điểm của Monte Carlo và gradient descent
- Phù hợp cho các bài toán với không gian trạng thái lớn
