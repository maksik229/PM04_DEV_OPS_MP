import tkinter as tk
import random

def generate():
    text.delete(1.0, tk.END)
    for i in range(slider.get()):
        text.insert(tk.END, str(random.randint(1, 1000)) + " ")


root = tk.Tk()
root.title("Задание 6. Сбитнева Д.")  
root.geometry("400x350")  
tk.Label(root, text="Задание 6\nСбитнева Дарья").pack()

slider = tk.Scale(root, from_=1, to=100)  
slider.set(10)  
slider.pack(pady=10)
tk.Button(root, text="Генерировать", command=generate).pack()
text = tk.Text(root, height=10, width=40) 
text.pack(pady=10) 
root.mainloop()