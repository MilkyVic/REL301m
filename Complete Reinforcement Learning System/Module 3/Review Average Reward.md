# Đánh giá về Average Reward trong Reinforcement Learning

Nội dung này tập trung vào cách tiếp cận average reward (phần thưởng trung bình) trong học tăng cường, đặc biệt phù hợp với các bài toán liên tục (continuing tasks).

## Hiểu về Average Reward

Average reward là một cách tiếp cận giúp đánh giá hiệu suất dài hạn của tác tử mà không cần sử dụng hệ số chiết khấu (discount factor). Thay vì ưu tiên phần thưởng gần, average reward xem trọng tổng phần thưởng nhận được trên toàn bộ quá trình, giúp tác tử tối ưu hóa tốc độ nhận thưởng trung bình.

Công thức average reward của một chính sách (ký hiệu $R_\pi$) dựa trên kỳ vọng phần thưởng nhận được ở mỗi trạng thái, có tính đến tần suất tác tử ghé thăm các trạng thái đó.

## Ví dụ về Nearsighted MDP

Một ví dụ điển hình là MDP với hai vòng lặp (rings), nơi tác tử có thể chọn đi theo vòng trái hoặc phải. Mỗi vòng có phần thưởng khác nhau tại các vị trí nhất định. Khi sử dụng discount factor, việc lựa chọn chính sách tối ưu phụ thuộc mạnh vào giá trị gamma. Tuy nhiên, với average reward, tác tử sẽ ưu tiên chính sách mang lại tổng phần thưởng trung bình cao nhất, không bị ảnh hưởng bởi gamma.

## Differential Returns và Value Functions

Trong thiết lập average reward, giá trị trả về (return) được định nghĩa là hiệu giữa phần thưởng nhận được và average reward, gọi là differential return. Điều này giúp so sánh hiệu quả của các hành động trong cùng một chính sách.

Hàm giá trị (value function) trong average reward phản ánh kỳ vọng của differential return, cho phép sử dụng các phương trình Bellman mà không cần discount, giúp chuyển đổi các thuật toán cũ sang bối cảnh average reward dễ dàng hơn.

## Thuật toán Average Reward (Differential Sarsa)

Một thuật toán phổ biến cho average reward là Differential Sarsa, với các bước chính:

1. Khởi tạo:
   - Đặt ước lượng average reward $R$ ban đầu bằng 0.
   - Khởi tạo hàm giá trị hành động $Q(s, a)$.
   - Chọn trạng thái và hành động ban đầu.

2. Lặp lại cho mỗi bước:
   - Thực hiện hành động $a$, quan sát phần thưởng $r$ và trạng thái mới $s'$.
   - Tính differential return: $r - R$.
   - Cập nhật $Q(s, a)$:  
     $Q(s, a) \leftarrow Q(s, a) + \alpha \cdot (r - R)$
   - Cập nhật average reward:  
     $R \leftarrow R + \beta \cdot (r - R)$
   - Chuyển sang trạng thái mới và chọn hành động tiếp theo.

3. Chính sách có thể là epsilon-greedy hoặc softmax dựa trên $Q$.

## Kết luận

Average reward là một cách tiếp cận mạnh mẽ cho các bài toán liên tục, giúp tác tử tối ưu hóa hiệu suất dài hạn mà không cần lo lắng về việc lựa chọn hệ số chiết khấu. Các thuật toán như Differential Sarsa cho phép học cả giá trị hành động lẫn average reward, mở rộng khả năng áp dụng của học tăng cường trong thực tế.
