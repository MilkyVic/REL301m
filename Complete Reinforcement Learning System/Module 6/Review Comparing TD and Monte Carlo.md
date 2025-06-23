# Đánh giá về So sánh TD và Monte Carlo

Nội dung này tập trung vào việc so sánh hai phương pháp học tăng cường: Temporal Difference (TD) Learning và Monte Carlo, thông qua một thí nghiệm khoa học cụ thể.

## So sánh TD Learning và Monte Carlo

- Thí nghiệm sử dụng một quá trình quyết định không kết thúc (NDP) đơn giản với năm trạng thái và hai hành động, đánh giá chính sách chọn hành động ngẫu nhiên đều.
- TD Learning cập nhật giá trị của trạng thái ngay sau mỗi bước chuyển tiếp, trong khi Monte Carlo chỉ cập nhật giá trị sau khi kết thúc toàn bộ episode.

## Đánh giá hiệu suất

- Sau nhiều episode, TD Learning hội tụ nhanh hơn về giá trị thực so với Monte Carlo.
- Tốc độ học và độ chính xác phụ thuộc vào tốc độ học (learning rate): tốc độ học lớn giúp hội tụ nhanh nhưng sai số cuối cùng cao hơn, tốc độ học nhỏ giúp hội tụ chậm nhưng chính xác hơn.

## Sự khác biệt chính giữa TD và Monte Carlo

- **Thời điểm cập nhật:**
  - TD Learning: cập nhật sau mỗi bước, sử dụng giá trị trạng thái tiếp theo.
  - Monte Carlo: cập nhật sau mỗi episode, sử dụng tổng phần thưởng của cả episode.
- **Cách tiếp cận học:**
  - TD Learning: kết hợp ý tưởng từ dynamic programming và Monte Carlo, có thể học từ các episode chưa hoàn thành.
  - Monte Carlo: chỉ dựa vào các episode hoàn chỉnh để tính toán giá trị trung bình.

## TD Error trong TD Learning

- TD error là sai số giữa giá trị dự đoán của trạng thái hiện tại và giá trị thực tế quan sát được sau khi thực hiện hành động.
- **Công thức:**
  $$
  \text{TD Error} = \text{Reward} + \gamma \cdot V(s') - V(s)
  $$
  - Reward: phần thưởng nhận được sau khi chuyển sang trạng thái tiếp theo.
  - $\gamma$: hệ số chiết khấu.
  - $V(s')$: giá trị ước lượng của trạng thái tiếp theo.
  - $V(s)$: giá trị ước lượng của trạng thái hiện tại.

## Kết luận

- TD Learning hội tụ nhanh hơn và đạt sai số cuối cùng thấp hơn Monte Carlo trong bài toán này.
- TD error là thành phần cốt lõi giúp cập nhật giá trị trạng thái trong TD Learning, cho phép tác tử học hiệu quả từ từng trải nghiệm.
