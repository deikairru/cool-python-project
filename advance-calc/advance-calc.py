import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        operator = operator_var.get()
        
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                raise ValueError("Cannot divide by zero")
            result = num1 / num2
        elif operator == "**":
            result = num1 ** num2
        else:
            raise ValueError("Invalid operator")
        
        result_label.config(text=f"Result: {result}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Advanced Calculator")

# Input fields
num1_label = tk.Label(root, text="Number 1:")
num1_label.grid(row=0, column=0, padx=5, pady=5)
num1_entry = tk.Entry(root, width=15)
num1_entry.grid(row=0, column=1, padx=5, pady=5)

num2_label = tk.Label(root, text="Number 2:")
num2_label.grid(row=1, column=0, padx=5, pady=5)
num2_entry = tk.Entry(root, width=15)
num2_entry.grid(row=1, column=1, padx=5, pady=5)

# Operator selection
operator_label = tk.Label(root, text="Operator:")
operator_label.grid(row=2, column=0, padx=5, pady=5)
operator_var = tk.StringVar(value="+")
operator_options = ["+", "-", "*", "/", "**"]
operator_menu = tk.OptionMenu(root, operator_var, *operator_options)
operator_menu.grid(row=2, column=1, padx=5, pady=5)

# Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Result display
result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()