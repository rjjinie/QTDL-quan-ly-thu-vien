import tkinter as tk
from managers.author_manager import AuthorApp
from managers.book_manager import BookApp
from managers.card_manager import CardApp
from managers.staff_manager import StaffApp

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quản lý Thư viện")
        self.geometry("800x600")

        # Tạo sidebar
        self.sidebar_frame = tk.Frame(self, bg="#2C3E50", width=200)
        self.sidebar_frame.pack(side="left", fill="y")

        # Nút trong sidebar
        btn_book = tk.Button(self.sidebar_frame, text="Quản lý Sách", command=self.show_book_app, bg="#34495E", fg="white", font=("Arial", 12), pady=10)
        btn_book.pack(fill="x")

        btn_author = tk.Button(self.sidebar_frame, text="Quản lý Tác giả", command=self.show_author_app, bg="#34495E", fg="white", font=("Arial", 12), pady=10)
        btn_author.pack(fill="x")

        btn_card = tk.Button(self.sidebar_frame, text="Quản lý Thẻ", command=self.show_card_app, bg="#34495E", fg="white", font=("Arial", 12), pady=10)
        btn_card.pack(fill="x")

        btn_staff = tk.Button(self.sidebar_frame, text="Quản lý Nhân viên", command=self.show_staff_app, bg="#34495E", fg="white", font=("Arial", 12), pady=10)
        btn_staff.pack(fill="x")

        self.content_frame = tk.Frame(self)
        self.content_frame.pack(side="right", fill="both", expand=True)

        self.author_app = AuthorApp(self.content_frame)
        self.book_app = BookApp(self.content_frame)
        self.card_app = CardApp(self.content_frame)
        self.staff_app = StaffApp(self.content_frame)

        # Hiển thị BookApp mặc định
        self.book_app.pack(fill="both", expand=True)

    def show_author_app(self):
        self.hide_all_apps()
        self.author_app.pack(fill="both", expand=True)  # Hiển thị AuthorApp

    def show_book_app(self):
        self.hide_all_apps()
        self.book_app.pack(fill="both", expand=True)  # Hiển thị BookApp

    def show_card_app(self):
        self.hide_all_apps()
        self.card_app.pack(fill="both", expand=True)  # Hiển thị CardApp

    def show_staff_app(self):
        self.hide_all_apps()
        self.staff_app.pack(fill="both", expand=True)  # Hiển thị StaffApp

    def hide_all_apps(self):
        # Ẩn tất cả các app trước khi hiển thị app mới
        self.author_app.pack_forget()
        self.book_app.pack_forget()
        self.card_app.pack_forget()
        self.staff_app.pack_forget()

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
