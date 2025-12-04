import tkinter as tk

root = tk.Tk()
root.title("Градусник")
root.geometry("300x400")

# Заголовок
tk.Label(root, text="Задание 2: Работа Сбитневой Дарьи", font=("Arial", 12, "bold")).pack(pady=10)

canvas = tk.Canvas(root, width=100, height=200, bg="white")
canvas.pack()


canvas.create_rectangle(30, 20, 70, 180, fill="lightgray", outline="black")  # Основа
temp_bar = canvas.create_rectangle(30, 150, 70, 180, fill="red", outline="")  # Температура


for i in range(6):
    y = 20 + i * 30
    canvas.create_text(80, y, text=f"{i*20}°C")


temp = 20
temp_label = tk.Label(root, text=f"{temp}°C", font=("Arial", 20, "bold"), fg="red")
temp_label.pack(pady=10)


def change(delta):
    global temp
    temp += delta
    if temp > 100: temp = 100
    if temp < 0: temp = 0
    
    temp_label.config(text=f"{temp}°C")


    y = 180 - temp * 1.6
    canvas.coords(temp_bar, 30, y, 70, 180)

    color = "blue" if temp < 20 else "orange" if temp < 40 else "red"
    canvas.itemconfig(temp_bar, fill=color)
    temp_label.config(fg=color)


btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="-", command=lambda: change(-5), width=5).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="+", command=lambda: change(5), width=5).pack(side=tk.LEFT, padx=5)

root.mainloop()
    
    
    

