import tkinter as tk
from tkinter import ttk

class BookApp(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_book_list(self)
        self.create_book_info(self)

    def create_book_list(self, parent):
        title = tk.Label(parent, text="QUẢN LÝ SÁCH", font=("Arial", 16, "bold"), fg="orange", bg="white")
        title.pack(pady=10)

        # Frame chứa bảng danh sách
        list_frame = tk.Frame(parent)
        list_frame.pack(side="left", padx=20)

        # Tạo bảng Sách
        columns = ("Mã sách", "Tên sách", "Mã tác giả", "Mã thể loại", "Mã NXB", "Năm xuất bản")
        self.book_table = ttk.Treeview(list_frame, columns=columns, show="headings", height=15)

        # Cấu hình tiêu đề và độ rộng cột
        for col in columns:
            self.book_table.heading(col, text=col)
            self.book_table.column(col, anchor="center", width=120)

        # Thêm dữ liệu giả để hiển thị
        book_data = [
            ("B001", "Sách Toán", "TG001", "TL001", "NXB001", 2020),
            ("B002", "Sách Văn", "TG002", "TL002", "NXB002", 2019),
            ("B003", "Sách Lý", "TG003", "TL003", "NXB003", 2021),
            ("B004", "Sách Hóa", "TG004", "TL004", "NXB004", 2018),
            ("B005", "Sách Sinh", "TG005", "TL005", "NXB005", 2022),
        ]

        # Thêm dữ liệu vào bảng
        for item in book_data:
            self.book_table.insert('', 'end', values=item)

        self.book_table.pack(side="left", fill="both")

        # Thêm thanh cuộn dọc cho bảng
        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.book_table.yview)
        self.book_table.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

    def create_book_info(self, parent):
        # Khung chứa form thêm thông tin và tìm kiếm
        info_frame = tk.Frame(parent)
        info_frame.pack(side="right", padx=20, pady=10)

        # Phần thông tin sách
        info_label = tk.Label(info_frame, text="THÔNG TIN SÁCH", font=("Arial", 12, "bold"))
        info_label.grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(info_frame, text="Mã sách:").grid(row=1, column=0, sticky="e")
        self.book_code_entry = tk.Entry(info_frame)
        self.book_code_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(info_frame, text="Tên sách:").grid(row=2, column=0, sticky="e")
        self.book_name_entry = tk.Entry(info_frame)
        self.book_name_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(info_frame, text="Mã tác giả:").grid(row=3, column=0, sticky="e")
        self.author_code_entry = tk.Entry(info_frame)
        self.author_code_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(info_frame, text="Mã thể loại:").grid(row=4, column=0, sticky="e")
        self.category_code_entry = tk.Entry(info_frame)
        self.category_code_entry.grid(row=4, column=1, padx=10, pady=5)

        tk.Label(info_frame, text="Mã NXB:").grid(row=5, column=0, sticky="e")
        self.publisher_code_entry = tk.Entry(info_frame)
        self.publisher_code_entry.grid(row=5, column=1, padx=10, pady=5)

        tk.Label(info_frame, text="Năm xuất bản:").grid(row=6, column=0, sticky="e")
        self.publish_year_entry = tk.Entry(info_frame)
        self.publish_year_entry.grid(row=6, column=1, padx=10, pady=5)

        # Nút chức năng
        btn_frame = tk.Frame(info_frame)
        btn_frame.grid(row=7, column=0, columnspan=2, pady=10)

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
        search_label.grid(row=8, column=0, columnspan=2, pady=10)

        tk.Label(info_frame, text="Tên sách:").grid(row=9, column=0, sticky="e")
        self.search_name_entry = tk.Entry(info_frame)
        self.search_name_entry.grid(row=9, column=1, padx=10, pady=5)

        search_button = tk.Button(info_frame, text="TÌM KIẾM", width=10)
        search_button.grid(row=10, column=0, columnspan=2, pady=5)

        cancel_button = tk.Button(info_frame, text="HỦY TÌM KIẾM", width=10)
        cancel_button.grid(row=11, column=0, columnspan=2, pady=5)
