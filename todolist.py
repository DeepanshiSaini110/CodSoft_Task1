import tkinter as tk
from tkinter import messagebox

# Setting up the main app window

root = tk.Tk()
root.title("To-Do List")
root.geometry("500x500")
root.config(bg="#EEF8BA")
root.resizable(False, False)

# Header Label
title_var = tk.StringVar(value="📝 To-Do List App")
title_label = tk.Label(root, textvariable=title_var,bg="#272D08", fg="#DDF26F",font=("Arial", 16, "bold"),
                       padx=15, pady=15,relief=tk.RAISED)
title_label.pack(padx=20, pady=20, fill='x')

# Task input box
task_entry = tk.Entry(root, width=40, font=("Arial", 12))
task_entry.insert(0, "e.g., Buy groceries")
task_entry.pack(pady=10)

# Listbox to show tasks
task_listbox = tk.Listbox(root, width=50, height=10, font=("Arial", 11))
task_listbox.pack(pady=10)

# Just grabs the selected task index (if any)
def get_selected_task_index():
    try:
        return task_listbox.curselection()[0]
    except IndexError:
        return None
 # Add task
def add_task():
    task = task_entry.get().strip()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Oops!", "You forgot to type something.")

# Select task to edit
def select_task(event=None):
    index = get_selected_task_index()
    if index is not None:
        task_entry.delete(0, tk.END)
        task_entry.insert(0, task_listbox.get(index))

# Update task
def update_task():
    index = get_selected_task_index()
    if index is not None:
        new_text = task_entry.get().strip()
        if new_text:
            task_listbox.delete(index)
            task_listbox.insert(index, new_text)
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Update Error", "Task cannot be empty.")
    else:
        messagebox.showinfo("Heads up!", "Click on a task before updating it.")

# Delete task
def delete_task():
    index = get_selected_task_index()
    if index is not None:
        task_listbox.delete(index)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showinfo("Selection Error", "Select a task to delete.")

# View all tasks
def view_tasks():
    tasks = task_listbox.get(0, tk.END)
    if tasks:
        task_text = "\n".join([f"{i+1}. {task}" for i, task in enumerate(tasks)])
        messagebox.showinfo("Your Tasks", task_text)
    else:
        messagebox.showinfo("Task List", "Looks like you haven't added any tasks yet.")

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)
add_btn = tk.Button(button_frame, text="Add Task",background="#C7DF3F",foreground="#363D11", width=12, command=add_task)
add_btn.grid(row=0, column=0, padx=5)

update_btn = tk.Button(button_frame, text="Update Task",background="#C7DF3F",foreground="#363D11", width=12, command=update_task)
update_btn.grid(row=0, column=1, padx=5)

delete_btn = tk.Button(button_frame, text="Delete Task",background="#C7DF3F",foreground="#363D11", width=12, command=delete_task)
delete_btn.grid(row=0, column=2, padx=5)

view_btn = tk.Button(button_frame, text="View Tasks", background="#C7DF3F",foreground="#363D11",width=12, command=view_tasks)
view_btn.grid(row=0, column=3, padx=5)

# Bind selecting a task
task_listbox.bind('<<ListboxSelect>>', select_task)

# Run the app (main loop starts here)
root.mainloop()
