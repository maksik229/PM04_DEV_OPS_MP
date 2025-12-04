import tkinter as tk
from math import cos, sin, pi

def create_button(canvas, shape, x, y, text, cmd):
    """Создает кнопку нестандартной формы на Canvas"""
    size = 35  # Размер кнопки
    color = "lightblue"  # Цвет по умолчанию
    
    # Создаем форму в зависимости от типа
    if shape == "triangle":
        # Треугольник: верхняя точка и две нижних
        points = [(x, y-size), (x-size, y+size), (x+size, y+size)]
        btn = canvas.create_polygon(points, fill=color, activefill="lightgreen")
    
    elif shape == "star":
        # Звезда: чередуем длинные и короткие лучи
        points = []
        for i in range(10):
            angle = pi/2 - i*2*pi/10
            r = size if i%2==0 else size*0.4  # Длинные/короткие лучи
            points.extend([x + r*cos(angle), y - r*sin(angle)])
        btn = canvas.create_polygon(points, fill=color, activefill="lightgreen")
    
    elif shape == "hexagon":
        # Шестиугольник: 6 вершин
        points = [(x+size*cos(pi/3*i), y+size*sin(pi/3*i)) for i in range(6)]
        points = [coord for point in points for coord in point]  # Преобразуем в плоский список
        btn = canvas.create_polygon(points, fill=color, activefill="lightgreen")
    
    elif shape == "octagon":
          # Восьмиугольник: 8 вершин
        points = [(x+size*cos(pi/4*i), y+size*sin(pi/4*i)) for i in range(8)]
        points = [coord for point in points for coord in point]
        btn = canvas.create_polygon(points, fill=color, activefill="lightgreen")
        elif shape == "oval":
        # Овальная кнопка
        btn = canvas.create_oval(x-size, y-size//2, x+size, y+size//2, 
                                fill=color, activefill="lightgreen")
    
    elif shape == "double_oval":
       
        canvas.create_oval(x-size, y-size//2, x+size, y+size//2, fill=color)
        btn = canvas.create_oval(x-size//2, y-size//4, x+size//2, y+size//4, 
                                fill="yellow", activefill="lightyellow")
    
    
    canvas.create_text(x, y, text=text[:3], font=("Arial", 8))
    
    def click(e):
        """Обработчик нажатия на кнопку"""
        cmd() 
        
        canvas.itemconfig(btn, fill="gray")
        canvas.after(100, lambda: canvas.itemconfig(btn, fill=color))
    
    
    canvas.tag_bind(btn, "<Button-1>", click)
    return btn
root = tk.Tk()
root.title("Задание 1 - Сбитнева Д.")
root.geometry("600x400")
tk.Label(root, text="Задание 1: Кнопки разной формы\nСбитнева Дарья").pack()
canvas = tk.Canvas(root, width=550, height=250, bg="white")
canvas.pack(pady=20)
status = tk.Label(root, text="Нажмите кнопку")
status.pack()

def action(name):
    status.config(text=f"Нажата: {name}")
create_button(canvas, "triangle", 80, 100, "Треуг", lambda: action("Треугольная"))
create_button(canvas, "star", 160, 100, "Звез", lambda: action("Звезда"))
create_button(canvas, "hexagon", 240, 100, "6-уг", lambda: action("Шестиугольная"))
create_button(canvas, "octagon", 320, 100, "8-уг", lambda: action("Восьмиугольная"))
create_button(canvas, "oval", 400, 100, "Овал", lambda: action("Овальная"))
create_button(canvas, "double_oval", 480, 100, "Дв", lambda: action("Двойная"))
labels = ["Треугольная", "Звезда", "6-угольная", "8-угольная", "Овальная", "Двойная"]
for i, label in enumerate(labels):
    canvas.create_text(80 + i*80, 150, text=label, font=("Arial", 8))
root.mainloop()