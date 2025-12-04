import tkinter as tk
import random

def draw():
    canvas.delete("all")
    
   
    try:
        count = min(int(count_entry.get()), 1000)
        max_val = max(int(max_entry.get()), 1)
    except:
        count, max_val = 100, 100
    
    w, h = 400, 200


    canvas.create_line(30, h-30, w-30, h-30, width=2)
    canvas.create_line(30, 30, 30, h-30, width=2)

    for i in range(count):
        x = 30 + i * (w-60) / count
        y = h - 30 - random.randint(0, max_val) * (h-60) / max_val
        canvas.create_oval(x-1, y-1, x+1, y+1, fill="blue")

    info.config(text=f"Точек: {count}, Макс: {max_val}")


root.title("Задание 8. Сбитнева Д.")
root.geometry("450x350")

tk.Label(root, text="Задание 8\nСбитнева Дарья").pack()


frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Количество:").pack(side=tk.LEFT)
count_entry = tk.Entry(frame, width=8)
count_entry.insert(0, "100")
count_entry.pack(side=tk.LEFT, padx=5)

tk.Label(frame, text="Макс:").pack(side=tk.LEFT)
max_entry = tk.Entry(frame, width=8)
max_entry.insert(0, "100")
max_entry.pack(side=tk.LEFT, padx=5)

tk.Button(root, text="Нарисовать", command=draw).pack()


canvas = tk.Canvas(root, width=400, height=200, bg="white")
canvas.pack(pady=10)


info = tk.Label(root, text="Установите параметры")
info.pack()


draw()

root.mainloop()