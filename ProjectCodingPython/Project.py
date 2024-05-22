import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ttkbootstrap import Style

class ShoppingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Belanja")
        self.root.geometry("400x300")

        self.style = Style(theme="flatly")

        self.shopping_list = []

        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(padx=10, pady=10, fill="both", expand=True)

        name_label = ttk.Label(self.main_frame, text="Nama Barang:")
        name_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.name_entry = ttk.Entry(self.main_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        price_label = ttk.Label(self.main_frame, text="Harga per Item:")
        price_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.price_entry = ttk.Entry(self.main_frame)
        self.price_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        quantity_label = ttk.Label(self.main_frame, text="Jumlah Barang:")
        quantity_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.quantity_entry = ttk.Entry(self.main_frame)
        self.quantity_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        add_button = ttk.Button(self.main_frame, text="Tambah", command=self.add_item)
        add_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10, sticky="we")

        self.shopping_listbox = tk.Listbox(self.main_frame)
        self.shopping_listbox.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

        self.total_label = ttk.Label(self.main_frame, text="Total Biaya: Rp 0")
        self.total_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="w")

        remove_button = ttk.Button(self.main_frame, text="Hapus", command=self.remove_item)
        remove_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky="we")

    def add_item(self):
        name = self.name_entry.get()
        price = float(self.price_entry.get())
        quantity = int(self.quantity_entry.get())

        total_price = price * quantity

        self.shopping_list.append((name, price, quantity, total_price))
        self.refresh_shopping_listbox()
        self.calculate_total()

        self.name_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)

    def remove_item(self):
        selected_index = self.shopping_listbox.curselection()
        if selected_index:
            self.shopping_list.pop(selected_index[0])
            self.refresh_shopping_listbox()
            self.calculate_total()

    def refresh_shopping_listbox(self):
        self.shopping_listbox.delete(0, tk.END)
        for item in self.shopping_list:
            self.shopping_listbox.insert(tk.END, f"{item[0]} - Rp {item[1]:.2f} x {item[2]} = Rp {item[3]:.2f}")

    def calculate_total(self):
        total = sum(item[3] for item in self.shopping_list)
        self.total_label.config(text=f"Total Biaya: Rp {total:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ShoppingApp(root)
    root.mainloop()
