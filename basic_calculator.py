import tkinter as tk
from tkinter import messagebox


def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2

        result_label.config(text=f"Result: {result:.2f}", fg="#ffffff", bg="#4CAF50")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")
    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Cannot divide by zero.")


def clear_fields():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_label.config(text="Result:", bg=main_bg, fg="white")

root = tk.Tk()
root.title("🎨 Basic Calculator")
root.geometry("320x350")
root.resizable(False, False)


main_bg = "#2c3e50"
btn_bg = "#3498db"
btn_fg = "white"
entry_bg = "#ecf0f1"
entry_fg = "#2c3e50"


root.config(bg=main_bg)


tk.Label(root, text=" Basic Calculator", font=("Helvetica", 16, "bold"), fg="white", bg=main_bg).pack(pady=10)


tk.Label(root, text="Enter first number:", bg=main_bg, fg="white").pack()
entry1 = tk.Entry(root, width=25, bg=entry_bg, fg=entry_fg, font=("Arial", 11))
entry1.pack(pady=5)


tk.Label(root, text="Enter second number:", bg=main_bg, fg="white").pack()
entry2 = tk.Entry(root, width=25, bg=entry_bg, fg=entry_fg, font=("Arial", 11))
entry2.pack(pady=5)


button_frame = tk.Frame(root, bg=main_bg)
button_frame.pack(pady=15)


btn_style = {
    "width": 10,
    "bg": btn_bg,
    "fg": btn_fg,
    "font": ("Arial", 10, "bold"),
    "bd": 0,
    "activebackground": "#2980b9"
}


tk.Button(button_frame, text="Add", command=lambda: calculate('add'), **btn_style).grid(row=0, column=0, padx=5, pady=5)
tk.Button(button_frame, text="Subtract", command=lambda: calculate('subtract'), **btn_style).grid(row=0, column=1, padx=5, pady=5)
tk.Button(button_frame, text="Multiply", command=lambda: calculate('multiply'), **btn_style).grid(row=1, column=0, padx=5, pady=5)
tk.Button(button_frame, text="Divide", command=lambda: calculate('divide'), **btn_style).grid(row=1, column=1, padx=5, pady=5)


clear_btn_style = {
    "width": 22,
    "bg": "#e74c3c",
    "fg": btn_fg,
    "font": ("Arial", 10, "bold"),
    "bd": 0,
    "activebackground": "#c0392b"
}

tk.Button(root, text="Clear", command=clear_fields, **clear_btn_style).pack(pady=10)

result_label = tk.Label(root, text="Result:", font=("Arial", 12), bg=main_bg, fg="white")
result_label.pack(pady=10)
root.mainloop()
