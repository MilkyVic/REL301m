import tkinter as tk
from tkinter import messagebox, ttk
import json
import os
from datetime import datetime

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe - Cờ Caro")
        self.window.geometry("800x900")
        self.window.configure(bg='#2c3e50')
        self.window.resizable(False, False)
        
        # Biến game
        self.board_size = 3  # Mặc định 3x3
        self.current_player = "X"
        self.board = []
        self.game_active = True
        self.scores = {"X": 0, "O": 0, "Draw": 0}
        self.buttons = []
        
        # Load điểm số từ file
        self.load_scores()
        
        # Tạo giao diện
        self.create_widgets()
        
        # Center window
        self.center_window()
        
    def center_window(self):
        """Căn giữa cửa sổ trên màn hình"""
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry(f'{width}x{height}+{x}+{y}')
    
    def create_widgets(self):
        """Tạo các widget cho giao diện"""
        # Frame chính
        main_frame = tk.Frame(self.window, bg='#2c3e50')
        main_frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        # Tiêu đề
        title_label = tk.Label(
            main_frame, 
            text="TIC TAC TOE", 
            font=('Arial', 24, 'bold'), 
            fg='#ecf0f1', 
            bg='#2c3e50'
        )
        title_label.pack(pady=(0, 10))
        
        subtitle_label = tk.Label(
            main_frame, 
            text="Cờ Caro", 
            font=('Arial', 14), 
            fg='#bdc3c7', 
            bg='#2c3e50'
        )
        subtitle_label.pack(pady=(0, 20))
        
        # Frame cho chọn kích thước bàn cờ
        size_frame = tk.Frame(main_frame, bg='#34495e', relief='raised', bd=2)
        size_frame.pack(fill='x', pady=(0, 20))
        
        size_title = tk.Label(
            size_frame, 
            text="CHỌN KÍCH THƯỚC BÀN CỜ", 
            font=('Arial', 12, 'bold'), 
            fg='#ecf0f1', 
            bg='#34495e'
        )
        size_title.pack(pady=10)
        
        size_buttons_frame = tk.Frame(size_frame, bg='#34495e')
        size_buttons_frame.pack(pady=(0, 10))
        
        # Nút chọn kích thước
        sizes = [("3 x 3", 3), ("5 x 5", 5), ("7 x 7", 7)]
        for text, size in sizes:
            btn = tk.Button(
                size_buttons_frame,
                text=text,
                font=('Arial', 10, 'bold'),
                bg='#e67e22' if size == 3 else '#3498db',
                fg='white',
                relief='raised',
                bd=2,
                command=lambda s=size: self.change_board_size(s),
                width=8,
                height=2
            )
            btn.pack(side='left', padx=10)
        
        # Frame cho bảng điểm
        score_frame = tk.Frame(main_frame, bg='#34495e', relief='raised', bd=2)
        score_frame.pack(fill='x', pady=(0, 20))
        
        # Bảng điểm
        score_title = tk.Label(
            score_frame, 
            text="BẢNG ĐIỂM", 
            font=('Arial', 12, 'bold'), 
            fg='#ecf0f1', 
            bg='#34495e'
        )
        score_title.pack(pady=10)
        
        score_content = tk.Frame(score_frame, bg='#34495e')
        score_content.pack(pady=(0, 10))
        
        # Điểm số
        self.score_labels = {}
        players = [("X", "#e74c3c"), ("O", "#3498db"), ("Draw", "#95a5a6")]
        
        for i, (player, color) in enumerate(players):
            frame = tk.Frame(score_content, bg='#34495e')
            frame.pack(side='left', padx=20)
            
            player_label = tk.Label(
                frame, 
                text=f"Người chơi {player}", 
                font=('Arial', 10), 
                fg='#ecf0f1', 
                bg='#34495e'
            )
            player_label.pack()
            
            score_label = tk.Label(
                frame, 
                text=str(self.scores[player]), 
                font=('Arial', 16, 'bold'), 
                fg=color, 
                bg='#34495e'
            )
            score_label.pack()
            
            self.score_labels[player] = score_label
        
        # Frame cho trạng thái game
        status_frame = tk.Frame(main_frame, bg='#34495e', relief='raised', bd=2)
        status_frame.pack(fill='x', pady=(0, 20))
        
        self.status_label = tk.Label(
            status_frame, 
            text=f"Lượt của: {self.current_player} (Bàn cờ {self.board_size}x{self.board_size})", 
            font=('Arial', 14, 'bold'), 
            fg='#f39c12', 
            bg='#34495e'
        )
        self.status_label.pack(pady=15)
        
        # Frame cho bàn cờ
        self.board_frame = tk.Frame(main_frame, bg='#34495e', relief='raised', bd=3)
        self.board_frame.pack(pady=(0, 20))
        
        # Tạo bàn cờ ban đầu
        self.create_board()
        
        # Frame cho các nút điều khiển
        control_frame = tk.Frame(main_frame, bg='#2c3e50')
        control_frame.pack(pady=(0, 20))
        
        # Nút Reset
        reset_button = tk.Button(
            control_frame,
            text="Chơi Lại",
            font=('Arial', 12, 'bold'),
            bg='#e74c3c',
            fg='white',
            relief='raised',
            bd=2,
            command=self.reset_game,
            width=12,
            height=2
        )
        reset_button.pack(side='left', padx=10)
        
        # Nút Trò Chơi Mới
        new_game_button = tk.Button(
            control_frame,
            text="Trò Chơi Mới",
            font=('Arial', 12, 'bold'),
            bg='#3498db',
            fg='white',
            relief='raised',
            bd=2,
            command=self.new_game,
            width=12,
            height=2
        )
        new_game_button.pack(side='left', padx=10)
        
        # Nút Thoát
        exit_button = tk.Button(
            control_frame,
            text="Thoát",
            font=('Arial', 12, 'bold'),
            bg='#95a5a6',
            fg='white',
            relief='raised',
            bd=2,
            command=self.window.quit,
            width=12,
            height=2
        )
        exit_button.pack(side='left', padx=10)
        
        # Frame cho thông tin
        info_frame = tk.Frame(main_frame, bg='#34495e', relief='raised', bd=2)
        info_frame.pack(fill='x')
        
        info_text = f"""
        HƯỚNG DẪN CHƠI:
        • Người chơi X đi trước
        • Click vào ô trống để đánh
        • Tạo {self.get_win_length()} ô liên tiếp để thắng
        • Nút 'Chơi Lại': Reset bàn cờ
        • Nút 'Trò Chơi Mới': Reset điểm số
        • Chọn kích thước bàn cờ ở trên
        """
        
        self.info_label = tk.Label(
            info_frame,
            text=info_text,
            font=('Arial', 9),
            fg='#ecf0f1',
            bg='#34495e',
            justify='left'
        )
        self.info_label.pack(pady=10)
    
    def get_win_length(self):
        """Lấy số ô cần để thắng dựa trên kích thước bàn cờ"""
        if self.board_size == 3:
            return 3
        elif self.board_size == 5:
            return 5
        else:  # 7x7
            return 5  # Thay đổi từ 7 thành 5
    
    def create_board(self):
        """Tạo bàn cờ với kích thước hiện tại"""
        # Xóa bàn cờ cũ
        for widget in self.board_frame.winfo_children():
            widget.destroy()
        
        # Tạo bàn cờ mới
        self.board = [""] * (self.board_size * self.board_size)
        self.buttons = []
        
        # Tính toán kích thước button dựa trên board_size
        if self.board_size == 3:
            button_width, button_height = 8, 3
            font_size = 20
        elif self.board_size == 5:
            button_width, button_height = 6, 2
            font_size = 16
        else:  # 7x7
            button_width, button_height = 4, 1
            font_size = 12
        
        for i in range(self.board_size):
            for j in range(self.board_size):
                button = tk.Button(
                    self.board_frame,
                    text="",
                    font=('Arial', font_size, 'bold'),
                    width=button_width,
                    height=button_height,
                    bg='#ecf0f1',
                    fg='#2c3e50',
                    relief='raised',
                    bd=2,
                    command=lambda row=i, col=j: self.button_click(row, col)
                )
                button.grid(row=i, column=j, padx=1, pady=1)
                self.buttons.append(button)
    
    def change_board_size(self, size):
        """Thay đổi kích thước bàn cờ"""
        if size != self.board_size:
            self.board_size = size
            self.create_board()
            self.reset_game()
            
            # Cập nhật thông tin
            info_text = f"""
            HƯỚNG DẪN CHƠI:
            • Người chơi X đi trước
            • Click vào ô trống để đánh
            • Tạo {self.get_win_length()} ô liên tiếp để thắng
            • Nút 'Chơi Lại': Reset bàn cờ
            • Nút 'Trò Chơi Mới': Reset điểm số
            • Chọn kích thước bàn cờ ở trên
            """
            self.info_label.config(text=info_text)
            
            messagebox.showinfo(
                "Thay Đổi Kích Thước", 
                f"Đã chuyển sang bàn cờ {size}x{size}!"
            )
    
    def button_click(self, row, col):
        """Xử lý khi click vào ô trên bàn cờ"""
        index = row * self.board_size + col
        
        if self.board[index] == "" and self.game_active:
            # Đánh dấu ô
            self.board[index] = self.current_player
            
            # Cập nhật giao diện
            button = self.buttons[index]
            button.config(
                text=self.current_player,
                bg='#e74c3c' if self.current_player == 'X' else '#3498db',
                fg='white'
            )
            
            # Kiểm tra thắng
            if self.check_winner():
                self.handle_win()
            elif self.check_draw():
                self.handle_draw()
            else:
                # Chuyển lượt
                self.current_player = "O" if self.current_player == "X" else "X"
                self.update_status()
    
    def check_winner(self):
        """Kiểm tra có người thắng không"""
        win_length = self.get_win_length()
        
        # Kiểm tra hàng ngang
        for row in range(self.board_size):
            for col in range(self.board_size - win_length + 1):
                if self.check_line(row, col, 0, 1, win_length):
                    return True
        
        # Kiểm tra hàng dọc
        for row in range(self.board_size - win_length + 1):
            for col in range(self.board_size):
                if self.check_line(row, col, 1, 0, win_length):
                    return True
        
        # Kiểm tra đường chéo chính
        for row in range(self.board_size - win_length + 1):
            for col in range(self.board_size - win_length + 1):
                if self.check_line(row, col, 1, 1, win_length):
                    return True
        
        # Kiểm tra đường chéo phụ
        for row in range(self.board_size - win_length + 1):
            for col in range(win_length - 1, self.board_size):
                if self.check_line(row, col, 1, -1, win_length):
                    return True
        
        return False
    
    def check_line(self, start_row, start_col, delta_row, delta_col, win_length):
        """Kiểm tra một đường thẳng có thắng không"""
        player = self.board[start_row * self.board_size + start_col]
        if player == "":
            return False
        
        winning_cells = []
        for i in range(win_length):
            row = start_row + i * delta_row
            col = start_col + i * delta_col
            
            if (0 <= row < self.board_size and 0 <= col < self.board_size):
                index = row * self.board_size + col
                if self.board[index] == player:
                    winning_cells.append(index)
                else:
                    return False
            else:
                return False
        
        # Highlight ô thắng
        for index in winning_cells:
            self.buttons[index].config(bg='#27ae60')
        
        return True
    
    def check_draw(self):
        """Kiểm tra hòa"""
        return "" not in self.board
    
    def handle_win(self):
        """Xử lý khi có người thắng"""
        self.game_active = False
        self.scores[self.current_player] += 1
        self.update_scores()
        self.save_scores()
        
        messagebox.showinfo(
            "Chúc mừng!", 
            f"Người chơi {self.current_player} thắng! 🎉"
        )
        
        self.window.after(2000, self.reset_game)
    
    def handle_draw(self):
        """Xử lý khi hòa"""
        self.game_active = False
        self.scores["Draw"] += 1
        self.update_scores()
        self.save_scores()
        
        messagebox.showinfo("Hòa!", "Trò chơi hòa! 🤝")
        
        self.window.after(2000, self.reset_game)
    
    def reset_game(self):
        """Reset bàn cờ"""
        self.board = [""] * (self.board_size * self.board_size)
        self.current_player = "X"
        self.game_active = True
        
        # Reset giao diện
        for button in self.buttons:
            button.config(text="", bg='#ecf0f1', fg='#2c3e50')
        
        self.update_status()
    
    def new_game(self):
        """Trò chơi mới - reset điểm số"""
        self.scores = {"X": 0, "O": 0, "Draw": 0}
        self.update_scores()
        self.save_scores()
        self.reset_game()
        
        messagebox.showinfo("Trò Chơi Mới", "Đã bắt đầu trò chơi mới!")
    
    def update_status(self):
        """Cập nhật trạng thái game"""
        color = '#e74c3c' if self.current_player == 'X' else '#3498db'
        self.status_label.config(
            text=f"Lượt của: {self.current_player} (Bàn cờ {self.board_size}x{self.board_size})",
            fg=color
        )
    
    def update_scores(self):
        """Cập nhật hiển thị điểm số"""
        for player, label in self.score_labels.items():
            label.config(text=str(self.scores[player]))
    
    def save_scores(self):
        """Lưu điểm số vào file"""
        try:
            with open('scores.json', 'w', encoding='utf-8') as f:
                json.dump(self.scores, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Lỗi khi lưu điểm số: {e}")
    
    def load_scores(self):
        """Load điểm số từ file"""
        try:
            if os.path.exists('scores.json'):
                with open('scores.json', 'r', encoding='utf-8') as f:
                    self.scores = json.load(f)
        except Exception as e:
            print(f"Lỗi khi load điểm số: {e}")
            self.scores = {"X": 0, "O": 0, "Draw": 0}
    
    def run(self):
        """Chạy ứng dụng"""
        self.window.mainloop()

def main():
    """Hàm chính"""
    try:
        game = TicTacToe()
        game.run()
    except Exception as e:
        print(f"Lỗi: {e}")
        messagebox.showerror("Lỗi", f"Có lỗi xảy ra: {e}")

if __name__ == "__main__":
    main() 