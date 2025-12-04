import tkinter as tk
import random


root = tk.Tk()
root.title("Задание 1: Работа Сбитневой Дарьи")
root.geometry("450x320")


tk.Label(root, text="Задание 1: Работа Сбитневой Дарьи", 
         font=("Arial", 14, "bold"), fg="blue").pack(pady=5)

tk.Label(root, text="4 случайных байта (32 бита)", 
         font=("Arial", 10)).pack()

bytes_data = [0, 0, 0, 0]
bit_labels = []


frame = tk.Frame(root)
frame.pack(pady=10)

for i in range(4):
    byte_frame = tk.Frame(frame)
    byte_frame.grid(row=0, column=i, padx=5)
    
    tk.Label(byte_frame, text=f"Байт {i+1}").pack()
    
    bits = []
    for j in range(8):
        bit = tk.Label(byte_frame, text="0", width=2, 
                      relief="raised", font=("Arial", 10))
        bit.pack(side="left", padx=1)
        bits.append(bit)
    
    bit_labels.append(bits)


def generate():
    """Генерировать случайные байты"""
    ones = 0
    for i in range(4):
        byte = random.randint(0, 255)
        bytes_data[i] = byte
        binary = format(byte, '08b')
        
        for j in range(8):
            if binary[j] == '1':
                bit_labels[i][j].config(text="1", bg="lightgreen")
                ones += 1
            else:
                bit_labels[i][j].config(text="0", bg="lightgray")
    
    info_label.config(text=f"Десятичные: {bytes_data[0]} {bytes_data[1]} {bytes_data[2]} {bytes_data[3]}\n"
                         f"Единиц: {ones}/32")

def reset():
    """Сбросить все в 0"""
    for i in range(4):
        bytes_data[i] = 0
        for j in range(8):
            bit_labels[i][j].config(text="0", bg="lightgray")
    
    info_label.config(text=f"Десятичные: 0 0 0 0\nЕдиниц: 0/32")


btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Сгенерировать", command=generate, 
         bg="lightblue", width=12).pack(side="left", padx=5)

tk.Button(btn_frame, text="Сбросить", command=reset,
         bg="lightcoral", width=12).pack(side="left", padx=5)


info_label = tk.Label(root, text="Десятичные: 0 0 0 0\nЕдиниц: 0/32",
                     font=("Arial", 10))
info_label.pack(pady=10)


generate()

root.mainloop()




