import tkinter as tk
from tkinter import ttk

def update_progress(value):
     progressbar['value'] = float(value)
     value_label.config(text=f"{value}%")
root = tk.Tk()
root.title("Задание 5 работа Сбитневой Дарьи")
root.geometry("400x400")

title_label = tk.Label(root, text="Задание 5: Вертикальный ProgressBar\nРабота Сбитневой Дарьи", 
                       font=("Arial", 14, "bold"))
title_label.pack(pady=10)
progressbar = ttk.Progressbar(root, orient='vertical', length=200, mode='determinate', maximum=100)
progressbar.pack(pady=20)
value_label = tk.Label(root, text="0%", font=("Arial", 16, "bold"))
value_label.pack()
trackbar = tk.Scale(
    root, 
    from_=0, 
    to=100, 
    orient=tk.HORIZONTAL,
    length=250,
    command=update_progress,
    font=("Arial", 10)
)
trackbar.pack(pady=20)
use_label = tk.Label(root, text="Пример: Уровень громкости", font=("Arial", 12))
use_label.pack(pady=10)
frame = tk.Frame(root)
frame.pack(pady=10)
min_label = tk.Label(frame, text="Мин: 0%", font=("Arial", 10))
min_label.pack(side=tk.LEFT, padx=20)

max_label = tk.Label(frame, text="Макс: 100%", font=("Arial", 10))
max_label.pack(side=tk.LEFT, padx=20)
root.mainloop()