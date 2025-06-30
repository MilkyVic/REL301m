# 🎮 Trò Chơi Tic Tac Toe (Cờ Caro) - Python

Một trò chơi Tic Tac Toe hoàn chỉnh được tạo bằng Python với giao diện đồ họa sử dụng Tkinter, hỗ trợ nhiều kích thước bàn cờ.

## ✨ Tính Năng

- 🖥️ **Giao diện đồ họa** đẹp mắt với Tkinter
- 🎨 **Thiết kế hiện đại** với màu sắc và layout chuyên nghiệp
- 📏 **Nhiều kích thước bàn cờ**: 3x3, 5x5, 7x7
- 📊 **Bảng điểm** theo dõi thắng/thua/hòa
- 💾 **Lưu điểm số** tự động vào file JSON
- 🔄 **Tự động reset** sau khi kết thúc
- 🎯 **Highlight ô thắng** với màu xanh lá
- 🎮 **Điều khiển dễ dàng** với các nút chức năng
- 📱 **Giao diện responsive** và thân thiện
- 🔄 **Chuyển đổi kích thước** bàn cờ linh hoạt

## 🚀 Cách Chạy

### Yêu Cầu Hệ Thống
- Python 3.6 trở lên
- Tkinter (thường đã có sẵn trong Python)

### Cài Đặt

1. **Clone hoặc tải xuống** các file vào thư mục
2. **Kiểm tra Python**: Mở terminal/command prompt và gõ:
   ```bash
   python --version
   ```
3. **Chạy trò chơi**:
   ```bash
   python app.py
   ```

### Nếu Gặp Lỗi Tkinter

Nếu gặp lỗi "No module named 'tkinter'", hãy cài đặt:

**Ubuntu/Debian:**
```bash
sudo apt-get install python3-tk
```

**CentOS/RHEL:**
```bash
sudo yum install tkinter
```

**Windows/macOS:** Thường đã có sẵn Tkinter

## 🎮 Cách Chơi

1. **Khởi động**: Chạy `python app.py`
2. **Chọn kích thước**: Click vào nút "3 x 3", "5 x 5", hoặc "7 x 7"
3. **Luật chơi**: 
   - Người chơi X đi trước (màu đỏ)
   - Người chơi O đi sau (màu xanh)
   - Click vào ô trống để đánh
   - Tạo N ô liên tiếp (ngang, dọc hoặc chéo) để thắng
     - 3x3: Tạo 3 ô liên tiếp
     - 5x5: Tạo 5 ô liên tiếp  
     - 7x7: Tạo 5 ô liên tiếp
4. **Điều khiển**:
   - **Chơi Lại**: Reset bàn cờ hiện tại
   - **Trò Chơi Mới**: Reset toàn bộ điểm số
   - **Thoát**: Đóng ứng dụng

## 🎨 Giao Diện

