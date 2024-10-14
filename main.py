# import tkinter as tk
# from managers.author_manager import AuthorApp
# from managers.book_manager import BookApp

# class MainApp(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Hệ thống quản lý thư viện")
#         self.geometry("1000x600")

#         # Tạo frame menu bên trái
#         self.create_left_menu()

#         # Tạo frame chính để chứa các ứng dụng
#         self.main_frame = tk.Frame(self)
#         self.main_frame.pack(side="right", fill="both", expand=True)

#         # Lưu trữ các frame của các ứng dụng con
#         self.frames = {}

#     def create_left_menu(self):
#         left_menu = tk.Frame(self, bg="#4ABAF7", width=200)
#         left_menu.pack(side="left", fill="y")

#         menu_options = [
#             ("Quản lý Sách", self.show_book_app),
#             ("Quản lý Tác giả", self.show_author_app),
#         ]

#         for label, command in menu_options:
#             btn = tk.Button(left_menu, text=label, anchor="w", font=("Arial", 12), bg="#4ABAF7", fg="white", bd=0, command=command)
#             btn.pack(fill="x", padx=10, pady=10)

#     def show_frame(self, frame_class):
#         """Hàm này sẽ tạo và hiển thị frame của ứng dụng được chọn"""
#         if frame_class not in self.frames:
#             frame = frame_class(self.main_frame)
#             self.frames[frame_class] = frame
#             frame.pack(fill="both", expand=True)

#         # Ẩn tất cả các frame
#         for frame in self.frames.values():
#             frame.pack_forget()

#         # Hiển thị frame hiện tại
#         self.frames[frame_class].pack(fill="both", expand=True)

#     def show_author_app(self):
#         self.show_frame(AuthorApp)

#     def show_book_app(self):
#         self.show_frame(BookApp)

# if __name__ == "__main__":
#     app = MainApp()
#     app.mainloop()



import tkinter as tk
from managers.author_manager import AuthorApp
from managers.book_manager import BookApp

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quản lý Thư viện")
        self.geometry("800x600")

        # Khởi tạo AuthorApp và BookApp
        self.author_app = AuthorApp(self)
        self.book_app = BookApp(self)

        # Hiển thị AuthorApp mặc định
        self.author_app.pack(fill="both", expand=True)

        # Nút để chuyển đổi giữa AuthorApp và BookApp
        switch_frame = tk.Frame(self)
        switch_frame.pack(side="bottom", pady=10)

        btn_author = tk.Button(switch_frame, text="Quản lý Tác giả", command=self.show_author_app)
        btn_author.pack(side="left", padx=5)

        btn_book = tk.Button(switch_frame, text="Quản lý Sách", command=self.show_book_app)
        btn_book.pack(side="left", padx=5)

    def show_author_app(self):
        self.book_app.pack_forget()  # Ẩn BookApp
        self.author_app.pack(fill="both", expand=True)  # Hiển thị AuthorApp

    def show_book_app(self):
        self.author_app.pack_forget()  # Ẩn AuthorApp
        self.book_app.pack(fill="both", expand=True)  # Hiển thị BookApp

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
