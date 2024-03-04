import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Gelişmiş Hesap Makinesi")
        self.master.configure(bg='light gray')
        self.current_input = ""
        self.create_widgets()

    def create_widgets(self):
        self.entry = tk.Entry(self.master, width=35, borderwidth=5, font=('Arial', 14))
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Buton renkleri ve yazı tipi
        button_color = "#ffffff"
        operator_color = "#ffcc5c"
        clear_color = "#ff6f69"
        equals_color = "#ffeead"
        special_color = "#88d8b0" 
        font = ('Arial', 14)

        buttons = [
            ('7', 1, 0, button_color), ('8', 1, 1, button_color), ('9', 1, 2, button_color),
            ('4', 2, 0, button_color), ('5', 2, 1, button_color), ('6', 2, 2, button_color),
            ('1', 3, 0, button_color), ('2', 3, 1, button_color), ('3', 3, 2, button_color), ('0', 4, 1, button_color),
            ('+', 1, 3, operator_color), ('-', 2, 3, operator_color), ('*', 3, 3, operator_color), ('/', 4, 3, operator_color),
            ('%', 5, 0, special_color), ('C', 4, 0, clear_color), ('=', 4, 2, equals_color), ('Del', 5, 1, clear_color),
            (',', 5, 2, special_color),
        ]

        for (text, row, col, bg) in buttons:
            self.add_button(text, row, col, bg, font)

        self.master.bind("<Key>", self.key_input)  # Klavye girişini yakala

    def add_button(self, text, row, col, bg, font):
        button = tk.Button(self.master, text=text, width=9, height=3, bg=bg, font=font,
                           command=lambda: self.button_click(text))
        button.grid(row=row, column=col)

    def button_click(self, value):
        if value == "=":
            try:
                # Küsuratlı sayıları ve yüzde işlemlerini hesapla
                result = str(eval(self.current_input.replace(',', '.')))
                self.entry.delete(0, tk.END)
                self.entry.insert(0, result)
                self.current_input = result
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Hata")
        elif value == "C":
            self.current_input = ""
            self.entry.delete(0, tk.END)
        elif value == "Del":
            self.current_input = self.current_input[:-1]
            self.entry.delete(0, tk.END)
            self.entry.insert(0, self.current_input)
        elif value == "%":
            try:
                # Yüzde işlemi için mevcut girişi 100'e böl
                self.current_input = str(eval(self.current_input) / 100)
                self.entry.delete(0, tk.END)
                self.entry.insert(0, self.current_input)
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Hata")
        elif value == ",":
            # Küsuratlı sayılar için virgül ekle
            if "," not in self.current_input:
                self.current_input += "."
                self.entry.delete(0, tk.END)
                self.entry.insert(0, self.current_input.replace('.', ','))
        else:
            self.current_input += str(value)
            self.entry.delete(0, tk.END)
            self.entry.insert(0, self.current_input.replace('.', ','))

    def key_input(self, event):
        if event.char in '0123456789+-*/':
            self.button_click(event.char)
        elif event.char == '%':
            self.button_click('%')
        elif event.char == '.' or event.char == ',':
            self.button_click(',')
        elif event.keysym == "Return":
            self.button_click("=")
        elif event.keysym == "Escape":
            self.button_click("C")
        elif event.keysym == "BackSpace":
            self.button_click("Del")

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
