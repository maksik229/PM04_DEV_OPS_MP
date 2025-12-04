import tkinter as tk
import random

def update_data():
    """Обновляет данные случайными значениями"""
    for i in range(len(labels)):
        name, val = data[i]
        if val == "✔":


            if random.choice([True, False]):
                new_val = str(random.randint(1, 10))
                labels[i].config(text=f"{name:10} {new_val}", fg="black")
                data[i] = (name, new_val)
        else:


            new_val = str(int(val) + random.randint(1, 3))
            labels[i].config(text=f"{name:10} {new_val}", fg="black")
            data[i] = (name, new_val)

def check_status():


    for i in range(len(labels)):
        if random.choice([True, False]):
            name, _ = data[i]
            labels[i].config(text=f"{name:10} ✔", fg="green")
            data[i] = (name, "✔")
    
    status_label.config(text="Статус: Проверка завершена", fg="green")


root = tk.Tk()
root.title("Сбитневая Дарья")
root.geometry("350x250")


data = [("Daily", "4"), ("Weekly", "7"), ("Monthly", "✔"), ("Quarterly", "✔")]
labels = []


tk.Label(root, text="Задание 4: Работа Сбитневой Дарьи", 
         font=("Arial", 12, "bold")).pack(pady=10)


tk.Label(root, text="Maintenance", font=("Arial", 11, "bold")).pack()


for name, val in data:
    label = tk.Label(root, text=f"{name:10} {val}", 
                     fg="green" if val=="✔" else "black")
    label.pack()
    labels.append(label)

tk.Button(root, text="Обновить", bg="lightblue", 
          command=update_data).pack(pady=15)
tk.Button(root, text="Проверить", bg="lightgreen", 
          command=check_status).pack()


status_label = tk.Label(root, text="Статус: Активно", fg="blue")
status_label.pack(pady=10)


root.mainloop()


          