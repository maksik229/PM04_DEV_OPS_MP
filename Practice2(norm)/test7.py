import tkinter as tk
import random

def draw_new():
    canvas.delete("all")
    
    
    w, h = 500, 300
    margin = 40
    
    canvas.create_line(margin, h-margin, w-margin, h-margin, width=2)
    canvas.create_line(margin, margin, margin, h-margin, width=2)

    points = [random.randint(0, 100) for _ in range(1000)]
    point_w = (w - 2*margin) / 1000
    
    for i, val in enumerate(points):
        x = margin + i * point_w
        y = h - margin - (val * (h - 2*margin) / 100)
        canvas.create_oval(x-1, y-1, x+1, y+1, fill="blue")

root = tk.Tk()
root.title("Задание 7. Сбитнева Д.")
root.geometry("550x400")
tk.Label(root, text="Задание 7: График 1000 точек\nСбитнева Дарья").pack(pady=10)
canvas = tk.Canvas(root, width=500, height=300, bg="white")
canvas.pack(pady=10)
tk.Button(root, text="Новый график", command=draw_new).pack(side=tk.LEFT, padx=50)
tk.Button(root, text="Очистить", command=lambda: canvas.delete("all")).pack(side=tk.LEFT, padx=50)
draw_new()

root.mainloop()