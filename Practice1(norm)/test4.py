import tkinter as tk
from tkinter import ttk

def update_progressbar(value):
   progressbar['value'] = float(value)
   value_label.config(text=f"Значение: {value}%")
root = tk.Tk()
root.title("Задание 4 работа Сбитневой Дарьи")
root.geometry("400x200")
progressbar = ttk.Progressbar(root, length=300, mode='determinate', maximum=100)
progressbar.pack(pady=30)
value_label = tk.Label(root, text="Значение: 0%", font=("Arial", 12))
value_label.pack(pady=10)
trackbar = tk.Scale(
    root, 
    from_=0, 
    to=100, 
    orient=tk.HORIZONTAL,
    length=300,
    command=update_progressbar,
    font=("Arial", 10)
)
trackbar.pack(pady=10)
tk.Label(root, text="Перемещайте ползунок →", font=("Arial", 10)).pack()
root.mainloop()