- **Người chơi X**: Màu đỏ (#e74c3c)
- **Người chơi O**: Màu xanh (#3498db)
- **Ô thắng**: Màu xanh lá (#27ae60)
- **Bảng điểm**: Hiển thị số lần thắng của mỗi người chơi
- **Trạng thái**: Hiển thị lượt hiện tại và kích thước bàn cờ
- **Nút kích thước**: 
  - 3x3: Màu cam (#e67e22)
  - 5x5: Màu xanh (#3498db)
  - 7x7: Màu xanh (#3498db)

## 📁 Cấu Trúc File

```
Tic Tac Toe/
├── app.py              # File chính của trò chơi
├── requirements.txt    # Danh sách thư viện cần thiết
├── scores.json         # File lưu điểm số (tự động tạo)
└── README.md          # Hướng dẫn sử dụng
```

## 🛠️ Công Nghệ Sử Dụng

- **Python 3.6+**: Ngôn ngữ lập trình chính
- **Tkinter**: Thư viện GUI
- **JSON**: Lưu trữ điểm số
- **OS**: Thao tác với hệ thống file

## 🎯 Tính Năng Chi Tiết

### Nhiều Kích Thước Bàn Cờ
- **3x3**: Bàn cờ truyền thống, tạo 3 ô liên tiếp để thắng
- **5x5**: Bàn cờ trung bình, tạo 5 ô liên tiếp để thắng
- **7x7**: Bàn cờ lớn, tạo 5 ô liên tiếp để thắng (cân bằng hơn)
- **Tự động điều chỉnh**: Kích thước button và font chữ thay đổi theo bàn cờ

### Lưu Điểm Số
- Điểm số được lưu tự động vào file `scores.json`
- Dữ liệu được khôi phục khi khởi động lại trò chơi
- Hỗ trợ Unicode cho tiếng Việt

### Giao Diện
- Cửa sổ được căn giữa màn hình
- Kích thước cố định 800x900 pixels
- Màu sắc theo theme hiện đại
- Font chữ rõ ràng và dễ đọc

### Logic Game
- Kiểm tra thắng cho tất cả kích thước bàn cờ
- Xử lý trường hợp hòa
- Chuyển lượt tự động
- Highlight ô thắng
- Chuyển đổi kích thước bàn cờ linh hoạt

## 🎨 Tùy Chỉnh

Bạn có thể tùy chỉnh trò chơi bằng cách:

### Thay Đổi Màu Sắc
```python
# Trong file app.py, tìm và thay đổi các mã màu:
bg='#2c3e50'      # Màu nền chính
fg='#ecf0f1'      # Màu chữ
```

### Thay Đổi Kích Thước
```python
# Thay đổi kích thước cửa sổ:
self.window.geometry("800x900")
```

### Thêm Kích Thước Mới
```python
# Trong hàm create_widgets(), thêm vào danh sách sizes:
sizes = [("3 x 3", 3), ("5 x 5", 5), ("7 x 7", 7), ("9 x 9", 9)]
```

### Thay Đổi Số Ô Thắng
```python
# Trong hàm get_win_length(), thay đổi logic:
def get_win_length(self):
    if self.board_size == 3:
        return 3
    elif self.board_size == 5:
        return 5
    else:  # 7x7
        return 5  # Có thể thay đổi thành 6 hoặc 7
```

### Thay Đổi Font
```python
# Thay đổi font chữ:
font=('Arial', 24, 'bold')
```

## 🐛 Xử Lý Lỗi

### Lỗi Thường Gặp

1. **"No module named 'tkinter'"**
   - Giải pháp: Cài đặt Tkinter theo hướng dẫn trên

2. **"Permission denied" khi lưu file**
   - Giải pháp: Chạy với quyền admin hoặc thay đổi thư mục

3. **Font không hiển thị đúng**
   - Giải pháp: Thay đổi font thành font có sẵn trong hệ thống

4. **Bàn cờ quá lớn không hiển thị hết**
   - Giải pháp: Tăng kích thước cửa sổ hoặc giảm kích thước button

## 📝 Lịch Sử Phiên Bản

- **v1.0**: Phiên bản đầu tiên với đầy đủ tính năng cơ bản
- **v2.0**: Thêm hỗ trợ nhiều kích thước bàn cờ (3x3, 5x5, 7x7)
- **v2.1**: Cân bằng luật chơi cho bàn cờ 7x7 (5 ô thay vì 7 ô)
- Giao diện Tkinter hoàn chỉnh
- Lưu/load điểm số
- Highlight ô thắng
- Tự động reset
- Chuyển đổi kích thước bàn cờ

## 🎮 Chiến Lược Chơi

### Bàn Cờ 3x3
- Chiến lược cơ bản, tập trung vào trung tâm
- Thời gian chơi ngắn, phù hợp cho người mới
- Cần 3 ô liên tiếp để thắng

### Bàn Cờ 5x5
- Chiến lược phức tạp hơn, nhiều khả năng
- Cần tạo nhiều đường thắng đồng thời
- Cần 5 ô liên tiếp để thắng

### Bàn Cờ 7x7
- Chiến lược cao cấp, đòi hỏi tư duy dài hạn
- Thời gian chơi lâu, phù hợp cho người chơi có kinh nghiệm
- Cần 5 ô liên tiếp để thắng (cân bằng hơn so với 7 ô)

## 🤝 Đóng Góp

Nếu bạn muốn đóng góp cho dự án:
1. Fork repository
2. Tạo branch mới
3. Commit thay đổi
4. Push và tạo Pull Request

## 📄 Giấy Phép

Dự án này được phát hành dưới giấy phép MIT.

---

**Chúc bạn chơi vui vẻ! 🎉**

*Tạo bởi AI Assistant với ❤️* 