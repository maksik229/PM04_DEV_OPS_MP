import tkinter as tk

root = tk.Tk()
root.title("🎨 Музыкальная раскраска")
root.geometry("500x400")


tk.Label(root, text="Задание 2: Работа Сбитневой Дарьи", 
         font=("Arial", 14, "bold"), fg="darkblue").pack(pady=5)

tk.Label(root, text="🎨 Раскраска со звуками 🎵", 
         font=("Arial", 16, "bold"), fg="blue").pack()



colors = {
    'red': '#FF0000',
    'blue': '#0000FF', 
    'green': '#00FF00',
    'yellow': '#FFFF00',
    'purple': '#800080',
    'orange': '#FFA500',
}

current_color = 'red'


def select_color(color_name):
    global current_color
    current_color = color_name
    root.bell()  # Звук при выборе цвета
    info_label.config(text=f"Выбран: {color_name}")



color_frame = tk.Frame(root)
color_frame.pack(pady=10)

row = 0
col = 0
for color_name, color_code in colors.items():
    btn = tk.Button(
        color_frame,
        text="",
        bg=color_code,
        width=6,
        height=2,
        command=lambda c=color_name: select_color(c)
    )
    btn.grid(row=row, column=col, padx=3, pady=3)
    col += 1
    if col > 2:
        col = 0
        row += 1


canvas = tk.Canvas(root, bg='white', width=350, height=200)
canvas.pack(pady=10)



canvas.create_rectangle(50, 50, 300, 150, outline='black', width=2)


def paint(event):
    x, y = event.x, event.y
    if 50 <= x <= 300 and 50 <= y <= 150:  # Только внутри прямоугольника
        canvas.create_oval(x-5, y-5, x+5, y+5, fill=colors[current_color])

canvas.bind("<B1-Motion>", paint)



frame = tk.Frame(root)
frame.pack(pady=10)

tk.Button(frame, text="Очистить", 
         command=lambda: canvas.delete("all") or root.bell(),
         bg='lightgray').pack(side="left", padx=5)

tk.Button(frame, text="Звуки", 
         command=lambda: [root.bell() for _ in range(3)],
         bg='lightblue').pack(side="left", padx=5)





info_label = tk.Label(root, text="Выбран: красный")
info_label.pack(pady=5)


tk.Label(root, text="Выберите цвет и раскрашивайте фигуру!", 
         font=("Arial", 9), fg="gray").pack(pady=5)

root.mainloop()

