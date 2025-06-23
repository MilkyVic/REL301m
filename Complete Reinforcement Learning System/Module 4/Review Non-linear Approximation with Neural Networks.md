# Đánh giá về Non-linear Approximation with Neural Networks

Nội dung này tập trung vào cách mạng nơ-ron (neural networks) xây dựng đặc trưng (features) phi tuyến cho dự đoán trong học tăng cường.

## Hiểu về Neural Networks

Neural networks học các đặc trưng hữu ích thông qua quá trình nhân đầu vào với trọng số (weights) và truyền qua các hàm kích hoạt phi tuyến. Mỗi node trong mạng tạo ra một đặc trưng khác nhau, và tập hợp các đặc trưng này tạo thành một biểu diễn mới cho dữ liệu đầu vào.

## So sánh với Tile Coding

- Cả tile coding và neural networks đều sử dụng các tham số cố định để xây dựng đặc trưng, nhưng neural networks có thể điều chỉnh các tham số này trong quá trình học dựa trên dữ liệu.
- Neural networks tạo ra các đặc trưng phi tuyến, cho phép biểu diễn các mối quan hệ phức tạp hơn so với tổ hợp tuyến tính trong tile coding.

## Vai trò của Trọng số (Weights)

- Mỗi đầu vào được nhân với một trọng số, điều chỉnh mức độ ảnh hưởng của đầu vào lên đầu ra của node.
- Tổng có trọng số này được truyền qua hàm kích hoạt phi tuyến, tạo ra đầu ra của node.
- Trong quá trình học, các trọng số được cập nhật dựa trên sai số dự đoán, giúp mạng cải thiện hiệu suất dự đoán theo thời gian.

## Thuật toán huấn luyện mạng nơ-ron

1. **Lan truyền tiến (Forward Propagation):**
   - Đầu vào được truyền qua từng lớp của mạng.
   - Mỗi node tính tổng có trọng số và áp dụng hàm kích hoạt để tạo đầu ra.

2. **Tính toán hàm mất mát (Loss Function):**
   - Đầu ra của mạng được so sánh với giá trị mục tiêu để tính toán sai số dự đoán.

3. **Lan truyền ngược (Backpropagation):**
   - Tính gradient của hàm mất mát đối với từng trọng số bằng quy tắc chuỗi.
   - Lan truyền sai số ngược qua các lớp để xác định mức độ điều chỉnh trọng số.

4. **Cập nhật trọng số (Weight Update):**
   - Sử dụng các thuật toán tối ưu hóa như SGD hoặc Adam để cập nhật trọng số dựa trên gradient và tốc độ học.

5. **Lặp lại quá trình:** 
   - Quá trình này được lặp lại nhiều lần cho đến khi mạng đạt hiệu suất mong muốn.

## Tổng kết

Neural networks là công cụ mạnh mẽ để xây dựng các đặc trưng phi tuyến, cho phép mô hình hóa các mối quan hệ phức tạp trong dữ liệu. Khả năng điều chỉnh trọng số trong quá trình học giúp mạng thích nghi và cải thiện hiệu suất dự đoán, vượt trội so với các phương pháp xây dựng đặc trưng cố định như tile coding.
