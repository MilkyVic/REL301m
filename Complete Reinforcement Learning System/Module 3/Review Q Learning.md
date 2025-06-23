# Đánh giá về Q-Learning

Nội dung này tập trung vào Q-learning, một trong những thuật toán nền tảng và có ảnh hưởng nhất trong học tăng cường.

## Hiểu về Q-Learning

Q-learning là một thuật toán học tăng cường không cần mô hình (model-free) và hoạt động theo kiểu off-policy. Được phát triển vào năm 1989, nó đã trở thành nền tảng cho nhiều ứng dụng phức tạp, từ việc chơi game Atari đến điều khiển hệ thống.

Mục tiêu chính của Q-learning là học trực tiếp hàm giá trị hành động tối ưu, ký hiệu là $Q^*$, bất kể chính sách mà tác tử đang tuân theo là gì. Để làm được điều này, nó sử dụng một phiên bản dựa trên mẫu của phương trình tối ưu Bellman.

## Quy trình Cập nhật Học

Điểm khác biệt cốt lõi của Q-learning nằm ở cách nó cập nhật giá trị hành động. Thay vì sử dụng cặp trạng thái-hành động tiếp theo (như Sarsa), Q-learning sử dụng giá trị hành động lớn nhất có thể ở trạng thái tiếp theo.

Công thức cập nhật (còn gọi là quy tắc Q-learning):
$$Q(s_t, a_t) \leftarrow Q(s_t, a_t) + \alpha \left[ R_{t+1} + \gamma \max_{a'} Q(s_{t+1}, a') - Q(s_t, a_t) \right]$$

- **Mục tiêu (Target):** $R_{t+1} + \gamma \max_{a'} Q(s_{t+1}, a')$
- Việc sử dụng toán tử $\max$ cho phép thuật toán ước tính phần thưởng tương lai bằng cách giả định rằng tác tử sẽ luôn chọn hành động tốt nhất có thể từ trạng thái tiếp theo trở đi.

## So sánh với Sarsa và Tính Tối ưu

Sự khác biệt trong công thức cập nhật dẫn đến những đặc điểm riêng biệt của hai thuật toán:

- **Sarsa (On-policy):** Sarsa cập nhật giá trị Q dựa trên hành động $a_{t+1}$ mà tác tử *thực sự* thực hiện. Nó học giá trị của chính sách mà nó đang tuân theo (bao gồm cả các bước thăm dò).
- **Q-learning (Off-policy):** Q-learning cập nhật giá trị Q dựa trên hành động tốt nhất có thể $a'$ ở trạng thái tiếp theo. Điều này cho phép nó học chính sách tối ưu ngay cả khi nó đang thực hiện các hành động thăm dò ngẫu nhiên.

Nhờ việc áp dụng phương trình tối ưu Bellman, Q-learning có thể cải thiện liên tục hàm giá trị và được đảm bảo sẽ hội tụ đến hàm giá trị hành động tối ưu $Q^*$, miễn là tất cả các cặp trạng thái-hành động được khám phá đầy đủ.
