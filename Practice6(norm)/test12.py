import tkinter as tk
import random

root = tk.Tk()
root.title("Задание 12: Работа Сбитневой Дарьи")
root.geometry("400x400")

tk.Label(root, text="Задание 12: Работа Сбитневой Дарьи", 
         font=("Arial", 12, "bold"), fg="blue").pack(pady=5)
tk.Label(root, text="Искажение битов в тексте").pack()


text = "Привет, мир!"
distorted = ""


def distort(n):
    global distorted
    bytes_data = bytearray(text.encode())
    
    for _ in range(n):
        if bytes_data:
            idx = random.randint(0, len(bytes_data)-1)
            bit = random.randint(0, 7)
            bytes_data[idx] ^= (1 << bit)
    
    try:
        distorted = bytes_data.decode()
    except:
        distorted = bytes_data.decode(errors='replace')
    
    update()

def reset():
    global distorted
    distorted = ""
    update()



tk.Label(root, text="Оригинал:", font=("Arial", 9, "bold")).pack(pady=5)
orig_label = tk.Label(root, text=text, bg="lightgreen", padx=10, pady=5)
orig_label.pack()

tk.Label(root, text="Искаженный:", font=("Arial", 9, "bold")).pack(pady=5)
dist_label = tk.Label(root, text="", bg="lightcoral", padx=10, pady=5)
dist_label.pack()



frame = tk.Frame(root)
frame.pack(pady=10)

tk.Button(frame, text="1 бит", command=lambda: distort(1),
         bg="lightblue", width=6).pack(side="left", padx=2)
tk.Button(frame, text="5 битов", command=lambda: distort(5),
         bg="lightblue", width=6).pack(side="left", padx=2)
tk.Button(frame, text="10 битов", command=lambda: distort(10),
         bg="lightblue", width=6).pack(side="left", padx=2)

tk.Button(root, text="Сбросить", command=reset,
         bg="lightgreen", width=10).pack(pady=5)




def update():
    orig_label.config(text=text)
    dist_label.config(text=distorted if distorted else "(нажмите кнопку)")




tk.Label(root, text="Инвертирование битов меняет текст", 
         font=("Arial", 8), fg="gray").pack(pady=10)

update()

root.mainloop()

