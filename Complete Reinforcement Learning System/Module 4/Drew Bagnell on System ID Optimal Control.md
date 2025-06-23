# Đánh giá về Drew Bagnell on System ID Optimal Control

Nội dung này tập trung vào quá trình học mô hình trong học tăng cường dựa trên mô hình (model-based RL), nhấn mạnh các phương pháp thực tiễn và khái niệm No-Regret learning.

## Học mô hình trong Reinforcement Learning

- Bài giảng sử dụng ví dụ về điều khiển trực thăng tự động để minh họa cho quá trình học mô hình.
- Cách tiếp cận truyền thống (system identification) là một bài toán học có giám sát, thu thập dữ liệu qua các chính sách thăm dò và xây dựng mô hình dựa trên dữ liệu này.
- Tuy nhiên, trong thực tế, các kỹ sư thường sử dụng phương pháp lặp (iterative), kết hợp dữ liệu từ các lần thử nghiệm và tối ưu hóa chính sách qua nhiều vòng.

## Vấn đề "chicken or the egg" và giải pháp tương tác

- Việc học mô hình chính xác gặp khó khăn do dữ liệu ở các trạng thái ít được thăm dò thường không đủ, dẫn đến mô hình sai lệch và chính sách tối ưu hóa trên mô hình này có thể thất bại trong thực tế.
- Giải pháp là tiếp cận tương tác: thu thập dữ liệu từ cả chính sách hiện tại và chính sách thăm dò, tổng hợp các chuyển tiếp, và lặp lại quá trình xây dựng mô hình và tối ưu hóa chính sách.
- Phương pháp này giúp mô hình và chính sách được cải thiện liên tục, phù hợp hơn với thực tiễn kỹ thuật.

## Khái niệm No-Regret Learning

- No-Regret learning là lớp thuật toán đảm bảo rằng hiệu suất trung bình của thuật toán sẽ tiệm cận hiệu suất của chiến lược tốt nhất trong quá khứ khi số lần lặp tăng lên.
- Đặc điểm:
  - **Ổn định**: Ít nhạy cảm với thay đổi nhỏ trong dữ liệu huấn luyện.
  - **Hiệu suất lâu dài**: Đạt hiệu quả tốt khi có nhiều dữ liệu.
  - **Thích nghi**: Có thể điều chỉnh chiến lược dựa trên kết quả trước đó.
- No-Regret learning giúp tăng độ tin cậy và hiệu quả của hệ thống học tăng cường trong thực tế.

## Kết luận

- Việc học mô hình trong RL nên được thực hiện theo cách tương tác, lặp lại giữa thu thập dữ liệu và tối ưu hóa chính sách.
- Sử dụng các thuật toán No-Regret giúp đảm bảo hiệu suất ổn định và thích nghi tốt với môi trường thực tế.
- Phương pháp này đã được chứng minh hiệu quả qua các ví dụ thực tiễn như điều khiển trực thăng tự động.
