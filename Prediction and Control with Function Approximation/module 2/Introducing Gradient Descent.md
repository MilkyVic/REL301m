# Giới Thiệu Gradient Descent

## Giới thiệu
Gradient Descent là một phương pháp tối ưu hóa quan trọng được sử dụng để tối thiểu hóa hàm mục tiêu trong học tăng cường, đặc biệt là trong việc ước lượng hàm giá trị.

## Mục Tiêu
Tối thiểu hóa sai số bình phương trung bình của giá trị:
$$J(w) = \frac{1}{2} \mathbb{E}[(v_{\pi}(s) - \hat{v}(s,w))^2]$$

Trong đó:
- $v_{\pi}(s)$: giá trị thực của trạng thái s
- $\hat{v}(s,w)$: giá trị ước lượng với tham số w

## Đạo Hàm và Gradient

### Đạo Hàm
- Cho hàm f với tham số vô hướng w
- Đạo hàm cho biết cách thay đổi w để tăng hoặc giảm f
- Dấu của đạo hàm chỉ hướng thay đổi
- Độ lớn của đạo hàm chỉ độ dốc của hàm

### Gradient
- Cho hàm f với tham số vector w
- Gradient là vector của các đạo hàm riêng phần
- Công thức:
$$\nabla_w f(w) = [\frac{\partial f}{\partial w_1}, \frac{\partial f}{\partial w_2}, ..., \frac{\partial f}{\partial w_n}]^T$$

## Gradient Descent

### Quy Tắc Cập Nhật
$$w_{t+1} = w_t - \alpha \nabla_w J(w_t)$$

Trong đó:
- $\alpha$: tốc độ học (step size)
- $\nabla_w J(w_t)$: gradient của hàm mục tiêu tại w_t

### Ví Dụ: Xấp Xỉ Tuyến Tính
- Hàm giá trị tuyến tính: $\hat{v}(s,w) = w^T \phi(s)$
- Gradient: $\nabla_w \hat{v}(s,w) = \phi(s)$

## Hội Tụ và Điểm Dừng

### Các Loại Điểm Dừng
1. **Cực tiểu cục bộ (Local Minimum)**
   - Gradient = 0
   - Giá trị hàm nhỏ nhất trong lân cận
   - Điểm ổn định

2. **Cực đại cục bộ (Local Maximum)**
   - Gradient = 0
   - Giá trị hàm lớn nhất trong lân cận
   - Điểm không ổn định

3. **Điểm yên ngựa (Saddle Point)**
   - Gradient = 0
   - Không phải cực trị
   - Điểm không ổn định

### Tính Chất Hội Tụ
- Với $\alpha$ đủ nhỏ, thuật toán sẽ hội tụ đến điểm dừng
- Thường hội tụ đến cực tiểu cục bộ
- Tính ngẫu nhiên trong thuật toán giúp tránh các điểm dừng không tốt

## Hạn Chế

### Giới Hạn của Hàm Xấp Xỉ
- Cực tiểu toàn cục có thể không tương ứng với hàm giá trị thực
- Phụ thuộc vào:
  - Cách chọn hàm xấp xỉ
  - Mục tiêu tối ưu hóa

### Ví Dụ Đơn Giản
- Vector đặc trưng chỉ chứa phần tử 1
- Hàm giá trị xấp xỉ sẽ hội tụ đến giá trị trung bình
- Không phải hàm giá trị tốt nhưng là tốt nhất có thể với tham số hóa này

## Kết luận
- Gradient Descent là công cụ mạnh mẽ để tối ưu hóa
- Cần hiểu rõ về:
  - Điểm dừng và tính chất hội tụ
  - Giới hạn của hàm xấp xỉ
  - Ảnh hưởng của việc chọn tham số
