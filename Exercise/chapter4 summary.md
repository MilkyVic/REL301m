# Chương 4: Dynamic Programming (Sutton & Barto, 2020)

##  Main point
Dynamic Programming (DP) là tập hợp các thuật toán giúp giải bài toán tối ưu chính sách trong MDP (Markov Decision Process) khi **biết rõ mô hình môi trường**. DP là cơ sở lý thuyết cho nhiều phương pháp học tăng cường hiện đại.

---

## 1. Policy Evaluation (Dự đoán giá trị chính sách)

### Mục tiêu:
Tính toán giá trị kỳ vọng (expected return) của từng trạng thái khi thực hiện chính sách $ \pi $. Giá trị này gọi là **state-value function**: $ v_\pi(s) $

### Công thức kỳ vọng:

$$ v_\pi(s) = \mathbb{E}\pi [ G_t \mid S_t = s ] = \mathbb{E}\pi [ R_{t+1} + \gamma v_\pi(S_{t+1}) \mid S_t = s ] $$

- $ G_t $: tổng phần thưởng về sau (return)
- $ \gamma $: hệ số chiết khấu
- Tức là giá trị của một trạng thái bằng phần thưởng ngay sau đó cộng với giá trị chiết khấu của trạng thái kế tiếp.

### Dạng tổng quát (Bellman Equation):

$$ v_\pi(s) = \sum_a \pi(a|s) \sum_{s',r} p(s', r \mid s, a) [r + \gamma v_\pi(s')] $$

Giải thích:
- $ \pi(a|s) $: xác suất chọn hành động $ a $ ở trạng thái $ s $
- $ p(s', r \mid s, a) $: xác suất chuyển đến trạng thái $ s' $ và nhận phần thưởng $ r $
- Công thức này tính kỳ vọng theo mọi hành động và mọi kết quả có thể.

### Phương pháp lặp (Iterative Policy Evaluation):

$$
v_{k+1}(s) = \sum_a \pi(a|s) \sum_{s',r} p(s', r \mid s, a) [r + \gamma v_k(s')]
\tag{4.5}
$$

- Bắt đầu với $ v_0(s) $ bất kỳ, lặp lại công thức này để hội tụ về $ v_\pi(s) $

---

## 2. Policy Improvement (Cải tiến chính sách)

### Mục tiêu:
Tìm chính sách tốt hơn bằng cách tận dụng $ v_\pi $ để chọn hành động tốt hơn.

### Hàm hành động (Action-Value Function):

$$q_\pi(s, a) = \mathbb{E}\pi [\sum_{k=0}^{\infty} \gamma^k R_{t+k+1} \mid S_t = s, A_t = a] = \sum_{s', r} p(s', r \mid s, a) [r + \gamma v_\pi(s')]
\tag{4.6}
$$

- Cho biết giá trị kỳ vọng nếu chọn hành động $ a $ tại trạng thái $ s $ và sau đó tuân theo chính sách $ \pi $

### Chính sách tham lam (Greedy policy):

$$
\pi'(s) = \arg\max_a q_\pi(s, a)
\tag{4.9}
$$

- Tại mỗi trạng thái, chọn hành động có $ q $ lớn nhất → dẫn đến chính sách mới tốt hơn hoặc bằng chính sách cũ.

---

## 3. Policy Iteration (Lặp cải tiến chính sách)

### Mô tả:
- Bắt đầu từ chính sách bất kỳ
- Lặp lại 2 bước:
  1. Policy Evaluation: Tính $ v_\pi $
  2. Policy Improvement: Tạo $ \pi' $ từ $ v_\pi $

### Cập nhật chính sách:

$$
\pi(s) = \arg\max_a \sum_{s'} P(s'\mid s, a) [R(s,a,s') + \gamma V(s')]
$$

- Dừng khi $ \pi $ không thay đổi nữa ⇒ chính sách tối ưu $ \pi^* $

---

## 4. Value Iteration (Lặp giá trị)

### Mô tả:
- Kết hợp luôn bước cải tiến chính sách vào bước đánh giá, thực hiện cập nhật trực tiếp như sau:

$$
v_{k+1}(s) = \max_a \sum_{s', r} p(s', r \mid s, a) [r + \gamma v_k(s')]
\tag{4.10}
$$

- Không cần đánh giá đầy đủ mỗi chính sách → nhanh hơn nhưng vẫn hội tụ về $ v^* $

---

## 5. Asynchronous Dynamic Programming

### Mô tả:
- Không cần cập nhật toàn bộ trạng thái cùng lúc.
- Cập nhật trạng thái bất kỳ, theo bất kỳ thứ tự nào.

### Ví dụ cập nhật tại một trạng thái:

$$
v(s_k) \leftarrow \max_a \sum_{s', r} p(s', r \mid s_k, a) [r + \gamma v(s')]
$$

- Miễn là mỗi trạng thái được cập nhật đủ số lần → vẫn hội tụ.

---

## 6. Generalized Policy Iteration (GPI)

### Mô hình tổng quát:
Hai quá trình song song:
- **Cải tiến chính sách**: $ \pi \leftarrow \text{greedy}(v) $
- **Đánh giá chính sách**: $ v \leftarrow v_\pi $

### Khi hội tụ:
$$
\pi = \pi^*, \quad v = v^*
$$

- Đây là cơ sở của phần lớn thuật toán RL hiện đại.

---

## 7. Tổng hợp công thức Bellman

| Loại giá trị         | Công thức                                                                 |
|----------------------|---------------------------------------------------------------------------|
| $ v_\pi(s) $    | $ \sum_a \pi(a|s) \sum_{s',r} p(s',r|s,a)[r + \gamma v_\pi(s')] $ |
| $ q_\pi(s,a) $  | $ \sum_{s',r} p(s',r|s,a)[r + \gamma v_\pi(s')] $                   |
| $ v^*(s) $       | $ \max_a \sum_{s',r} p(s',r|s,a)[r + \gamma v^*(s')] $              |
| $ q^*(s,a) $     | $ \sum_{s',r} p(s',r|s,a)[r + \gamma \max_{a'} q^*(s',a')] $        |

---

## Chi tiết công thức Bellman:

Hàm giá trị trạng thái ($ v_\pi(s) $):

```math
v_\pi(s) = \sum_a \pi(a|s) \sum_{s',r} p(s',r|s,a)[r + \gamma v_\pi(s')]
```

Hàm giá trị hành động ($ q_\pi(s,a) $):

```math
q_\pi(s,a) = \sum_{s',r} p(s',r|s,a)[r + \gamma v_\pi(s')]
```

Hàm giá trị tối ưu ($ v^*(s) $):

```math
v^*(s) = \max_a \sum_{s',r} p(s',r|s,a)[r + \gamma v^*(s')]
```

Hàm giá trị hành động tối ưu ($ q^*(s,a) $):

```math
q^*(s,a) = \sum_{s',r} p(s',r|s,a)[r + \gamma \max_{a'} q^*(s',a')]
```

---

## Kết luận

- DP yêu cầu mô hình môi trường chính xác.
- Gồm các thuật toán: Policy Evaluation, Policy Iteration, Value Iteration, GPI.
- Là nền tảng cho nhiều phương pháp RL, dù trong thực tế mô hình thường không biết trước.

