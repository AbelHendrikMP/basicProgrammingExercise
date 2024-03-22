import tkinter as tk
from tkinter import messagebox

class CosmeticItem:
    def __init__(self, name, cost_price):
        self.name = name
        self.cost_price = cost_price

    def calculate_selling_price(self, percentage):
        return self.cost_price * (1 + percentage / 100)

    def format_price(self, price):
        return "{:,.0f}".format(price).replace(",", ".")

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.history_text = tk.Text(self.master, height=10, width=70)
        self.history_text.pack()
        switch_theme_button = tk.Button(self, text="Switch Theme", command=self.switch_theme)
        switch_theme_button.pack()

    def create_widgets(self):
        self.master.title("WELCOME")
        self.dark_mode = True
        self.master.configure(bg='black')
        self.master.tk_setPalette(background='black', foreground='white')

        self.entries = []
        self.num_entries = 0

        add_entry_button = tk.Button(self, text="Add Entry", command=self.add_entry)
        add_entry_button.pack()

        remove_entry_button = tk.Button(self, text="Remove Entry", command=self.remove_entry)
        remove_entry_button.pack()


        calculate_button = tk.Button(self, text="Calculate Selling Prices", command=self.calculate_selling_prices)
        calculate_button.pack()

        save_button = tk.Button(self, text="Save Calculations", command=self.save_calculations)
        save_button.pack()

        percentage_info_label = tk.Label(self, text="Enter the percentage added to the price:", bg='black', fg='white')
        percentage_info_label.pack()

        self.percentage_entry = tk.Entry(self)
        self.percentage_entry.insert(0, "10")
        self.percentage_entry.pack()

    def add_entry(self):
        new_entry_frame = tk.Frame(self, bg='black')
        new_entry_frame.pack()

        name_label = tk.Label(new_entry_frame, text=f"Name of the cosmetic item {self.num_entries+1}:", bg='black', fg='white')
        name_label.grid(row=0, column=0)
        name_entry = tk.Entry(new_entry_frame)
        name_entry.grid(row=0, column=1)
        
        price_label = tk.Label(new_entry_frame, text=f"Cost price of the item {self.num_entries+1}:", bg='black', fg='white')
        price_label.grid(row=1, column=0)
        price_entry = tk.Entry(new_entry_frame)
        price_entry.grid(row=1, column=1)

        self.entries.append((name_entry, price_entry))
        self.num_entries += 1

    def remove_entry(self):
        if self.num_entries > 0:
            self.entries.pop()
            self.num_entries -= 1
            for widget in self.winfo_children():
                widget.destroy()
            self.create_widgets()

    def switch_theme(self):
        if self.dark_mode:
            self.master.configure(bg='white')
            self.master.tk_setPalette(background='white', foreground='black')
            self.dark_mode = False
        else:
            self.master.configure(bg='black')
            self.master.tk_setPalette(background='black', foreground='white')
            self.dark_mode = True

    def calculate_selling_prices(self):
        percentage = float(self.percentage_entry.get())
        
        calculations = []
        for name_entry, price_entry in self.entries:
            name = name_entry.get()
            cost_price = float(price_entry.get())
            item = CosmeticItem(name, cost_price)
            selling_price = item.calculate_selling_price(percentage)
            calculations.append(f"{name}: Cost Price - {item.format_price(cost_price)} | Selling Price - {item.format_price(selling_price)}")

        history_text = "\n".join(calculations)
        self.history_text.delete('1.0', tk.END)
        self.history_text.insert(tk.END, history_text)

    def save_calculations(self):
        with open("calculated_items.txt", "w") as file:
            for item in self.history_text.get("1.0", tk.END).splitlines():
                file.write(item + "\n")
        messagebox.showinfo("Save", "Calculations saved to calculated_items.txt")

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
