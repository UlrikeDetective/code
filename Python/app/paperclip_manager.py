""" Clipboard Manager 
Have you ever found yourself juggling multiple text snippets, losing track of what you’ve copied? Ever thought of having a tool that can 
keep track of everything you copy in a day?

This automation script watches over everything you copy, seamlessly storing each copied text within a sleek graphical interface, 
so that you don’t have to search through endless tabs and lose some valuable information.

This automation script harnesses the power of the Pyperclip library to capture copied data seamlessly and integrates 
Tkinter to visually track and manage the copied text.

Script Applications —
Capturing and categorizing research notes copied from various sources.
Extending the script can capture important calendar events, reminders, passwords, etc. """

import tkinter as tk
from tkinter import ttk
import pyperclip

def update_listbox():
    new_item = pyperclip.paste()
    if new_item not in X:
        X.append(new_item)
        listbox.insert(tk.END, new_item)
        listbox.insert(tk.END, "----------------------")
    listbox.yview(tk.END)
    root.after(1000, update_listbox)

def copy_to_clipboard(event):
    selected_item = listbox.get(listbox.curselection())
    if selected_item:
        pyperclip.copy(selected_item)

X = []

root = tk.Tk()
root.title("Clipboard Manager")
root.geometry("500x500")
root.configure(bg="#f0f0f0")

frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Clipboard Contents:", bg="#f0f0f0")
label.grid(row=0, column=0)

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(root, width=150, height=150, yscrollcommand=scrollbar.set)
listbox.pack(pady=10)
scrollbar.config(command=listbox.yview)

update_listbox()

listbox.bind("<Double-Button-1>", copy_to_clipboard)

root.mainloop()