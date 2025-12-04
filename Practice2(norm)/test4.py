import tkinter as tk
import random

def generate_numbers():
  
    memo.delete(1.0, tk.END)


    count = trackbar.get()

    numbers = [random.randint(1, 1000) for _ in range(count)]

    for i in range(0, count, 10):
        line = " ".join(f"{num:4}" for num in numbers[i:i+10])
        memo.insert(tk.END, line + "\n")
    
    memo.see(1.0)

root = tk.Tk()
root.title("Задание 4 работа Сбитневой Дарьи")
root.geometry("600x500")

title_label = tk.Label(root, 
                      text="Задание 4: Случайные числа в Memo\nРабота Сбитневой Дарьи",
                      font=("Arial", 12, "bold"),
                      fg="blue")
title_label.pack(pady=10)
trackbar_frame = tk.Frame(root)
trackbar_frame.pack(pady=10)
tk.Label(trackbar_frame, text="Количество чисел:", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
count_label = tk.Label(trackbar_frame, text="100", font=("Arial", 10, "bold"))
count_label.pack(side=tk.LEFT, padx=5)

def update_count_label(value):
    count_label.config(text=value)

trackbar = tk.Scale(root, from_=1, to=1000, orient=tk.HORIZONTAL,
                   length=400, command=update_count_label)
trackbar.set(100)  # Начальное значение
trackbar.pack()
generate_button = tk.Button(root, text="Сгенерировать числа", 
                           command=generate_numbers,
                           font=("Arial", 12),
                           bg="lightblue")
generate_button.pack(pady=10)
memo_frame = tk.Frame(root)
memo_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
scrollbar = tk.Scrollbar(memo_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
memo = tk.Text(memo_frame, height=15, width=70,
               yscrollcommand=scrollbar.set,
               font=("Courier New", 10),
               wrap=tk.NONE)  # Не переносить текст
memo.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
stats_label = tk.Label(root, text="Нажмите кнопку для генерации чисел", font=("Arial", 10))
stats_label.pack(pady=5)

root.mainloop()