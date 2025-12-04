import tkinter as tk

def show_greeting():
    label.config(text=f"Привет, Дарья!")

# Создаем главное окно
root = tk.Tk()
root.title("Задание 1 работа Сюитневой Дарьи")
root.geometry("300x150")
# Создаем кнопку
button = tk.Button(root, text="Нажми меня", command=show_greeting)
button.pack(pady=20)
label = tk.Label(root, text="", font=("Arial", 14))
label.pack(pady=20)
root.mainloop()