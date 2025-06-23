# Đánh giá về Expected Sarsa và Q-learning với Function Approximation

Nội dung này tập trung vào khái niệm Expected Sarsa với function approximation trong học tăng cường, cũng như mối liên hệ với Q-learning.

## Expected Sarsa với Function Approximation

- Expected Sarsa với function approximation cập nhật trọng số (weight vector) dựa trên kỳ vọng giá trị hành động ở trạng thái tiếp theo, thay vì chỉ sử dụng giá trị của một hành động được chọn ngẫu nhiên.
- Kỳ vọng này được tính bằng tổng các giá trị hành động, mỗi giá trị được nhân với xác suất chọn hành động đó theo chính sách mục tiêu (target policy).

**Phương trình cập nhật:**
$$
W \leftarrow W + \alpha \left( R + \gamma \sum_{a} \pi(a|s') Q(s', a; W) - Q(s, a; W) \right)
$$

Trong đó:
- $W$: vector trọng số cho function approximation.
- $\alpha$: tốc độ học.
- $R$: phần thưởng nhận được.
- $\gamma$: hệ số chiết khấu.
- $s'$: trạng thái tiếp theo.
- $\pi(a|s')$: xác suất chọn hành động $a$ ở trạng thái $s'$ theo chính sách mục tiêu.
- $Q(s', a; W)$: giá trị hành động ước lượng ở trạng thái $s'$, hành động $a$ với trọng số $W$.

## Q-learning với Function Approximation

- Q-learning là một trường hợp đặc biệt của Expected Sarsa, trong đó chính sách mục tiêu là greedy (tham lam) với các giá trị hành động xấp xỉ.
- Phương trình cập nhật của Q-learning sử dụng giá trị hành động lớn nhất ở trạng thái tiếp theo thay vì kỳ vọng:

$$
W \leftarrow W + \alpha \left( R + \gamma \max_{a} Q(s', a; W) - Q(s, a; W) \right)
$$

## Chuyển tiếp từ Sarsa sang Expected Sarsa

- Cập nhật của Sarsa với function approximation tương tự như trường hợp bảng (tabular), sử dụng hệ số trọng số và gradient.
- Expected Sarsa cũng theo cấu trúc này, nhưng tính giá trị hành động từ vector trọng số cho mọi hành động ở trạng thái tiếp theo.

## Kết luận

- Expected Sarsa và Q-learning với function approximation đều mở rộng khả năng áp dụng của các thuật toán TD control sang các không gian trạng thái lớn hoặc liên tục.
- Sự khác biệt chính nằm ở cách tính mục tiêu cập nhật: Expected Sarsa dùng kỳ vọng theo chính sách, còn Q-learning dùng giá trị lớn nhất. 