import tkinter as tk
from tkinter import messagebox

class BookManagement(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Quản lý Sách", font=("Helvetica", 16))
        label.pack(pady=10)

        button = tk.Button(self, text="Trở về Trang chính",
                           command=lambda: controller.show_frame("MainPage"))
        button.pack()

        # Các chức năng thêm, sửa, xóa sách
        add_button = tk.Button(self, text="Thêm Sách", command=self.add_book)
        add_button.pack(pady=5)

        edit_button = tk.Button(self, text="Sửa Sách", command=self.edit_book)
        edit_button.pack(pady=5)

        delete_button = tk.Button(self, text="Xóa Sách", command=self.delete_book)
        delete_button.pack(pady=5)

    def add_book(self):
        messagebox.showinfo("Thêm", "Thêm Sách")

    def edit_book(self):
        messagebox.showinfo("Sửa", "Sửa Sách")

    def delete_book(self):
        messagebox.showinfo("Xóa", "Xóa Sách")
