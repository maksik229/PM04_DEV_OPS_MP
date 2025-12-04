import tkinter as tk

# Создаем переменную для хранения счетчика
counter = 0

def increase_counter():
    global counter  # Используем глобальную переменную
    counter += 1  # Увеличиваем счетчик на 1
    counter_label.config(text=str(counter))  # Обновляем текст в Label

root = tk.Tk()
root.title("Задание 3 работа Сбитневой Дарьи ")
root.geometry("300x200")

counter_label = tk.Label(root, text="0", font=("Arial", 48))
counter_label.pack(pady=20)

button = tk.Button(root, text="Нажми меня!", command=increase_counter, font=("Arial", 16))
button.pack(pady=10)

info_label = tk.Label(root, text="Количество нажатий:", font=("Arial", 14))
info_label.pack(pady=5)
root.mainloop()