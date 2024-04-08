import tkinter as tk
from tkinter import ttk


def button_click(symbol):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + symbol)


def delete_last():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current[:-1])

def clear():
    entry.delete(0, tk.END)


def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


def percent():
    try:
        result = eval(entry.get())
        result /= 100
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


root = tk.Tk()
root.title("Calculator")

root.configure(bg="#f0f0f0")
root.geometry("430x270")
root.resizable(False, False)

entry = tk.Entry(root, width=20, font=("Helvetica", 20), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

button_style = ttk.Style()
button_style.configure('TButton', font=("Helvetica", 14))

buttons = [
    ('C', 1, 0), ('DEL', 1, 1), ('%', 1, 2), ('/', 1, 3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
    ('0', 5, 0), ('.', 5, 1), ('=', 5, 2)
]

for (text, row, column) in buttons:
    if text == 'C':
        button = ttk.Button(root, text=text, width=8, style='TButton', command=clear)
    elif text == 'DEL':
        button = ttk.Button(root, text=text, width=8, style='TButton', command=delete_last)
    elif text == '=':
        button = ttk.Button(root, text=text, width=8, style='TButton', command=calculate)
    elif text == '%':
        button = ttk.Button(root, text=text, width=8, style='TButton', command=percent)
    else:
        button = ttk.Button(root, text=text, width=8, style='TButton', command=lambda symbol=text: button_click(symbol))
    button.grid(row=row, column=column, padx=5, pady=5)

root.mainloop()
