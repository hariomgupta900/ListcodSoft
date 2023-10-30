import tkinter as tk
from tkinter import messagebox

# Create a function to add a new task
def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Create a function to delete a selected task
def delete_task():
    try:
        selected_task_index = task_list.curselection()[0]
        task_list.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Initialize the main window
root = tk.Tk()
root.title("To-Do List Application")

# Create a task entry field
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

# Create a button to add a task
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

# Create a listbox to display tasks
task_list = tk.Listbox(root, width=40)
task_list.pack(pady=10)

# Create a button to delete a selected task
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack()

# Run the application
root.mainloop()
