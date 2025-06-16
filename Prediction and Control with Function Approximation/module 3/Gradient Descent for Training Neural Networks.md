# Gradient Descent cho Huấn Luyện Mạng Nơ-ron

## Giới thiệu
Thuật toán backpropagation dựa trên gradient descent, nhằm tối thiểu hóa hàm mất mát đo lường sai số dự đoán. Gradient chỉ ra hướng tăng nhanh nhất, và di chuyển ngược lại giúp tối thiểu hóa mất mát.

## Ký Hiệu và Cấu Trúc
- Đầu vào mạng: S
- Đầu ra: ŷ
- Tầng ẩn: x
- Trọng số A: ảnh hưởng đến tầng ẩn
- Trọng số B: ảnh hưởng đến đầu ra

## Đạo Hàm Gradient

### Đạo Hàm cho Trọng Số B
1. **Bước 1**: Đạo hàm hàm mất mát theo ŷ
2. **Bước 2**: Đạo hàm ŷ theo B
3. **Kết quả**: Gradient = ΔB × x

### Đạo Hàm cho Trọng Số A
1. **Bước 1**: Đạo hàm hàm mất mát theo x
2. **Bước 2**: Đạo hàm x theo A
3. **Kết quả**: Gradient = ΔA × S

## Thuật Toán Backpropagation

### Quy Tắc Chuỗi
- Sử dụng quy tắc chuỗi để tính đạo hàm
- Bắt đầu từ tầng đầu ra
- Lan truyền ngược lỗi qua các tầng

### Các Bước Thực Hiện
1. **Lan Truyền Tiến**
   - Tính đầu ra ŷ
   - Tính hàm mất mát L

2. **Lan Truyền Ngược**
   - Tính ΔB cho tầng đầu ra
   - Tính ΔA cho tầng ẩn
   - Cập nhật trọng số

### Mã Giả
```
For each (s,y) in dataset:
    # Forward pass
    ŷ = network(s)
    
    # Backward pass
    ΔB = (ŷ - y) × x
    B = B - αB × ΔB
    
    ΔA = ΔB × f'(ψ) × s
    A = A - αA × ΔA
```

## Tối Ưu Hóa

### Hiệu Quả Tính Toán
- Tránh tính lại các đạo hàm
- Tái sử dụng ΔB cho ΔA
- Lan truyền lỗi từ tầng sau ra tầng trước

### Mở Rộng
- Áp dụng cho mạng sâu hơn
- Δ của tầng trước được tính đệ quy từ Δ của tầng sau
- Cập nhật luôn có dạng: Δ × đầu vào

## Ví Dụ Cụ Thể

### Mạng với ReLU
1. Tính lỗi tầng đầu ra
2. Tính đạo hàm ReLU theo ψ
3. Tính Δ cho tầng ẩn
4. Cập nhật trọng số

## Kết Luận
- Backpropagation là gradient descent với chiến lược tính gradient hiệu quả
- Cập nhật trọng số dựa trên lan truyền ngược lỗi
- Có thể mở rộng cho mạng sâu và phức tạp
- Hiệu quả trong việc tối ưu hóa hàm mất mát
