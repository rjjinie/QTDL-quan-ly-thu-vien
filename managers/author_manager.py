import tkinter as tk
from tkinter import ttk
import mysql.connector

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

        # Nạp dữ liệu từ MySQL
        self.load_author_data()

        self.author_table.pack(side="left", fill="both")

        # Thêm thanh cuộn dọc cho bảng
        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.author_table.yview)
        self.author_table.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        self.author_table.bind('<<TreeviewSelect>>', self.on_author_select)

    def load_author_data(self):
        """Nạp dữ liệu tác giả từ MySQL."""
        try:
            # Kết nối đến cơ sở dữ liệu MySQL
            connection = mysql.connector.connect(
                host='localhost',      
                user='root',          
                password='hyun', 
                database='qlthuvien'  
            )

            cursor = connection.cursor()
            cursor.execute("SELECT MaTG, tentg, website, ghichu FROM tacgia")

            for (author_id, author_name, website, note) in cursor:
                self.author_table.insert('', 'end', values=(author_id, author_name, website, note))

        except mysql.connector.Error as err:
            print(f"Lỗi khi kết nối MySQL: {err}")
        finally:
            if connection:
                cursor.close()
                connection.close()

    def on_author_select(self, event):
        """Xử lý sự kiện khi chọn một tác giả trong bảng."""
        selected_item = self.author_table.selection()
        if selected_item:
            author_data = self.author_table.item(selected_item, 'values')
            self.author_code_entry.delete(0, tk.END)
            self.author_code_entry.insert(0, author_data[0])
            self.author_name_entry.delete(0, tk.END)
            self.author_name_entry.insert(0, author_data[1])
            self.website_entry.delete(0, tk.END)
            self.website_entry.insert(0, author_data[2])
            self.note_entry.delete(0, tk.END)
            self.note_entry.insert(0, author_data[3])

    def create_author_info(self, parent):
        info_frame = tk.Frame(parent)
        info_frame.pack(side="right", padx=20, pady=10)

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

        add_button = tk.Button(btn_frame, text="THÊM", width=8, command=self.add_author)
        add_button.grid(row=0, column=0, padx=5)

        save_button = tk.Button(btn_frame, text="LƯU", width=8, command=self.update_author)
        save_button.grid(row=0, column=1, padx=5)

        delete_button = tk.Button(btn_frame, text="XÓA", width=8, command=self.delete_author)
        delete_button.grid(row=0, column=2, padx=5)

        reset_button = tk.Button(btn_frame, text="RESET", width=8, command=self.reset_entries)
        reset_button.grid(row=0, column=3, padx=5)

        # Phần tìm kiếm
        search_label = tk.Label(info_frame, text="TÌM KIẾM", font=("Arial", 12, "bold"))
        search_label.grid(row=6, column=0, columnspan=2, pady=10)

        tk.Label(info_frame, text="Tên tác giả:").grid(row=7, column=0, sticky="e")
        self.search_name_entry = tk.Entry(info_frame)
        self.search_name_entry.grid(row=7, column=1, padx=10, pady=5)

        search_button = tk.Button(info_frame, text="TÌM KIẾM", width=10, command=self.search_author)
        search_button.grid(row=8, column=0, columnspan=2, pady=5)

        cancel_button = tk.Button(info_frame, text="HỦY TÌM KIẾM", width=10, command=self.reset_search)
        cancel_button.grid(row=9, column=0, columnspan=2, pady=5)

    def add_author(self):
        """Thêm tác giả mới vào cơ sở dữ liệu."""
        author_id = self.author_code_entry.get()
        author_name = self.author_name_entry.get()
        website = self.website_entry.get()
        note = self.note_entry.get()
        
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='hyun',
                database='qlthuvien'
            )
            cursor = connection.cursor()
            cursor.execute("INSERT INTO tacgia (MaTG, tentg, website, ghichu) VALUES (%s, %s, %s, %s)", 
                           (author_id, author_name, website, note))
            connection.commit()
            self.author_table.insert('', 'end', values=(author_id, author_name, website, note))
            self.reset_entries()
        except mysql.connector.Error as err:
            print(f"Lỗi khi thêm tác giả: {err}")
        finally:
            if connection:
                cursor.close()
                connection.close()

    def update_author(self):
        """Cập nhật thông tin tác giả đã chọn."""
        selected_item = self.author_table.selection()
        if not selected_item:
            return  # Không có tác giả nào được chọn

        author_id = self.author_code_entry.get()
        author_name = self.author_name_entry.get()
        website = self.website_entry.get()
        note = self.note_entry.get()

        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='hyun',
                database='qlthuvien'
            )
            cursor = connection.cursor()
            cursor.execute("UPDATE tacgia SET tentg=%s, website=%s, ghichu=%s WHERE MaTG=%s", 
                           (author_name, website, note, author_id))
            connection.commit()

            # Cập nhật dữ liệu trong bảng hiển thị
            self.load_author_data()
            self.reset_entries()
        except mysql.connector.Error as err:
            print(f"Lỗi khi cập nhật tác giả: {err}")
        finally:
            if connection:
                cursor.close()
                connection.close()

    def delete_author(self):
        """Xóa tác giả đã chọn khỏi cơ sở dữ liệu."""
        selected_item = self.author_table.selection()
        if not selected_item:
            return  # Không có tác giả nào được chọn

        author_id = self.author_table.item(selected_item, 'values')[0]

        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='hyun',
                database='qlthuvien'
            )
            cursor = connection.cursor()
            cursor.execute("DELETE FROM tacgia WHERE MaTG=%s", (author_id,))
            connection.commit()

            # Cập nhật dữ liệu trong bảng hiển thị
            self.author_table.delete(selected_item)
            self.reset_entries()
        except mysql.connector.Error as err:
            print(f"Lỗi khi xóa tác giả: {err}")
        finally:
            if connection:
                cursor.close()
                connection.close()

    def reset_entries(self):
        """Đặt lại các trường nhập liệu."""
        self.author_code_entry.delete(0, tk.END)
        self.author_name_entry.delete(0, tk.END)
        self.website_entry.delete(0, tk.END)
        self.note_entry.delete(0, tk.END)

    def search_author(self):
        """Tìm kiếm tác giả theo tên."""
        search_name = self.search_name_entry.get()
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='hyun',
                database='qlthuvien'
            )
            cursor = connection.cursor()
            cursor.execute("SELECT MaTG, tentg, website, ghichu FROM tacgia WHERE tentg LIKE %s", 
                           ('%' + search_name + '%',))

            self.author_table.delete(*self.author_table.get_children())  # Xóa dữ liệu hiện có
            for (author_id, author_name, website, note) in cursor:
                self.author_table.insert('', 'end', values=(author_id, author_name, website, note))

        except mysql.connector.Error as err:
            print(f"Lỗi khi tìm kiếm tác giả: {err}")
        finally:
            if connection:
                cursor.close()
                connection.close()

    def reset_search(self):
        """Đặt lại tìm kiếm và nạp lại dữ liệu."""
        self.search_name_entry.delete(0, tk.END)
        self.load_author_data()