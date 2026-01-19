import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator App")
        self.root.geometry("300x400")
        
        self.display = tk.Entry(root, font=("Arial", 20), justify="right")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
        
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C',jk
        ]
        
        row = 1
        col = 0
        for button in buttons:
            if button == '=':
                tk.Button(root, text=button, font=("Arial", 18), command=self.calculate).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            elif button == 'C':
                tk.Button(root, text=button, font=("Arial", 18), command=self.clear).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            else:
                tk.Button(root, text=button, font=("Arial", 18), command=lambda b=button: self.append_to_display(b)).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        for i in range(5):
            root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)
        
        self.expression = ""
    
    def append_to_display(self, value):
        self.expression += str(value)
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)
    
    def calculate(self):
        try:
            result = eval(self.expression)
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
            self.expression = str(result)
        except ZeroDivisionError:
            messagebox.showerror("Error", "Division by zero!")
            self.clear()
        except Exception as e:
            messagebox.showerror("Error", "Invalid expression!")
            self.clear()
    
    def clear(self):
        self.expression = ""
        self.display.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
