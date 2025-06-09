# Đánh Giá Chính Sách và Điều Khiển (Policy Evaluation vs Control)

## 1. Tổng Quan
Đánh giá chính sách và điều khiển là hai khái niệm cốt lõi trong học tăng cường, đặc biệt trong lập trình động (Dynamic Programming). Chúng đại diện cho hai nhiệm vụ chính trong quá trình tối ưu hóa chính sách.

## 2. Đánh Giá Chính Sách (Policy Evaluation)

### 2.1. Định Nghĩa
- Nhiệm vụ xác định hàm giá trị cho một chính sách cụ thể (π)
- Đánh giá mức độ hiệu quả của chính sách đó
- Tính toán phần thưởng kỳ vọng từ mỗi trạng thái.

### 2.2. Mục Tiêu
- Tính toán hàm giá trị trạng thái vπ
- Đánh giá chất lượng của chính sách hiện tại
- Hiểu rõ hiệu suất của chính sách trong từng trạng thái

### 2.3. Ứng Dụng Thực Tế
1. **Lái Xe Tự Động**:
   - Đánh giá chính sách lái xe dựa trên tín hiệu giao thông
   - Tính toán mức độ an toàn và hiệu quả của tuyến đường
   - Đánh giá các chiến lược lái xe khác nhau

2. **Quản Lý Kho**:
   - Đánh giá chính sách bổ sung hàng tồn kho
   - Ước tính lợi nhuận kỳ vọng từ các mức tồn kho khác nhau
   - Hướng dẫn quyết định quản lý kho trong tương lai

### 2.4. Công Thức Toán Học

**Phương trình Bellman cho Hàm Giá Trị Trạng Thái:**

$$v_\pi(s) = \sum_{a} \pi(a|s) \sum_{s'} \sum_{r} p(s', r|s, a) [r + \gamma v_\pi(s')]$$

Trong đó:
- $v_\pi(s)$: Giá trị của trạng thái s theo chính sách π
- $\pi(a|s)$: Xác suất thực hiện hành động a trong trạng thái s theo chính sách π
- $p(s', r|s, a)$: Xác suất chuyển đến trạng thái s' và nhận phần thưởng r khi thực hiện hành động a trong trạng thái s
- $\gamma$: Hệ số chiết khấu
- $v_\pi(s')$: Giá trị của trạng thái kế tiếp s'

**Công Thức Lặp cho Đánh Giá Chính Sách:**

$$v_{k+1}(s) \leftarrow \sum_{a} \pi(a|s) \sum_{s'} \sum_{r} p(s', r|s, a) [r + \gamma v_k(s')]$$

Công thức này cho phép tính toán hàm giá trị vπ một cách lặp đi lặp lại, khởi đầu từ một hàm giá trị tùy ý (ví dụ: v0(s) = 0 cho mọi s). Sau mỗi lần lặp k, giá trị mới vk+1(s) được ước tính dựa trên giá trị vk(s') của các trạng thái kế tiếp. Quá trình này hội tụ về vπ(s).

## 3. Điều Khiển (Control)

### 3.1. Định Nghĩa
- Nhiệm vụ cải thiện chính sách hiện tại để tối đa hóa phần thưởng
- Tìm chính sách mới tốt hơn chính sách hiện tại
- Hướng đến chính sách tối ưu

### 3.2. Mục Tiêu
- Tạo ra chính sách mới có giá trị cao hơn
- Đạt được chính sách tối ưu khi không thể cải thiện thêm
- Tối đa hóa phần thưởng tổng thể

## 4. Kỹ Thuật Lập Trình Động

### 4.1. Cơ Sở Toán Học
- Sử dụng phương trình Bellman
- Tạo các thuật toán lặp
- Tính toán hàm giá trị và chính sách tối ưu

### 4.2. Điều Kiện Áp Dụng
- Cần biết trước động học của môi trường
- Có thể mô hình hóa môi trường
- Có thể tính toán xác suất chuyển trạng thái

## 5. Cải Thiện Chính Sách

### 5.1. Tiêu Chí Đánh Giá
- Chính sách tốt hơn có giá trị cao hơn trong mọi trạng thái
- So sánh giá trị giữa các chính sách
- Xác định hướng cải thiện

### 5.2. Quy Trình Cải Thiện
1. Đánh giá chính sách hiện tại
2. Xác định các hành động tốt hơn
3. Cập nhật chính sách
4. Lặp lại quá trình

## 6. Ví Dụ Minh Họa

### 6.1. Trò Chơi Đơn Giản
- **Đánh Giá Chính Sách**:
  + Tính toán giá trị của mỗi trạng thái
  + Đánh giá hiệu quả của chiến lược hiện tại
  + Xác định các trạng thái yếu

- **Điều Khiển**:
  + Tìm hành động tốt hơn cho các trạng thái yếu
  + Cập nhật chính sách
  + Đánh giá lại hiệu quả

### 6.2. Kết Quả
- Chính sách được cải thiện qua mỗi lần lặp
- Giá trị trạng thái tăng dần
- Tiến đến chính sách tối ưu

## 7. Kết Luận
Đánh giá chính sách và điều khiển:
- Là hai nhiệm vụ bổ sung cho nhau
- Tạo nên quy trình tối ưu hóa chính sách
- Cho phép cải thiện liên tục hiệu suất của agent
