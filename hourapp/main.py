import tkinter as tk

window = tk.Tk()
window.title("To Do List")
window.geometry("800x600")

def start():
    entry.pack()
    add_btn.pack()

def add_task():
    text = entry.get()
    if text == "":
        return

    frame = tk.Frame(window)
    frame.pack()

    tk.Label(frame, text=text).pack(side="left")

    tk.Button(frame, text="✔").pack(side="left")  # complete (no logic)
    tk.Button(frame, text="X", command=frame.destroy).pack(side="left")  # delete
    tk.Button(frame, text="+", command=add_task).pack(side="left")  # new

    entry.delete(0, tk.END)

tk.Label(window, text="My To Do List").pack()
tk.Button(window, text="Start", command=start).pack()

entry = tk.Entry(window)
add_btn = tk.Button(window, text="Add", command=add_task)

window.mainloop()