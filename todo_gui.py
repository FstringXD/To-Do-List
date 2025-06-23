import tkinter as tk
from tkinter import messagebox
import os

TODO_FILE = "todo_list.txt"

# Load tasks from file
def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as f:
            return [line.strip() for line in f.readlines()]
    return []

# Save tasks to file
def save_tasks():
    tasks = listbox.get(0, tk.END)
    with open(TODO_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")
    messagebox.showinfo("Saved", "✅ Tasks saved to file.")

# Add a new task
def add_task():
    task = entry.get().strip()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Delete selected task
def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)
    else:
        messagebox.showwarning("Warning", "No task selected.")

# Mark task as done
def mark_done():
    selected = listbox.curselection()
    if selected:
        task = listbox.get(selected)
        if not task.startswith("✅"):
            listbox.delete(selected)
            listbox.insert(selected, f"✅ {task}")
    else:
        messagebox.showwarning("Warning", "No task selected.")

# Create GUI window
root = tk.Tk()
root.title("📝 To-Do List")

# Layout
frame = tk.Frame(root)
frame.pack(pady=10)

entry = tk.Entry(frame, width=30)
entry.pack(side=tk.LEFT, padx=5)

add_btn = tk.Button(frame, text="Add Task", command=add_task)
add_btn.pack(side=tk.LEFT)

listbox = tk.Listbox(root, width=50, height=10, selectmode=tk.SINGLE)
listbox.pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack()

done_btn = tk.Button(btn_frame, text="✅ Mark Done", command=mark_done)
done_btn.grid(row=0, column=0, padx=5)

delete_btn = tk.Button(btn_frame, text="🗑️ Delete Task", command=delete_task)
delete_btn.grid(row=0, column=1, padx=5)

save_btn = tk.Button(btn_frame, text="💾 Save Tasks", command=save_tasks)
save_btn.grid(row=0, column=2, padx=5)

# Load existing tasks
for task in load_tasks():
    listbox.insert(tk.END, task)

# Run the GUI loop
root.mainloop()
