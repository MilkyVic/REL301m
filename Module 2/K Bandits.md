<!--
layout: default
title: K-Armed Bandit
---

<script type="text/javascript" async
  src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
</script>

<style>
mjx-container {
  font-size: 10000% !important;
}
</style>
-->

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
  - Công thức: 
$$q_*(a) \overset{\text{.}}{=} \mathbb{E}[R_t \mid A_t = a], \quad \forall a \in \{1, \ldots, k}\$$
  - Trong đó:
    + $q_{*}(a)$: giá trị thực của hành động a
    + $R_t$: phần thưởng tại thời điểm t
    + $A_t$: hành động được chọn tại thời điểm t
    + $a$: hành động bất kỳ trong tập k hành động
  - Công thức này cho biết giá trị kỳ vọng của phần thưởng khi chọn hành động a 




## Ứng dụng Thực tế

 **Recommendation System**
   - Đề xuất nội dung cho người dùng
   - Cá nhân hóa nội dung



## Vì sao nên tìm hiểu K bandits trước khi học reinforcement learning ? 
K-armed bandit là một mô hình quan trọng trong việc học cách ra quyết định dưới điều kiện không chắc chắn. Nó là nền tảng cho nhiều thuật toán machine learning và real-life application.
-------------------------------------------------------------------------------------------------------
  ##### 5-12-2025 at 5PM.
  ##### Course: Fundamentals of Reinforcement Learning/Module 2.
  ##### Đọc tài liệu tại: K-Armed Bandit problem.
  ##### Học nội dung từ clip: K-Armed Bandit problem/Sequential Decision Making with Evaluative Feedback.
