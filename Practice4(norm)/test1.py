import tkinter as tk

root = tk.Tk()
root.title("Kids Sound Maker")
root.geometry("400x350")


tk.Label(root, text="Задание 1: Работа Сбитневой Дарьи", 
         font=("Arial", 14, "bold"), fg="darkblue").pack(pady=5)

tk.Label(root, text="🎵 Детский оркестр 🎵", 
         font=("Arial", 16, "bold"), fg="blue").pack()


frame = tk.Frame(root)
frame.pack(pady=20)

buttons = [
    ("🥁 Барабан", "red"),
    ("🔔 Колокольчик", "yellow"),
    ("🎹 Пианино", "blue"),
    ("🎵 Флейта", "green"),
    ("🎸 Гитара", "purple"),
    ("🐘 Животное", "orange"),
]

for i, (text, color) in enumerate(buttons):
    row = i // 3
    col = i % 3
    
    btn = tk.Button(
        frame,
        text=text,
        font=("Arial", 10),
        bg=color,
        fg='white',
        width=10,
        height=2,
        command=lambda t=text: play(t)
    )
    btn.grid(row=row, column=col, padx=5, pady=5)




def play(name):
    root.bell()
    status.config(text=f"Играет: {name}")



status = tk.Label(root, text="Нажмите кнопку!")
status.pack(pady=10)

root.mainloop()
   
