# Phương Trình Bellman (Bellman Equation)

## 1. Tổng Quan
Phương trình Bellman là nền tảng toán học trong học tăng cường, thiết lập mối quan hệ giữa giá trị của các trạng thái và hành động. Nó giúp chúng ta hiểu và tính toán giá trị của các trạng thái một cách hiệu quả.

## 2. Phương Trình Bellman Cho Hàm Giá Trị Trạng Thái

### 2.1. Định Nghĩa
Phương trình Bellman cho hàm giá trị trạng thái định nghĩa mối quan hệ giữa giá trị của một trạng thái và các trạng thái kế tiếp có thể có:

$$V^\pi(s) = \mathbb{E}_\pi[R_{t+1} + \gamma V^\pi(S_{t+1})|S_t=s]$$

Trong đó:
- $V^\pi(s)$: Giá trị của trạng thái hiện tại s
- $\mathbb{E}_\pi$: Kỳ vọng theo chính sách π
- $R_{t+1}$: Phần thưởng ngay lập tức nhận được
- $\gamma$: Hệ số chiết khấu (0 ≤ γ < 1)
- $V^\pi(S_{t+1})$: Giá trị của trạng thái kế tiếp

### 2.2. Ý Nghĩa
- Phần thưởng kỳ vọng được biểu diễn dưới dạng tổng có trọng số của:
  + Phần thưởng ngay lập tức
  + Giá trị của các trạng thái tương lai
- Hệ số chiết khấu γ điều chỉnh tầm quan trọng của phần thưởng tương lai

## 3. Phương Trình Bellman Cho Hàm Giá Trị Hành Động

### 3.1. Định Nghĩa
Phương trình Bellman cho hàm giá trị hành động thiết lập một phương trình đệ quy cho giá trị của cặp trạng thái-hành động:

$$Q^\pi(s,a) = \mathbb{E}_\pi[R_{t+1} + \gamma Q^\pi(S_{t+1},A_{t+1})|S_t=s,A_t=a]$$

Trong đó:
- $Q^\pi(s,a)$: Giá trị của hành động a trong trạng thái s
- $A_{t+1}$: Hành động tiếp theo
- Các ký hiệu khác tương tự như trên

### 3.2. Đặc Điểm
- Phần thưởng kỳ vọng được điều kiện hóa bởi:
  + Trạng thái tiếp theo
  + Hành động tiếp theo
- Tổng hợp trên tất cả các hành động có thể

## 4. Tầm Quan Trọng Của Phương Trình Bellman

### 4.1. Cấu Trúc Vấn Đề
- Nắm bắt cấu trúc cơ bản của bài toán học tăng cường
- Cung cấp cơ sở toán học cho việc thiết kế thuật toán
- Cho phép tính toán hiệu quả các hàm giá trị

### 4.2. Ứng Dụng
- Thiết kế các thuật toán ước lượng hàm giá trị
- Tối ưu hóa chính sách
- Học tăng cường hiệu quả

## 5. Ví Dụ Minh Họa

### 5.1. Trò Chơi Đơn Giản
Giả sử một trò chơi với:
- Phần thưởng ngay lập tức: R = 10
- Hệ số chiết khấu: γ = 0.9
- Giá trị trạng thái tiếp theo: V(s') = 20

Khi đó:
$$V(s) = 10 + 0.9 \times 20 = 28$$

### 5.2. Ý Nghĩa Thực Tế
- Giúp agent đánh giá giá trị của các trạng thái
- Hướng dẫn quá trình ra quyết định
- Tối ưu hóa chiến lược dài hạn

## 6. Kết Luận
Phương trình Bellman là công cụ không thể thiếu trong học tăng cường, giúp:
- Hiểu rõ mối quan hệ giữa các trạng thái
- Tính toán hiệu quả các hàm giá trị
- Thiết kế các thuật toán học tăng cường mạnh mẽ
