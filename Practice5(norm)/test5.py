import tkinter as tk
import math

root = tk.Tk()
root.title("Спидометр")
root.geometry("250x350")

# Заголовок
tk.Label(root, text="Задание 5: Работа Сбитневой Дарьи").pack(pady=10)

canvas = tk.Canvas(root, width=150, height=150, bg="white")
canvas.pack()

canvas.create_arc(10, 10, 140, 140, start=30, extent=120, style=tk.ARC, width=2)


canvas.create_oval(72, 72, 78, 78, fill="black")


arrow = canvas.create_line(75, 75, 75, 30, width=3, fill="red")


speed = 60
label = tk.Label(root, text=f"{speed} км/ч", font=("Arial", 20))
label.pack(pady=10)


def set_speed(s):
    global speed
    speed = max(0, min(120, s))  # Ограничение 0-120
    label.config(text=f"{speed} км/ч")


    angle = 30 + speed
    rad = math.radians(angle)

    x = 75 + 45 * math.cos(rad)
    y = 75 - 45 * math.sin(rad)

    canvas.coords(arrow, 75, 75, x, y)


for s in [0, 30, 60, 90, 120]:
    color = "green" if s < 60 else "orange" if s < 90 else "red"
    tk.Button(root, text=f"{s} км/ч", bg=color, fg="white",
              command=lambda v=s: set_speed(v)).pack(side=tk.LEFT, padx=5)

root.mainloop()
