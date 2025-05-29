# Exercise 4.2 – Gridworld (Sutton & Barto)

## Summary

###  Example 4.1:
- Lưới 4×4, đánh số từ 1 đến 14.
- Các trạng thái đích ở góc là tường (không thể vào).
- Mỗi hành động đều dẫn đến phần thưởng \( R_t = -1 \).
- Chính sách: **chọn đều 4 hành động (trái, phải, lên, xuống)**.

### Exercise 4.2:
1. Thêm trạng thái **15**, phía dưới ô **13**.
2. Từ **15**, các hành động:
   - `left → 12`
   - `up → 13`
   - `right → 14`
   - `down → 15` (tự chuyển về chính nó).
3. Phần đầu: **Không thay đổi dynamics của các trạng thái cũ**.
4. Phần sau: Thay đổi trạng thái 13 → đi xuống thì đến 15.

---

## 1 – Không thay đổi dynamics cũ

giá trị trạng thái của state 15 theo công thức Bellman:

$$v_\pi(15) = \sum_a \pi(a|15) \sum_{s',r} p(s', r | 15, a) [r + \gamma v_\pi(s')]$$

- Với mỗi hành động có xác suất \( \frac{1}{4} \), \( \gamma = 1 \), \( r = -1 \):

$$v_\pi(15) = \frac{1}{4} \sum_{s'} [-1 + v_\pi(s')]$$

Các trạng thái đích từ state 15:
- left → 12
- up → 13
- right → 14
- down → 15 (self)

$$v_\pi(15) = \frac{1}{4} [ -1 + v_\pi(12) + (-1 + v_\pi(13)) + (-1 + v_\pi(14)) + (-1 + v_\pi(15)) ]$$

$$v_\pi(15) = \frac{1}{4} [ -4 + v_\pi(12) + v_\pi(13) + v_\pi(14) + v_\pi(15) ]$$

$$\Rightarrow \frac{3}{4}v_\pi(15) = \frac{1}{4} [ -4 + v_\pi(12) + v_\pi(13) + v_\pi(14) ]$$

$$\Rightarrow v_\pi(15) = \frac{-4 + v_\pi(12) + v_\pi(13) + v_\pi(14)}{3}$$

Giá trị từ sách:
- \( v_\pi(12) = -22 \)
- \( v_\pi(13) = -20 \)
- \( v_\pi(14) = -14 \)

$$v_\pi(15) = \frac{-4 -22 -20 -14}{3} = \frac{-60}{3} = -20$$

---

## 2 – state 13 đi xuống tới state 15

Giờ đây, hành động `down` từ state 13 dẫn đến state 15.

$$v_\pi(13) = \frac{1}{4} [ -1 + v_\pi(12) + (-1 + v_\pi(14)) + (-1 + v_\pi(9)) + (-1 + v_\pi(15)) ]$$

$$v_\pi(13) = \frac{-4 + v_\pi(12) + v_\pi(14) + v_\pi(9) + v_\pi(15)}{4}$$

Giá trị:
- \( v_\pi(12) = -22 \)
- \( v_\pi(14) = -14 \)
- \( v_\pi(9) = -18 \)

Gọi \( x = v_\pi(15) \):

$$v_\pi(13) = \frac{-58 + x}{4}$$

Kết hợp lại công thức phần 1:

$$v_\pi(15) = \frac{-4 + v_\pi(12) + v_\pi(13) + v_\pi(14)}{3}
= \frac{-40 + v_\pi(13)}{3}$$

$$\Rightarrow x = \frac{-40 + \frac{-58 + x}{4}}{3}
= \frac{-218 + x}{12}
\Rightarrow 12x = -218 + x
\Rightarrow 11x = -218
\Rightarrow x = -19.82$$

---

## Conclusion:

- **1 (không thay đổi dynamics)**:  
   \( v_\pi(15) = -20 \)

- **2 (13 đi xuống 15)**:  
  👉 \( v_\pi(15) \approx -19.82 \)
