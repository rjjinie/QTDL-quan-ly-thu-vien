import tkinter as tk
from tkinter import messagebox
from managers.author_manager import AuthorManagement
from managers.book_manager import BookManagement

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quản lý Thư viện")
        self.geometry("400x300")

        # Tạo Menu Bar
        self.create_menu_bar()

        # Container để chứa các trang
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.frames = {}
        for F in (MainPage, AuthorManagement, BookManagement):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainPage")

    def create_menu_bar(self):
        # Tạo menu
        menu_bar = tk.Menu(self)

        # Tạo menu cho "Trang quản lý"
        manage_menu = tk.Menu(menu_bar, tearoff=0)
        manage_menu.add_command(label="Trang Chính", command=lambda: self.show_frame("MainPage"))
        manage_menu.add_command(label="Quản lý Tác giả", command=lambda: self.show_frame("AuthorManagement"))
        manage_menu.add_command(label="Quản lý Sách", command=lambda: self.show_frame("BookManagement"))

        # Thêm menu vào menu bar
        menu_bar.add_cascade(label="Trang quản lý", menu=manage_menu)

        # Đặt menu bar cho cửa sổ chính
        self.config(menu=menu_bar)

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Trang chính", font=("Helvetica", 16))
        label.pack(pady=10)

        button1 = tk.Button(self, text="Quản lý Tác giả",
                            command=lambda: controller.show_frame("AuthorManagement"))
        button1.pack(pady=5)

        button2 = tk.Button(self, text="Quản lý Sách",
                            command=lambda: controller.show_frame("BookManagement"))
        button2.pack(pady=5)

if __name__ == "__main__":
    app = App()
    app.mainloop()
