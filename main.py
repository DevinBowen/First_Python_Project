import tkinter as tk
from tkinter import ttk


def greet():
    print(f"Hello, {user_name.get() or 'World'}!")


root = tk.Tk()
root.geometry("600x400")


user_name = tk.StringVar()


rectangle_1 = tk.Label(root, text="Title", bg="blue", fg="white")
rectangle_1.pack(ipadx=10, ipady=10, fill="x")

name_label = ttk.Label(root, text="Name: ")
name_label.pack(side="left", padx=(0, 10))

name_entry = ttk.Entry(root, width=15, textvariable=user_name)
name_entry.pack(side="left")
name_entry.focus()

greet_button = ttk.Button(root, text="greet", command=greet)
greet_button.pack(side="left")

quit_button = ttk.Button(root, text="quit", command=root.destroy)
quit_button.pack(side="right")

root.mainloop()
