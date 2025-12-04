import tkinter as tk

root = tk.Tk()
root.title("Заряд батареи")
root.geometry("250x300")

# Заголовок
tk.Label(root, text="Задание 4: Работа Сбитневой Дарьи").pack(pady=10)


canvas = tk.Canvas(root, width=150, height=80, bg="white")
canvas.pack()


canvas.create_rectangle(20, 20, 130, 60, width=2)
canvas.create_rectangle(130, 30, 140, 50, fill="black")

charge = canvas.create_rectangle(22, 22, 82, 58, fill="green")  # 50%


percent = 50
label = tk.Label(root, text=f"{percent}%", font=("Arial", 20))
label.pack(pady=10)


def set_charge(p):
    global percent
    percent = p
    label.config(text=f"{percent}%")


    width = 22 + percent * 1.08  # 100% = 130
    canvas.coords(charge, 22, 22, width, 58)


    color = "green" if p > 50 else "orange" if p > 20 else "red"
    canvas.itemconfig(charge, fill=color)
    label.config(fg=color)

for p in [0, 25, 50, 75, 100]:
    color = "green" if p > 50 else "orange" if p > 20 else "red"
    tk.Button(root, text=f"{p}%", bg=color, fg="white",
              command=lambda v=p: set_charge(v)).pack(side=tk.LEFT, padx=5)

root.mainloop()

