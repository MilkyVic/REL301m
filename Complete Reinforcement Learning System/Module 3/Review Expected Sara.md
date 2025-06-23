# Đánh giá về Expected Sarsa

Nội dung này tập trung vào thuật toán Expected Sarsa, một phương pháp trong học tăng cường.

## Hiểu về Expected Sarsa

Expected Sarsa là một phương pháp điều khiển dựa trên sự khác biệt thời gian (TD), tính toán trực tiếp kỳ vọng của các giá trị hành động thay vì lấy mẫu chúng. Thuật toán này sử dụng phương trình Bellman cho các giá trị hành động, chia nhỏ kỳ vọng thành một tổng trên các trạng thái và hành động tiếp theo có thể xảy ra.

Thay vì lấy mẫu hành động tiếp theo từ chính sách (như Sarsa), Expected Sarsa tính toán trực tiếp kỳ vọng bằng cách lấy tổng có trọng số của các giá trị của tất cả các hành động tiếp theo có thể có. Các trọng số chính là xác suất thực hiện mỗi hành động theo chính sách của tác tử.

## Quy trình Cập nhật Học

Việc cập nhật học trong Expected Sarsa tương tự như Sarsa, nhưng nó sử dụng ước tính kỳ vọng của giá trị hành động tiếp theo thay vì một giá trị được lấy mẫu.

Công thức cập nhật:
$$Q(s_t, a_t) \leftarrow Q(s_t, a_t) + \alpha \left[ R_{t+1} + \gamma \sum_a \pi(a|s_{t+1})Q(s_{t+1}, a) - Q(s_t, a_t) \right]$$

Điều này dẫn đến một mục tiêu cập nhật ổn định hơn, vì các mục tiêu của Expected Sarsa có phương sai thấp hơn đáng kể so với Sarsa.

## Ưu điểm và Nhược điểm

### Ưu điểm
Expected Sarsa cung cấp phương sai thấp hơn trong các mục tiêu cập nhật, dẫn đến các ước tính giá trị chính xác hơn và sự hội tụ tốt hơn trong nhiều trường hợp.

### Nhược điểm
Tuy nhiên, việc tính toán giá trị trung bình qua tất cả các hành động có thể có chi phí tính toán cao, đặc biệt là khi số lượng hành động lớn. Chi phí này phát sinh vì việc tính trung bình phải được thực hiện ở mỗi bước thời gian.
