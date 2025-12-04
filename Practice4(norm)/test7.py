import tkinter as tk

root = tk.Tk()
root.title("Music Maker")
root.geometry("500x400")


tk.Label(root, text="Задание 7: Работа Сбитневой Дарьи", 
         font=("Arial", 14, "bold"), fg="darkblue").pack(pady=5)

tk.Label(root, text="🎵 Создатель музыки 🎵", 
         font=("Arial", 16, "bold"), fg="blue").pack()

frame = tk.Frame(root)
frame.pack(pady=10)

sounds = [
    ("🥁", "Барабан", "red"),
    ("🎹", "Пианино", "blue"),
    ("🔔", "Колокольчик", "yellow"),
    ("🎸", "Гитара", "purple")
]

for i, (icon, name, color) in enumerate(sounds):
    btn = tk.Button(
        frame,
        text=f"{icon}\n{name}",
        font=("Arial", 10),
        bg=color,
        fg='white',
        width=8,
        height=3,
        command=lambda n=name: play_sound(n)
    )
    btn.pack(side="left", padx=5)




tk.Label(root, text="Музыкальная сетка (кликните по ячейкам):").pack(pady=5)

canvas = tk.Canvas(root, bg='lightgray', width=300, height=150)
canvas.pack()

grid = []
for row in range(4):
    grid_row = []
    for col in range(4):
        x1 = col * 75
        y1 = row * 37
        rect = canvas.create_rectangle(x1, y1, x1+70, y1+32, fill='white', outline='gray')
        grid_row.append(('white', None))
    grid.append(grid_row)



colors = ['red', 'blue', 'yellow', 'purple']
current_color = 0

def click_grid(event):
    """Обработка клика по сетке"""
    col = event.x // 75
    row = event.y // 37
    
    if 0 <= col < 4 and 0 <= row < 4:



        color = colors[current_color]
        canvas.itemconfig(canvas.find_closest(event.x, event.y)[0], fill=color)
        grid[row][col] = (color, current_color)



        root.bell()
        status.config(text=f"Добавлен: {sounds[current_color][1]}")

def change_color():
    """Смена цвета для следующей ячейки"""
    global current_color
    current_color = (current_color + 1) % 4
    color_btn.config(bg=colors[current_color], text=f"Цвет: {sounds[current_color][1]}")

def play_sound(name):
    """Проигрывание звука"""
    root.bell()
    status.config(text=f"Играет: {name}")

def play_all():
    """Проигрывание всей сетки"""
    status.config(text="Играет музыка! 🎵")
    for i in range(16):  # Простой цикл
        root.after(i * 200, root.bell)

def clear_grid():
    """Очистка сетки"""
    for item in canvas.find_all():
        canvas.itemconfig(item, fill='white')
    status.config(text="Сетка очищена!")


control_frame = tk.Frame(root)
control_frame.pack(pady=10)

color_btn = tk.Button(control_frame, text="Цвет: Барабан", 
                     command=change_color, bg='red', fg='white')
color_btn.pack(side="left", padx=5)

tk.Button(control_frame, text="▶ Играть всё", 
         command=play_all, bg='green', fg='white').pack(side="left", padx=5)

tk.Button(control_frame, text="🗑️ Очистить", 
         command=clear_grid, bg='gray', fg='white').pack(side="left", padx=5)




status = tk.Label(root, text="Нажмите на инструменты или сетку")
status.pack(pady=10)



canvas.bind("<Button-1>", click_grid)



tk.Label(root, text="1. Выберите цвет 2. Кликните по сетке 3. Нажмите 'Играть всё'", 
         font=("Arial", 9), fg="gray").pack(pady=5)

root.mainloop()


