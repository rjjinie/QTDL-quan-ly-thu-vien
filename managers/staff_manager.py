import tkinter as tk
from tkinter import ttk
import mysql.connector

class StaffApp(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_staff_list(self)
        self.create_staff_info(self)

    def create_staff_list(self, parent):
        title = tk.Label(parent, text="QUẢN LÝ NHÂN VIÊN", font=("Arial", 16, "bold"), fg="green", bg="white")
        title.pack(pady=10)

        # Frame chứa bảng danh sách
        list_frame = tk.Frame(parent)
        list_frame.pack(side="left", padx=20)

        # Tạo bảng Nhân viên
        columns = ("Mã NV", "Tên NV", "Ngày sinh", "Số điện thoại")
        self.staff_table = ttk.Treeview(list_frame, columns=columns, show="headings", height=10)

        # Cấu hình tiêu đề và độ rộng cột
        for col in columns:
            self.staff_table.heading(col, text=col)
            self.staff_table.column(col, anchor="center", width=150)

        # Nạp dữ liệu từ MySQL
        self.load_staff_data()

        self.staff_table.pack(side="left", fill="both")

        # Thêm thanh cuộn dọc cho bảng
        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.staff_table.yview)
        self.staff_table.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        self.staff_table.bind('<<TreeviewSelect>>', self.on_staff_select)

    def load_staff_data(self):
        """Nạp dữ liệu nhân viên từ MySQL."""
        try:
            connection = mysql.connector.connect(
                host='localhost',      
                user='root',          
                password='hyun', 
                database='qlthuvien'  
            )

            cursor = connection.cursor()
            cursor.execute("SELECT MaNV, TenNV, NgaySinh, SDT FROM NhanVien")

            for (staff_id, staff_name, birthdate, phone) in cursor:
                self.staff_table.insert('', 'end', values=(staff_id, staff_name, birthdate, phone))

        except mysql.connector.Error as err:
            print(f"Lỗi khi kết nối MySQL: {err}")
        finally:
            if connection:
                cursor.close()
                connection.close()

    def on_staff_select(self, event):
        """Xử lý sự kiện khi chọn một nhân viên trong bảng."""
        selected_item = self.staff_table.selection()
        if selected_item:
            staff_data = self.staff_table.item(selected_item, 'values')
            self.staff_code_entry.delete(0, tk.END)
            self.staff_code_entry.insert(0, staff_data[0])
            self.staff_name_entry.delete(0, tk.END)
            self.staff_name_entry.insert(0, staff_data[1])
            self.birthdate_entry.delete(0, tk.END)
            self.birthdate_entry.insert(0, staff_data[2])
            self.phone_entry.delete(0, tk.END)
            self.phone_entry.insert(0, staff_data[3])

    def create_staff_info(self, parent):
        info_frame = tk.Frame(parent)
        info_frame.pack(side="right", padx=20, pady=10)

        info_label = tk.Label(info_frame, text="THÔNG TIN NHÂN VIÊN", font=("Arial", 12, "bold"))
        info_label.grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(info_frame, text="Mã NV:").grid(row=1, column=0, sticky="e")
        self.staff_code_entry = tk.Entry(info_frame)
        self.staff_code_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(info_frame, text="Tên NV:").grid(row=2, column=0, sticky="e")
        self.staff_name_entry = tk.Entry(info_frame)
        self.staff_name_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(info_frame, text="Ngày sinh:").grid(row=3, column=0, sticky="e")
        self.birthdate_entry = tk.Entry(info_frame)
        self.birthdate_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(info_frame, text="Số điện thoại:").grid(row=4, column=0, sticky="e")
        self.phone_entry = tk.Entry(info_frame)
        self.phone_entry.grid(row=4, column=1, padx=10, pady=5)

        # Nút chức năng
        btn_frame = tk.Frame(info_frame)
        btn_frame.grid(row=5, column=0, columnspan=2, pady=10)

        add_button = tk.Button(btn_frame, text="THÊM", width=8, command=self.add_staff)
        add_button.grid(row=0, column=0, padx=5)

        save_button = tk.Button(btn_frame, text="LƯU", width=8, command=self.update_staff)
        save_button.grid(row=0, column=1, padx=5)

        delete_button = tk.Button(btn_frame, text="XÓA", width=8, command=self.delete_staff)
        delete_button.grid(row=0, column=2, padx=5)

        reset_button = tk.Button(btn_frame, text="RESET", width=8, command=self.reset_entries)
        reset_button.grid(row=0, column=3, padx=5)

        # Phần tìm kiếm
        search_label = tk.Label(info_frame, text="TÌM KIẾM", font=("Arial", 12, "bold"))
        search_label.grid(row=6, column=0, columnspan=2, pady=10)

        tk.Label(info_frame, text="Tên NV:").grid(row=7, column=0, sticky="e")
        self.search_name_entry = tk.Entry(info_frame)
        self.search_name_entry.grid(row=7, column=1, padx=10, pady=5)

        search_button = tk.Button(info_frame, text="TÌM KIẾM", width=10, command=self.search_staff)
        search_button.grid(row=8, column=0, columnspan=2, pady=5)

        cancel_button = tk.Button(info_frame, text="HỦY TÌM KIẾM", width=10, command=self.reset_search)
        cancel_button.grid(row=9, column=0, columnspan=2, pady=5)

    def add_staff(self):
        """Thêm nhân viên mới vào cơ sở dữ liệu."""
        staff_id = self.staff_code_entry.get()
        staff_name = self.staff_name_entry.get()
        birthdate = self.birthdate_entry.get()
        phone = self.phone_entry.get()
        
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='hyun',
                database='qlthuvien'
            )
            cursor = connection.cursor()
            cursor.execute("INSERT INTO NhanVien (MaNV, TenNV, NgaySinh, SDT) VALUES (%s, %s, %s, %s)", 
                           (staff_id, staff_name, birthdate, phone))
            connection.commit()
            self.staff_table.insert('', 'end', values=(staff_id, staff_name, birthdate, phone))
            self.reset_entries()
        except mysql.connector.Error as err:
            print(f"Lỗi khi thêm nhân viên: {err}")
        finally:
            if connection:
                cursor.close()
                connection.close()

    def update_staff(self):
        """Cập nhật thông tin nhân viên đã chọn."""
        selected_item = self.staff_table.selection()
        if not selected_item:
            return  # Không có nhân viên nào được chọn

        staff_id = self.staff_code_entry.get()
        staff_name = self.staff_name_entry.get()
        birthdate = self.birthdate_entry.get()
        phone = self.phone_entry.get()

        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='hyun',
                database='qlthuvien'
            )
            cursor = connection.cursor()
            cursor.execute("UPDATE NhanVien SET TenNV=%s, NgaySinh=%s, SDT=%s WHERE MaNV=%s", 
                           (staff_name, birthdate, phone, staff_id))
            connection.commit()

            # Cập nhật dữ liệu trong bảng hiển thị
            self.load_staff_data()
            self.reset_entries()
        except mysql.connector.Error as err:
            print(f"Lỗi khi cập nhật nhân viên: {err}")
        finally:
            if connection:
                cursor.close()
                connection.close()

    def delete_staff(self):
        """Xóa nhân viên đã chọn khỏi cơ sở dữ liệu."""
        selected_item = self.staff_table.selection()
        if not selected_item:
            return  # Không có nhân viên nào được chọn

        staff_id = self.staff_table.item(selected_item, 'values')[0]

        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='hyun',
                database='qlthuvien'
            )
            cursor = connection.cursor()
            cursor.execute("DELETE FROM NhanVien WHERE MaNV=%s", (staff_id,))
            connection.commit()

            # Cập nhật dữ liệu trong bảng hiển thị
            self.staff_table.delete(selected_item)
            self.reset_entries()
        except mysql.connector.Error as err:
            print(f"Lỗi khi xóa nhân viên: {err}")
        finally:
            if connection:
                cursor.close()
                connection.close()

    def reset_entries(self):
        """Đặt lại các trường nhập liệu."""
        self.staff_code_entry.delete(0, tk.END)
        self.staff_name_entry.delete(0, tk.END)
        self.birthdate_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)

    def search_staff(self):
        """Tìm kiếm nhân viên theo tên."""
        search_name = self.search_name_entry.get()
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='hyun',
                database='qlthuvien'
            )
            cursor = connection.cursor()
            cursor.execute("SELECT MaNV, TenNV, NgaySinh, SDT FROM NhanVien WHERE TenNV LIKE %s", 
                           ('%' + search_name + '%',))

            self.staff_table.delete(*self.staff_table.get_children())  # Xóa dữ liệu hiện có
            for (staff_id, staff_name, birthdate, phone) in cursor:
                self.staff_table.insert('', 'end', values=(staff_id, staff_name, birthdate, phone))

        except mysql.connector.Error as err:
            print(f"Lỗi khi tìm kiếm nhân viên: {err}")
        finally:
            if connection:
                cursor.close()
                connection.close()

    def reset_search(self):
        """Đặt lại tìm kiếm và nạp lại dữ liệu."""
        self.search_name_entry.delete(0, tk.END)
        self.load_staff_data()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Quản lý Nhân Viên")
    app = StaffApp(root)
    app.pack(fill="both", expand=True)
    root.mainloop()
