import tkinter as tk

root = tk.Tk()
root.title("Kids Orchestra")
root.geometry("400x400")


tk.Label(root, text="🎵 Детский оркестр 🎵", 
         font=("Arial", 16, "bold"), fg="blue").pack(pady=10)


frame = tk.Frame(root)
frame.pack(pady=20)


instruments = [
    ("🥁", "Барабан", "red"),
    ("🎹", "Пианино", "blue"),
    ("🔔", "Колокольчик", "yellow"),
    ("🎵", "Флейта", "green"),
    ("🎸", "Гитара", "purple"),
    ("🐘", "Животное", "orange"),
]

buttons = []

for i, (icon, name, color) in enumerate(instruments):
    row = i // 3
    col = i % 3
    
    btn = tk.Button(
        frame,
        text=f"{icon}\n{name}",
        font=("Arial", 10),
        bg=color,
        fg='white',
        width=8,
        height=3,
        command=lambda n=name: play_sound(n)
    )
    btn.grid(row=row, column=col, padx=5, pady=5)
    buttons.append(btn)



def play_sound(name):
    root.bell()  # Простой системный звук
    status.config(text=f"Играет: {name}")



tk.Button(root, text="🎶 Играть всё", 
         command=play_all, bg='green', fg='white', width=15).pack(pady=5)

tk.Button(root, text="✨ Мелодия", 
         command=play_melody, bg='purple', fg='white', width=15).pack(pady=5)


status = tk.Label(root, text="Нажмите на инструменты!")
status.pack(pady=10)


def play_all():
    status.config(text="Играют все инструменты! 🎵")
    for i in range(6):
        root.after(i * 100, root.bell)

def play_melody():
    status.config(text="Играет мелодия! 🎶")
    for i in range(8):
        root.after(i * 150, root.bell)

root.mainloop()


