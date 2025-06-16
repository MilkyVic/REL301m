# Chuyển sang Hàm Tham Số Hóa

## Giới thiệu
Hàm tham số hóa là một phương pháp quan trọng trong việc xấp xỉ hàm giá trị, cho phép chúng ta xử lý các không gian trạng thái lớn một cách hiệu quả.

## Hàm Tham Số Hóa

### Định nghĩa
Hàm tham số hóa sử dụng một tập các trọng số có thể điều chỉnh để ước lượng giá trị của các trạng thái:

$$v_{\hat{w}}(s) \approx v_{\pi}(s)$$

Trong đó:
- $v_{\hat{w}}(s)$: giá trị ước lượng cho trạng thái s
- $v_{\pi}(s)$: giá trị thực của trạng thái s theo chính sách π
- $\hat{w}$: vector trọng số

### Công thức tổng quát
$$v_{\hat{w}}(s) = \sum_{i=1}^{n} w_i \cdot x_i(s)$$

Trong đó:
- $w_i$: trọng số thứ i
- $x_i(s)$: đặc trưng thứ i của trạng thái s
- n: số lượng đặc trưng

## Xấp xỉ Tuyến tính

### Biểu diễn Vector
$$v_{\hat{w}}(s) = \mathbf{x}(s)^T \cdot \mathbf{w}$$

Trong đó:
- $\mathbf{x}(s)$: vector đặc trưng của trạng thái s
- $\mathbf{w}$: vector trọng số
- $^T$: ký hiệu chuyển vị

### Cập nhật Trọng số
$$\mathbf{w}_{t+1} = \mathbf{w}_t + \alpha \cdot \delta_t \cdot \mathbf{x}(s_t)$$

Trong đó:
- $\alpha$: tốc độ học
- $\delta_t$: sai số TD tại bước thời gian t
- $s_t$: trạng thái tại bước thời gian t

## Mạng Nơ-ron

### Hàm kích hoạt
$$f(x) = \frac{1}{1 + e^{-x}}$$

### Lan truyền ngược
$$\frac{\partial L}{\partial w_{ij}} = \frac{\partial L}{\partial y_j} \cdot \frac{\partial y_j}{\partial w_{ij}}$$

Trong đó:
- L: hàm mất mát
- $w_{ij}$: trọng số kết nối từ nơ-ron i đến nơ-ron j
- $y_j$: đầu ra của nơ-ron j

## Ưu điểm của Hàm Tham Số Hóa

1. **Hiệu quả bộ nhớ**
   - Không cần lưu trữ giá trị cho từng trạng thái
   - Chỉ cần lưu trữ vector trọng số

2. **Khả năng tổng quát hóa**
   - Có thể dự đoán giá trị cho các trạng thái chưa gặp
   - Học được các mẫu hình và quy luật từ dữ liệu

3. **Khả năng mở rộng**
   - Phù hợp với không gian trạng thái lớn
   - Có thể xử lý các trạng thái liên tục

## Ứng dụng

1. **Học tăng cường**
   - Xấp xỉ hàm giá trị
   - Xấp xỉ hàm hành động-giá trị

2. **Hệ thống đề xuất**
   - Dự đoán giá trị người dùng
   - Tối ưu hóa quyết định

3. **Điều khiển robot**
   - Xấp xỉ hàm chính sách
   - Học từ dữ liệu cảm biến
