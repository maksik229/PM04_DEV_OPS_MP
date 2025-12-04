import tkinter as tk
from tkinter import ttk
import random

def generate():
    max_val = slider.get()
    rand_num = random.randint(0, max_val)
    progress['value'] = rand_num
    label.config(text=f"Число: {rand_num}")

root = tk.Tk()
root.title("Задание 7")

tk.Label(root, text="Задание 7\nСбитнева Дарья").pack(pady=5)
slider = tk.Scale(root, from_=10, to=100)
slider.set(50)
slider.pack()
progress = ttk.Progressbar(root, length=200, maximum=100)
progress.pack(pady=10)
tk.Button(root, text="Сгенерировать", command=generate).pack()
label = tk.Label(root, text="Нажмите кнопку")
label.pack(pady=10)

root.mainloop()