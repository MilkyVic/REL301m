# Vấn đề K-Armed Bandit

## Giới thiệu
K-armed bandit là một bài toán cổ điển trong học máy và lý thuyết ra quyết định, mô phỏng tình huống người chơi phải đưa ra lựa chọn giữa nhiều phương án khác nhau để tối đa hóa phần thưởng nhận được.

## Ví dụ Thực tế
Hãy tưởng tượng bạn là một bác sĩ muốn áp dụng 3 kiểu điều trị khác nhau lên bệnh nhân (k=3). Mỗi lần bệnh nhân tới tìm, bạn sẽ kê 1 loại đơn khác nhau, và mục tiêu ở đây là tìm ra đơn tốt nhất cho bệnh nhân
- Bác sĩ có số lần kê đơn có hạn
- Mỗi lần kê đơnn sẽ cho kết quả ngẫu nhiên
- Mục tiêu là kiếm được đơn thuốc tốt nhất


## Action Values
1. **Values (giá trị)**
   - Values ở đây là phần thưởng được dự kiến 
   - Công thức: q*(a) = 𝔼[Rt|At = a] với ∀a ∈ {1,...,k}
   - Trong đó:
     + q*(a): giá trị thực của hành động a
     + Rt: phần thưởng tại thời điểm t
     + At: hành động được chọn tại thời điểm t
     + a: hành động bất kỳ trong tập k hành động
   - Công thức này cho biết giá trị kỳ vọng của phần thưởng khi chọn hành động a


2. **Rewards (Phần thưởng)**
   - Giá trị nhận được sau mỗi lần kéo cần
   - Thường là các giá trị số
   - Có tính ngẫu nhiên theo phân phối xác suất

3. **Strategy (Chiến lược)**
   - Cách thức lựa chọn cần gạt trong mỗi lượt
   - Cần cân bằng giữa khám phá và khai thác

## Thách Thức Chính: Exploration vs. Exploitation

### Exploration (Khám phá)
- Thử nghiệm các cần gạt mới
- Thu thập thông tin về phân phối phần thưởng
- Rủi ro nhận được phần thưởng thấp
- Cần thiết để tìm ra lựa chọn tối ưu

### Exploitation (Khai thác)
- Sử dụng cần gạt đã biết cho phần thưởng tốt
- Tận dụng kiến thức đã có
- An toàn hơn nhưng có thể bỏ lỡ cơ hội tốt hơn

## Ứng dụng Thực tế
1. **Marketing Online**
   - A/B testing quảng cáo
   - Tối ưu hóa nội dung hiển thị

2. **Hệ thống Đề xuất**
   - Đề xuất sản phẩm cho người dùng
   - Cá nhân hóa nội dung

3. **Tài chính**
   - Quản lý danh mục đầu tư
   - Phân bổ nguồn lực

## Kết luận
K-armed bandit là một mô hình quan trọng trong việc học cách ra quyết định dưới điều kiện không chắc chắn. Nó cung cấp nền tảng cho nhiều thuật toán học máy và ứng dụng thực tế.