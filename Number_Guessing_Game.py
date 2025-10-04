import tkinter as tk
from tkinter import messagebox
import random

def start_new_game():
    global target_number, attempts
    target_number = random.randint(1, 100)
    attempts = 0
    feedback_label.config(
        text="Guess a number between 1 and 100",
        bg="#dabf56",
        fg="#2c3e50"
    )
    guess_entry.delete(0, tk.END)

def check_guess():
    global attempts
    try:
        guess = int(guess_entry.get())
        if guess < 1 or guess > 100:
            raise ValueError

        attempts += 1

        if guess < target_number:
            feedback_label.config(text="Too low! Try again.", bg="#3498db", fg="white")
        elif guess > target_number:
            feedback_label.config(text="Too high! Try again.", bg="#f39c12", fg="white")
        else:
            feedback_label.config(text=f"🎉 Correct! You guessed it in {attempts} attempts.", bg="#27ae60", fg="white")
            messagebox.showinfo("Congratulations!", f"You guessed the number {target_number} in {attempts} tries!")
            start_new_game()

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter an integer between 1 and 100.")

root = tk.Tk()
root.title("🎯 Number Guessing Game")
root.geometry("400x300")
root.resizable(False, False)

main_bg = "#f4f1ff"  # NEW light lavender background
entry_bg = "#ffffff"
entry_fg = "#2c3e50"
btn_bg = "#9b59b6"
btn_fg = "white"

root.config(bg=main_bg)

tk.Label(root, text="Number Guessing Game", font=("Helvetica", 18, "bold"), fg="#2c3e50", bg=main_bg).pack(pady=15)

feedback_label = tk.Label(root, text="", font=("Arial", 12), bg=main_bg, fg="#2c3e50")
feedback_label.pack(pady=10)

guess_entry = tk.Entry(root, font=("Arial", 12), width=20, bg=entry_bg, fg=entry_fg, justify="center")
guess_entry.pack(pady=10)

tk.Button(root, text="Submit Guess", command=check_guess, width=20, bg=btn_bg, fg=btn_fg,
          font=("Arial", 11, "bold"), bd=0, activebackground="#8e44ad").pack(pady=10)

tk.Button(root, text="Reset Game", command=start_new_game, width=20, bg="#e74c3c", fg="white",
          font=("Arial", 11, "bold"), bd=0, activebackground="#c0392b").pack(pady=5)

start_new_game()
root.mainloop()
