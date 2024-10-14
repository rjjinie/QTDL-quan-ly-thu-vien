import tkinter as tk
from tkinter import messagebox

class AuthorManagement(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Quản lý Tác giả", font=("Helvetica", 16))
        label.pack(pady=10)

        button = tk.Button(self, text="Trở về Trang chính",
                           command=lambda: controller.show_frame("MainPage"))
        button.pack()

        # Các chức năng thêm, sửa, xóa tác giả
        add_button = tk.Button(self, text="Thêm Tác giả", command=self.add_author)
        add_button.pack(pady=5)

        edit_button = tk.Button(self, text="Sửa Tác giả", command=self.edit_author)
        edit_button.pack(pady=5)

        delete_button = tk.Button(self, text="Xóa Tác giả", command=self.delete_author)
        delete_button.pack(pady=5)

    def add_author(self):
        messagebox.showinfo("Thêm", "Thêm Tác giả")

    def edit_author(self):
        messagebox.showinfo("Sửa", "Sửa Tác giả")

    def delete_author(self):
        messagebox.showinfo("Xóa", "Xóa Tác giả")
