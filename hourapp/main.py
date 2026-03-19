import tkinter as tk

completed_tasks = ["Do homework", "Go to gym", "Buy food"]
window = tk.Tk()
window.title("To Do List")
window.geometry("800x600")

def start():
    title_label.pack_forget()
    start_btn.pack_forget()
    see_completed.pack()

    entry.pack()
    add_btn.pack()

def add_task():
    text = entry.get()
    if text == "":
        return

    frame = tk.Frame(window)
    frame.pack()

    tk.Label(frame, text=text).pack(side="left")

    tk.Button(frame, text="✔").pack(side="left")
    tk.Button(frame, text="X", command=frame.destroy).pack(side="left")

    entry.delete(0, tk.END)

def show_completed():
    new_window = tk.Toplevel(window)
    new_window.title("Completed Tasks")
    new_window.geometry("400x400")


    for task in completed_tasks:
        tk.Label(new_window, text=task).pack()

# store these in variables so we can hide them
title_label = tk.Label(window, text="My To Do List")
title_label.pack()

start_btn = tk.Button(window, text="Start", command=start)
start_btn.pack()

entry = tk.Entry(window)
add_btn = tk.Button(window, text="Add", command=add_task)

see_completed = tk.Button(window, text="See Completed Tasks", command=show_completed)
window.mainloop()