import tkinter as tk
from tkinter import ttk, messagebox


def celsius_to_fahrenheit(c): return (c * 9/5) + 32
def celsius_to_kelvin(c): return c + 273.15
def fahrenheit_to_celsius(f): return (f - 32) * 5/9
def fahrenheit_to_kelvin(f): return (f - 32) * 5/9 + 273.15
def kelvin_to_celsius(k): return k - 273.15
def kelvin_to_fahrenheit(k): return (k - 273.15) * 9/5 + 32


def convert():
    try:
        temp = float(entry_temp.get())
        from_unit = combo_from.get()
        to_unit = combo_to.get()

        if from_unit == to_unit:
            result = temp
        elif from_unit == "Celsius" and to_unit == "Fahrenheit":
            result = celsius_to_fahrenheit(temp)
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            result = celsius_to_kelvin(temp)
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            result = fahrenheit_to_celsius(temp)
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            result = fahrenheit_to_kelvin(temp)
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            result = kelvin_to_celsius(temp)
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            result = kelvin_to_fahrenheit(temp)
        else:
            result = "Invalid"

        label_result.config(text=f"Result: {result:.2f} {to_unit}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")

root = tk.Tk()
root.title("Temperature Converter")
root.geometry("350x350")
root.resizable(False, False)


tk.Label(root, text="Enter Temperature:", font=("Arial", 11)).pack(pady=5)
entry_temp = tk.Entry(root, font=("Arial", 11))
entry_temp.pack(pady=5)


tk.Label(root, text="From:", font=("Arial", 11)).pack()
combo_from = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"], font=("Arial", 11))
combo_from.current(0)
combo_from.pack(pady=5)

tk.Label(root, text="To:", font=("Arial", 11)).pack()
combo_to = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"], font=("Arial", 11))
combo_to.current(1)
combo_to.pack(pady=5)

tk.Button(root, text="Convert", font=("Arial", 11), command=convert, bg="lightblue").pack(pady=10)


label_result = tk.Label(root, text="Result: ", font=("Arial", 12, "bold"))
label_result.pack(pady=10)

root.mainloop()
