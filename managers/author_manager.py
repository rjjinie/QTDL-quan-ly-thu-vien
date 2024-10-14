import tkinter as tk
from tkinter import ttk

class AuthorApp(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_author_list(self)
        self.create_author_info(self)

    def create_author_list(self, parent):
        title = tk.Label(parent, text="QUẢN LÝ TÁC GIẢ", font=("Arial", 16, "bold"), fg="green", bg="white")
        title.pack(pady=10)

        # Frame chứa bảng danh sách
        list_frame = tk.Frame(parent)
        list_frame.pack(side="left", padx=20)

        # Tạo bảng Tác giả
        columns = ("Mã tác giả", "Tên tác giả", "Website", "Ghi chú")
        self.author_table = ttk.Treeview(list_frame, columns=columns, show="headings", height=10)

        # Cấu hình tiêu đề và độ rộng cột
        for col in columns:
            self.author_table.heading(col, text=col)
            self.author_table.column(col, anchor="center", width=150)

        # Thêm dữ liệu giả để hiển thị
        author_data = [
            ("TG001", "Nguyễn Nhật Ánh", "https://tacgia1.com", "Tác giả nổi tiếng"),
            ("TG002", "J.K. Rowling", "https://jkrowling.com", "Tác giả Harry Potter"),
            ("TG003", "Haruki Murakami", "https://murakami.com", "Tác giả văn học Nhật Bản"),
        ]

        # Thêm dữ liệu vào bảng
        for item in author_data:
            self.author_table.insert('', 'end', values=item)

        self.author_table.pack(side="left", fill="both")

        # Thêm thanh cuộn dọc cho bảng
        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.author_table.yview)
        self.author_table.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

    def create_author_info(self, parent):
        # Khung chứa form thêm thông tin và tìm kiếm
        info_frame = tk.Frame(parent)
        info_frame.pack(side="right", padx=20, pady=10)

        # Phần thông tin tác giả
        info_label = tk.Label(info_frame, text="THÔNG TIN TÁC GIẢ", font=("Arial", 12, "bold"))
        info_label.grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(info_frame, text="Mã tác giả:").grid(row=1, column=0, sticky="e")
        self.author_code_entry = tk.Entry(info_frame)
        self.author_code_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(info_frame, text="Tên tác giả:").grid(row=2, column=0, sticky="e")
        self.author_name_entry = tk.Entry(info_frame)
        self.author_name_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(info_frame, text="Website:").grid(row=3, column=0, sticky="e")
        self.website_entry = tk.Entry(info_frame)
        self.website_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(info_frame, text="Ghi chú:").grid(row=4, column=0, sticky="e")
        self.note_entry = tk.Entry(info_frame)
        self.note_entry.grid(row=4, column=1, padx=10, pady=5)

        # Nút chức năng
        btn_frame = tk.Frame(info_frame)
        btn_frame.grid(row=5, column=0, columnspan=2, pady=10)

        add_button = tk.Button(btn_frame, text="THÊM", width=8)
        add_button.grid(row=0, column=0, padx=5)

        save_button = tk.Button(btn_frame, text="LƯU", width=8)
        save_button.grid(row=0, column=1, padx=5)

        edit_button = tk.Button(btn_frame, text="SỬA", width=8)
        edit_button.grid(row=0, column=2, padx=5)

        delete_button = tk.Button(btn_frame, text="XÓA", width=8)
        delete_button.grid(row=0, column=3, padx=5)

        reset_button = tk.Button(btn_frame, text="RESET", width=8)
        reset_button.grid(row=0, column=4, padx=5)

        # Phần tìm kiếm
        search_label = tk.Label(info_frame, text="TÌM KIẾM", font=("Arial", 12, "bold"))
        search_label.grid(row=6, column=0, columnspan=2, pady=10)

        tk.Label(info_frame, text="Tên tác giả:").grid(row=7, column=0, sticky="e")
        self.search_name_entry = tk.Entry(info_frame)
        self.search_name_entry.grid(row=7, column=1, padx=10, pady=5)

        search_button = tk.Button(info_frame, text="TÌM KIẾM", width=10)
        search_button.grid(row=8, column=0, columnspan=2, pady=5)

        cancel_button = tk.Button(info_frame, text="HỦY TÌM KIẾM", width=10)
        cancel_button.grid(row=9, column=0, columnspan=2, pady=5)
