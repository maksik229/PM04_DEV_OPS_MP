import tkinter as tk

size = 12

def change(delta):
    global size 
    if delta > 0 or size > 8:
        size += delta  # Изменяем размер
        label.config(font=("Arial", size)) 

root = tk.Tk()
root.title("Доп. задание - Сбитнева Д.")  
root.geometry("350x250")  

tk.Label(root, text="Доп. задание\nСбитнева Дарья").pack(pady=10)

label = tk.Label(root, text="Пример текста", font=("Arial", size))
label.pack(pady=20)

tk.Button(root, text="Увеличить", command=lambda: change(2)).pack(side=tk.LEFT, padx=40)
tk.Button(root, text="Уменьшить", command=lambda: change(-2)).pack(side=tk.LEFT, padx=40)
root.mainloop()