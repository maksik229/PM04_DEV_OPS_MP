import tkinter as tk

def add_greeting():
    # Добавляем строку "Привет, Дарья!" в текстовое поле
    memo.insert(tk.END, "Привет, Дарья!\n")

# Создаем окно
root = tk.Tk()
root.title("Задание 2 работа Сбитневой Дарья")
root.geometry("300x200")

# Создаем кнопку
button = tk.Button(root, text="Добавить приветствие", command=add_greeting)
button.pack(pady=10)

# Создаем текстовое поле (Memo)
memo = tk.Text(root, height=8, width=30)
memo.pack(pady=10)
root.mainloop()