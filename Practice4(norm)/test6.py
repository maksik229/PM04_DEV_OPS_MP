import tkinter as tk
import random

root = tk.Tk()
root.title("Повтори мелодию")
root.geometry("400x400")


tk.Label(root, text="Задание 6: Работа Сбитневой Дарьи", 
         font=("Arial", 14, "bold"), fg="darkblue").pack(pady=5)

tk.Label(root, text="🎵 Повтори мелодию", font=("Arial", 16, "bold")).pack()


sequence = []
player = []
level = 1


frame = tk.Frame(root)
frame.pack(pady=10)

colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']
notes = ['До', 'Ре', 'Ми', 'Фа', 'Соль', 'Ля']

buttons = []
for i in range(6):
    btn = tk.Button(
        frame,
        text=notes[i],
        bg=colors[i],
        fg='white',
        width=5,
        height=2,
        state='disabled'
    )
    btn.grid(row=i//3, column=i%3, padx=3, pady=3)
    buttons.append(btn)



status = tk.Label(root, text="Нажми 'Старт'")
status.pack(pady=10)



def start_game():
    global sequence, player, level
    sequence = []
    player = []
    level = 1


    for _ in range(3):
        sequence.append(random.randint(0, 5))



    for btn in buttons:
        btn.config(state='normal', command=lambda idx=buttons.index(btn): tap(idx))
    
    show_seq()
    status.config(text="Слушайте...")
    play_seq()

def show_seq():




    notes_text = " ".join([notes[n] for n in sequence])
    status.config(text=f"Мелодия: {notes_text}")

def play_seq():




    for i, note in enumerate(sequence):
        root.after(i * 500, lambda n=note: highlight(n))
    root.after(len(sequence) * 500, lambda: status.config(text="Повторите!"))

def highlight(note_idx):
    original = colors[note_idx]
    buttons[note_idx].config(bg='white')
    root.bell()  # Звук
    root.after(200, lambda: buttons[note_idx].config(bg=original))

def tap(note_idx):
    root.bell()  # Звук
    player.append(note_idx)






    if len(player) <= len(sequence):
        if player[-1] != sequence[len(player)-1]:
            status.config(text="Ошибка! Нажми 'Старт'", fg="red")
            for btn in buttons:
                btn.config(state='disabled')
        elif len(player) == len(sequence):
            status.config(text="Правильно! Нажми 'Следующий'", fg="green")
    else:
        status.config(text="Слишком много нот!", fg="red")

def next_level():
    global sequence, player, level
    player = []
    level += 1



    sequence.append(random.randint(0, 5))
    
    show_seq()
    status.config(text=f"Уровень {level}. Слушайте...")
    play_seq()



control = tk.Frame(root)
control.pack(pady=10)

tk.Button(control, text="Старт", command=start_game, 
         bg='green', fg='white').pack(side="left", padx=5)

tk.Button(control, text="Следующий", command=next_level,
         bg='blue', fg='white').pack(side="left", padx=5)


tk.Label(root, text="Нажми 'Старт', слушайте, повторяйте", 
         font=("Arial", 9), fg="gray").pack(pady=10)

root.mainloop()

    
    
    




