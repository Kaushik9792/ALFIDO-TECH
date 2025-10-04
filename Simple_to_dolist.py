import tkinter as tk
from tkinter import messagebox
import os

TASKS_FILE = "tasks.txt"

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x400")
        
        self.task_entry = tk.Entry(self.root, width=30)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(self.root, text="Add Task", width=15, command=self.add_task)
        self.add_button.pack(pady=5)

        self.remove_button = tk.Button(self.root, text="Remove Selected", width=15, command=self.remove_task)
        self.remove_button.pack(pady=5)

        self.task_listbox = tk.Listbox(self.root, width=40, height=10, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        self.view_button = tk.Button(self.root, text="View All Tasks", width=15, command=self.view_tasks)
        self.view_button.pack(pady=5)

        self.tasks = []
        self.load_tasks()

    def add_task(self):
        task = self.task_entry.get().strip()
        if task == "":
            messagebox.showwarning("Input Error", "Please enter a task.")
        else:
            self.tasks.append(task)
            self.task_entry.delete(0, tk.END)
            self.update_listbox()
            self.save_tasks()

    def remove_task(self):
        selected = self.task_listbox.curselection()
        if not selected:
            messagebox.showwarning("Selection Error", "Please select a task to remove.")
        else:
            task_to_remove = self.task_listbox.get(selected)
            self.tasks.remove(task_to_remove)
            self.update_listbox()
            self.save_tasks()

    def view_tasks(self):
        if not self.tasks:
            messagebox.showinfo("To-Do List", "No tasks added yet.")
        else:
            tasks_str = "\n".join(f"{i+1}. {task}" for i, task in enumerate(self.tasks))
            messagebox.showinfo("To-Do List", tasks_str)

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def load_tasks(self):
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, "r") as file:
                self.tasks = [line.strip() for line in file.readlines()]
            self.update_listbox()

    def save_tasks(self):
        with open(TASKS_FILE, "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

