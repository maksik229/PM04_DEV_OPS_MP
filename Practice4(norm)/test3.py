import tkinter as tk
import random

root = tk.Tk()
root.title("🎵 Угадай звук")
root.geometry("400x400")


tk.Label(root, text="Задание 3: Работа Сбитневой Дарьи", 
         font=("Arial", 14, "bold"), fg="darkblue").pack(pady=5)

tk.Label(root, text="🎵 Угадай животное по звуку", 
         font=("Arial", 16, "bold"), fg="blue").pack()


animals = [
    ("🐱", "Кошка"),
    ("🐶", "Собака"),
    ("🐮", "Корова"),
    ("🐔", "Курица"),
    ("🐸", "Лягушка"),
    ("🚗", "Машина")
]

score = 0
current_animal = None


score_label = tk.Label(root, text=f"Счёт: {score}", font=("Arial", 12))
score_label.pack(pady=5)


tk.Button(root, text="🔊 Играть звук", font=("Arial", 12),
         command=lambda: play_sound(),
         bg="lightblue").pack(pady=10)



frame = tk.Frame(root)
frame.pack(pady=10)

buttons = []
for i, (emoji, name) in enumerate(animals):
    btn = tk.Button(
        frame,
        text=emoji,
        font=("Arial", 14),
        width=4,
        height=2,
        command=lambda n=name: check_answer(n)
    )
    btn.grid(row=i//3, column=i%3, padx=5, pady=5)
    buttons.append(btn)

result_label = tk.Label(root, text="Нажми 'Играть звук'!", font=("Arial", 12))
result_label.pack(pady=10)



def play_sound():
    global current_animal
    current_animal = random.choice(animals)[1]
    root.bell()  # Простой звук
    result_label.config(text="Что это за звук?")

def check_answer(answer):
    global score
    
    if not current_animal:
        result_label.config(text="Сначала нажми 'Играть звук'!")
        return
    
    if answer == current_animal:
        score += 5
        result_label.config(text=f"✅ Правильно! Это {current_animal}", fg="green")
        root.bell()  # Радостный звук
    else:
        result_label.config(text=f"❌ Нет, это {current_animal}", fg="red")
    
    score_label.config(text=f"Счёт: {score}")



tk.Button(root, text="🔄 Новая игра", 
         command=lambda: new_game(),
         bg="lightgreen").pack(pady=10)

def new_game():
    global score, current_animal
    score = 0
    current_animal = None
    score_label.config(text=f"Счёт: {score}")
    result_label.config(text="Нажми 'Играть звук'!")



tk.Label(root, text="1. Нажми 'Играть звук' 2. Выбери животное", 
         font=("Arial", 9), fg="gray").pack(pady=5)

root.mainloop()


