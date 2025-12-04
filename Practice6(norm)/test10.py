import tkinter as tk
import random
import math

root = tk.Tk()
root.title("Задание 10: Работа Сбитневой Дарьи")
root.geometry("500x500")


tk.Label(root, text="Задание 10: Работа Сбитневой Дарьи", 
         font=("Arial", 14, "bold"), fg="blue").pack(pady=5)
tk.Label(root, text="Модуляция: ASK, FSK, PSK").pack()

mod = "ASK"
bits = [1, 0, 1, 1, 0, 0, 1, 0]


canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack(pady=10)


def draw():
    canvas.delete("all")



    for i, bit in enumerate(bits):
        x1 = 50 + i * 40
        x2 = x1 + 30
        y = 50
        color = "green" if bit == 1 else "red"
        canvas.create_rectangle(x1, y, x2, y+20, fill=color)
        canvas.create_text((x1+x2)//2, y+10, text=str(bit))




    points = []
    for i, bit in enumerate(bits):
        x = 50 + i * 40 + 15
        y = 150
        
        if mod == "ASK":



            if bit == 1:
                points.extend([x, y-40, x+20, y-40])
            else:
                points.extend([x, y-20, x+20, y-20])
        
        elif mod == "FSK":




            if bit == 1:
                # Высокая частота
                points.extend([x, y-40, x+5, y-20, x+10, y-40, x+15, y-20, x+20, y-40])
            else:




                points.extend([x, y-20, x+10, y-40, x+20, y-20])
        
        elif mod == "PSK":



            if bit == 1:
                points.extend([x, y-40, x+10, y-20, x+20, y-40])
            else:
                points.extend([x, y-20, x+10, y-40, x+20, y-20])
    
    if points:
        canvas.create_line(points, fill="blue", width=2)






    canvas.create_text(200, 20, text=f"Тип модуляции: {mod}")
    canvas.create_text(200, 280, text=f"Биты: {bits}")



frame = tk.Frame(root)
frame.pack(pady=10)

tk.Button(frame, text="ASK", command=lambda: set_mod("ASK"), 
         bg="lightblue", width=8).pack(side="left", padx=5)
tk.Button(frame, text="FSK", command=lambda: set_mod("FSK"),
         bg="lightblue", width=8).pack(side="left", padx=5)
tk.Button(frame, text="PSK", command=lambda: set_mod("PSK"),
         bg="lightblue", width=8).pack(side="left", padx=5)

tk.Button(frame, text="Случайные биты", command=random_bits,
         bg="lightgreen", width=12).pack(side="left", padx=5)
tk.Button(frame, text="Обновить", command=draw,
         bg="yellow", width=8).pack(side="left", padx=5)



def set_mod(m):
    global mod
    mod = m
    draw()

def random_bits():
    global bits
    bits = [random.randint(0, 1) for _ in range(8)]
    draw()





info = """ASK: разная амплитуда (зеленый=1, красный=0)
FSK: разная частота
PSK: разная фаза"""
tk.Label(root, text=info, font=("Arial", 8)).pack(pady=5)



draw()

root.mainloop()


    

