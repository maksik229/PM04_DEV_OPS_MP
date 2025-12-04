import tkinter as tk
import math

root = tk.Tk()
root.title("Термометр")
root.geometry("200x300")

# Заголовок
tk.Label(root, text="Задание 1: Работа Сбитневой Дарьи").pack(pady=5)


canvas = tk.Canvas(root, width=120, height=120, bg="white")
canvas.pack()


canvas.create_oval(10, 10, 110, 110, width=2)


arrow = canvas.create_line(60, 60, 60, 20, width=3, fill="red")


temp = 20
label = tk.Label(root, text=f"{temp}°C", font=("Arial", 20))
label.pack(pady=10)

def set_temp(t):
    global temp
    temp = t
    label.config(text=f"{temp}°C")


    angle = 180 - temp * 1.8
    rad = math.radians(angle)


    x = 60 + 40 * math.cos(rad)
    y = 60 - 40 * math.sin(rad)


    color = "blue" if t < 20 else "orange" if t < 40 else "red"
    canvas.itemconfig(arrow, fill=color)
    label.config(fg=color)


for t in [0, 20, 37, 100]:
    color = "blue" if t < 20 else "orange" if t < 40 else "red"
    tk.Button(root, text=f"{t}°", bg=color, fg="white",
              command=lambda v=t: set_temp(v)).pack(side=tk.LEFT, padx=5)

root.mainloop()





