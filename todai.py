import tkinter as tk
from tkinter import messagebox

root = tk.Tk() 

root.title("todai")
root.geometry("800x700")
root.configure(bg="#5E4D47")


def save_button_c():
    print("clicked")
    

my_button = tk.Button(
    root, 
    text="    save    ", 
    command=save_button_c,
    bg="#4B604F",
    fg="#E1DEDC",
    font=('Arial', 10, 'bold')
)

my_button.grid(
    row=1, 
    column=1, 
    padx=700, 
    pady=650, 
    sticky='se'
)

root.mainloop()