import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Simple Calculator")
        self.geometry("400x400")

        self.result_var = tk.StringVar()
        self.result_var.set("0")

        self.create_widgets()

    def create_widgets(self):
        # Result display
        result_entry = tk.Entry(self, textvariable=self.result_var, font=("Arial", 24), bd=20, justify="right")
        result_entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

        # Number buttons
        button_font = ("Arial", 14)
        button_bg = "#ccc"
        button_active_bg = "#aaa"
        buttons = [
            '7', '8', '9',
            '4', '5', '6',
            '1', '2', '3',
            'Clear', '0', 'Delete'
        ]
        row_val = 1
        col_val = 0
        for button in buttons:
            action = lambda x=button: self.on_button_click(x)
            tk.Button(self, text=button, font=button_font, bg=button_bg, activebackground=button_active_bg, command=action).grid(row=row_val, column=col_val, sticky="nsew")
            col_val += 1
            if col_val > 2:
                col_val = 0
                row_val += 1

        # Operator buttons
        operators = ['+', '-', '*', '/', '=']
        for i, operator in enumerate(operators):
            action = lambda x=operator: self.on_operator_button_click(x)
            tk.Button(self, text=operator, font=button_font, bg=button_bg, activebackground=button_active_bg, command=action).grid(row=i+1, column=3, sticky="nsew")

        # Configure rows and columns to resize with window
        for i in range(5):
            self.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == 'Clear':
            self.result_var.set("0")
        elif char == 'Delete':
            current_result = self.result_var.get()
            if len(current_result) > 1:
                self.result_var.set(current_result[:-1])
            else:
                self.result_var.set("0")
        else:
            current_result = self.result_var.get()
            if current_result == "0" or current_result[-1] in "+-*/":
                self.result_var.set(char)
            else:
                self.result_var.set(current_result + char)

    def on_operator_button_click(self, operator):
        if operator == "=":
            self.on_equal_button_click()
        else:
            current_result = self.result_var.get()
            if current_result[-1] in "+-*/":
                self.result_var.set(current_result[:-1] + operator)
            else:
                self.result_var.set(current_result + operator)

    def on_equal_button_click(self):
        try:
            result = eval(self.result_var.get())
            self.result_var.set(str(result))
        except ZeroDivisionError:
            self.result_var.set("Error")
        except Exception as e:
            self.result_var.set("Error")

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
