import tkinter as tk
import random

def generate():
    max_val = slider.get()
    num = random.randint(1, max_val)
    number_label.config(text=str(num))

def toggle_timer():
    global timer_running
    if not timer_running:
        timer_running = True
        timer_btn.config(text="Стоп", bg="red")
        update_timer()
    else:
        timer_running = False
        timer_btn.config(text="Старт", bg="green")

def update_timer():
    if timer_running:
        generate()
        interval = speed.get()
        root.after(interval, update_timer)


root = tk.Tk()
root.title("Задание 5. Сбитнева Д.")
root.geometry("400x350")

timer_running = False

tk.Label(root, text="Задание 5\nСбитнева Дарья", font=("Arial", 12)).pack(pady=10)

tk.Label(root, text="Максимальное число:").pack()
slider = tk.Scale(root, from_=10, to=500, orient=tk.HORIZONTAL)
slider.set(100)
slider.pack(pady=10)

number_label = tk.Label(root, text="0", font=("Arial", 48))
number_label.pack(pady=20)
frame = tk.Frame(root)
frame.pack(pady=10)
tk.Button(frame, text="Случайное", command=generate).pack(side=tk.LEFT, padx=5)
timer_btn = tk.Button(frame, text="Старт", command=toggle_timer, bg="green")
timer_btn.pack(side=tk.LEFT, padx=5)
tk.Label(root, text="Скорость (мс):").pack()
speed = tk.Scale(root, from_=100, to=1000, orient=tk.HORIZONTAL)
speed.set(500)
speed.pack()
generate()

root.mainloop()