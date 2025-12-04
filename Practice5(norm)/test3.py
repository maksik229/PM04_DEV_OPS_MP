import tkinter as tk
import time

root = tk.Tk()
root.title("Часы")
root.geometry("250x350")

# Заголовок
tk.Label(root, text="Задание 3: Работа Сбитневой Дарьи", font=("Arial", 11, "bold")).pack(pady=10)

# Холст для часов
canvas = tk.Canvas(root, width=150, height=150, bg="white")
canvas.pack()

# Циферблат
canvas.create_oval(10, 10, 140, 140, width=2)

# Центр
canvas.create_oval(72, 72, 78, 78, fill="black")

# Цифры (только основные)
canvas.create_text(75, 25, text="12", font=("Arial", 10))
canvas.create_text(125, 75, text="3", font=("Arial", 10))
canvas.create_text(75, 125, text="6", font=("Arial", 10))
canvas.create_text(25, 75, text="9", font=("Arial", 10))

# Стрелки
hour_hand = canvas.create_line(75, 75, 75, 50, width=3, fill="black")
minute_hand = canvas.create_line(75, 75, 75, 35, width=2, fill="blue")
second_hand = canvas.create_line(75, 75, 75, 30, width=1, fill="red")

# Цифровые часы
digital = tk.Label(root, text="--:--:--", font=("Arial", 18, "bold"), fg="blue")
digital.pack(pady=15)

# Функция обновления
def update():
    t = time.localtime()
    h, m, s = t.tm_hour, t.tm_min, t.tm_sec
    
    # Цифровые
    digital.config(text=f"{h:02d}:{m:02d}:{s:02d}")
    
    # Углы для стрелок
    hour_angle = (h % 12 + m / 60) * 30 - 90
    minute_angle = m * 6 - 90
    second_angle = s * 6 - 90
    
    # Координаты стрелок (упрощенный расчет)
    def get_coords(angle, length):
        import math
        rad = angle * math.pi / 180
        x = 75 + length * math.cos(rad)
        y = 75 + length * math.sin(rad)
        return x, y
    
    # Обновляем стрелки
    hx, hy = get_coords(hour_angle, 30)
    mx, my = get_coords(minute_angle, 45)
    sx, sy = get_coords(second_angle, 50)
    
    canvas.coords(hour_hand, 75, 75, hx, hy)
    canvas.coords(minute_hand, 75, 75, mx, my)
    canvas.coords(second_hand, 75, 75, sx, sy)
    
    # Повтор через 200 мс
    root.after(200, update)

# Запуск
update()
root.mainloop()
