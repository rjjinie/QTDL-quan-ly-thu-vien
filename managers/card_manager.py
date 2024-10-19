import tkinter as tk
from tkinter import ttk
import mysql.connector
from datetime import datetime

class CardApp(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_card_list(self)
        self.create_card_info(self)

    def create_card_list(self, parent):
        title = tk.Label(parent, text="QUẢN LÝ THẺ THƯ VIỆN", font=("Arial", 16, "bold"), fg="blue", bg="white")
        title.pack(pady=10)

        # Frame chứa bảng danh sách
        list_frame = tk.Frame(parent)
        list_frame.pack(side="left", padx=20)

        # Tạo bảng Thẻ thư viện
        columns = ("Số thẻ", "Ngày bắt đầu", "Ngày hết hạn", "Ghi chú")
        self.card_table = ttk.Treeview(list_frame, columns=columns, show="headings", height=10)

        # Cấu hình tiêu đề và độ rộng cột
        for col in columns:
            self.card_table.heading(col, text=col)
            self.card_table.column(col, anchor="center", width=150)

        # Nạp dữ liệu từ MySQL
        self.load_card_data()

        self.card_table.pack(side="left", fill="both")

        # Thêm thanh cuộn dọc cho bảng
        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.card_table.yview)
        self.card_table.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        self.card_table.bind('<<TreeviewSelect>>', self.on_card_select)

    def load_card_data(self):
        """Nạp dữ liệu thẻ thư viện từ MySQL."""
        try:
            connection = mysql.connector.connect(
                host='localhost',      
                user='root',          
                password='hyun', 
                database='qlthuvien'  
            )

            cursor = connection.cursor()
            cursor.execute("SELECT SoThe, NgayBatDau, NgayHetHan, GhiChu FROM TheThuVien")

            for (card_id, start_date, end_date, note) in cursor:
                self.card_table.insert('', 'end', values=(card_id, start_date, end_date, note))

        except mysql.connector.Error as err:
            print(f"Lỗi khi kết nối MySQL: {err}")
        finally:
            if connection:
                cursor.close()
                connection.close()

    def on_card_select(self, event):
        """Xử lý sự kiện khi chọn một thẻ trong bảng."""
        selected_item = self.card_table.selection()
        if selected_item:
            card_data = self.card_table.item(selected_item, 'values')
            self.card_id_entry.delete(0, tk.END)
            self.card_id_entry.insert(0, card_data[0])
            self.start_date_entry.delete(0, tk.END)
            self.start_date_entry.insert(0, card_data[1])
            self.end_date_entry.delete(0, tk.END)
            self.end_date_entry.insert(0, card_data[2])
            self.note_entry.delete(0, tk.END)
            self.note_entry.insert(0, card_data[3])

    def create_card_info(self, parent):
        info_frame = tk.Frame(parent)
        info_frame.pack(side="right", padx=20, pady=10)

        info_label = tk.Label(info_frame, text="THÔNG TIN THẺ THƯ VIỆN", font=("Arial", 12, "bold"))
        info_label.grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(info_frame, text="Số thẻ:").grid(row=1, column=0, sticky="e")
        self.card_id_entry = tk.Entry(info_frame)
        self.card_id_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(info_frame, text="Ngày bắt đầu (YYYY-MM-DD):").grid(row=2, column=0, sticky="e")
        self.start_date_entry = tk.Entry(info_frame)
        self.start_date_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(info_frame, text="Ngày hết hạn (YYYY-MM-DD):").grid(row=3, column=0, sticky="e")
        self.end_date_entry = tk.Entry(info_frame)
        self.end_date_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(info_frame, text="Ghi chú:").grid(row=4, column=0, sticky="e")
        self.note_entry = tk.Entry(info_frame)
        self.note_entry.grid(row=4, column=1, padx=10, pady=5)

        # Nút chức năng
        btn_frame = tk.Frame(info_frame)
        btn_frame.grid(row=5, column=0, columnspan=2, pady=10)

        add_button = tk.Button(btn_frame, text="THÊM", width=8, command=self.add_card)
        add_button.grid(row=0, column=0, padx=5)

        save_button = tk.Button(btn_frame, text="LƯU", width=8, command=self.update_card)
        save_button.grid(row=0, column=1, padx=5)

        delete_button = tk.Button(btn_frame, text="XÓA", width=8, command=self.delete_card)
        delete_button.grid(row=0, column=2, padx=5)

        reset_button = tk.Button(btn_frame, text="RESET", width=8, command=self.reset_entries)
        reset_button.grid(row=0, column=3, padx=5)

        # Phần tìm kiếm
        search_label = tk.Label(info_frame, text="TÌM KIẾM", font=("Arial", 12, "bold"))
        search_label.grid(row=6, column=0, columnspan=2, pady=10)

        tk.Label(info_frame, text="Số thẻ:").grid(row=7, column=0, sticky="e")
        self.search_card_entry = tk.Entry(info_frame)
        self.search_card_entry.grid(row=7, column=1, padx=10, pady=5)

        search_button = tk.Button(info_frame, text="TÌM KIẾM", width=10, command=self.search_card)
        search_button.grid(row=8, column=0, columnspan=2, pady=5)

        cancel_button = tk.Button(info_frame, text="HỦY TÌM KIẾM", width=10, command=self.reset_search)
        cancel_button.grid(row=9, column=0, columnspan=2, pady=5)

    def add_card(self):
        """Thêm thẻ mới vào cơ sở dữ liệu."""
        card_id = self.card_id_entry.get()
        start_date = self.start_date_entry.get()
        end_date = self.end_date_entry.get()
        note = self.note_entry.get()

        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='hyun',
                database='qlthuvien'
            )
            cursor = connection.cursor()
            cursor.execute("INSERT INTO TheThuVien (SoThe, NgayBatDau, NgayHetHan, GhiChu) VALUES (%s, %s, %s, %s)", 
                           (card_id, start_date, end_date, note))
            connection.commit()
            self.card_table.insert('', 'end', values=(card_id, start_date, end_date, note))
            self.reset_entries()
        except mysql.connector.Error as err:
            print(f"Lỗi khi thêm thẻ: {err}")
        finally:
            if connection:
                cursor.close()
                connection.close()

    def update_card(self):
        """Cập nhật thông tin thẻ đã chọn."""
        selected_item = self.card_table.selection()
        if not selected_item:
            return  # Không có thẻ nào được chọn

        card_id = self.card_id_entry.get()
        start_date = self.start_date_entry.get()
        end_date = self.end_date_entry.get()
        note = self.note_entry.get()

        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='hyun',
                database='qlthuvien'
            )
            cursor = connection.cursor()
            cursor.execute("UPDATE TheThuVien SET NgayBatDau=%s, NgayHetHan=%s, GhiChu=%s WHERE SoThe=%s", 
                           (start_date, end_date, note, card_id))
            connection.commit()

            # Cập nhật dữ liệu trong bảng hiển thị
            self.load_card_data()
            self.reset_entries()
        except mysql.connector.Error as err:
            print(f"Lỗi khi cập nhật thẻ: {err}")
        finally:
            if connection:
                cursor.close()
                connection.close()

    def delete_card(self):
        """Xóa thẻ đã chọn khỏi cơ sở dữ liệu."""
        selected_item = self.card_table.selection()
        if not selected_item:
            return  # Không có thẻ nào được chọn

        card_id = self.card_table.item(selected_item, 'values')[0]

        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='hyun',
                database='qlthuvien'
            )
            cursor = connection.cursor()
            cursor.execute("DELETE FROM TheThuVien WHERE SoThe=%s", (card_id,))
            connection.commit()

            # Cập nhật dữ liệu trong bảng hiển thị
            self.card_table.delete(selected_item)
            self.reset_entries()
        except mysql.connector.Error as err:
            print(f"Lỗi khi xóa thẻ: {err}")
        finally:
            if connection:
                cursor.close()
                connection.close()

    def reset_entries(self):
        """Đặt lại các trường nhập liệu."""
        self.card_id_entry.delete(0, tk.END)
        self.start_date_entry.delete(0, tk.END)
        self.end_date_entry.delete(0, tk.END)
        self.note_entry.delete(0, tk.END)

    def search_card(self):
        """Tìm kiếm thẻ theo số thẻ."""
        search_card_id = self.search_card_entry.get()
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='hyun',
                database='qlthuvien'
            )
            cursor = connection.cursor()
            cursor.execute("SELECT SoThe, NgayBatDau, NgayHetHan, GhiChu FROM TheThuVien WHERE SoThe LIKE %s", 
                           ('%' + search_card_id + '%',))

            self.card_table.delete(*self.card_table.get_children())  # Xóa dữ liệu hiện có
            for (card_id, start_date, end_date, note) in cursor:
                self.card_table.insert('', 'end', values=(card_id, start_date, end_date, note))

        except mysql.connector.Error as err:
            print(f"Lỗi khi tìm kiếm thẻ: {err}")
        finally:
            if connection:
                cursor.close()
                connection.close()

    def reset_search(self):
        """Đặt lại tìm kiếm và nạp lại dữ liệu."""
        self.search_card_entry.delete(0, tk.END)
        self.load_card_data()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Quản lý Thẻ Thư Viện")
    app = CardApp(root)
    app.pack(fill="both", expand=True)
    root.mainloop()