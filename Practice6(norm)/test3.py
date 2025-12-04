import tkinter as tk
import random

root = tk.Tk()
root.title("Задание 3: Работа Сбитневой Дарьи")
root.geometry("450x400")


tk.Label(root, text="Задание 3: Работа Сбитневой Дарьи", 
         font=("Arial", 14, "bold"), fg="blue").pack(pady=5)
tk.Label(root, text="Контрольная сумма 4 байтов").pack()


bytes_data = [0, 0, 0, 0]
original = [0, 0, 0, 0]
bit_labels = []


frame = tk.Frame(root)
frame.pack(pady=10)

for i in range(4):
    byte_frame = tk.Frame(frame)
    byte_frame.grid(row=0, column=i, padx=5)
    tk.Label(byte_frame, text=f"Байт {i+1}").pack()
    
    bits = []
    for j in range(8):
        bit = tk.Label(byte_frame, text="0", width=2, relief="raised")
        bit.pack(side="left", padx=1)
        bits.append(bit)
    bit_labels.append(bits)



def generate():
    for i in range(4):
        byte = random.randint(0, 255)
        bytes_data[i] = byte
        update_byte(i, byte)
    original[:] = bytes_data[:]
    update_info()
    status.config(text="Не изменено", fg="green")

def flip():
    i = random.randint(0, 3)
    j = random.randint(0, 7)
    mask = 1 << (7 - j)
    bytes_data[i] ^= mask
    update_byte(i, bytes_data[i])
    update_info()
    status.config(text="Изменено!", fg="red")

def restore():
    bytes_data[:] = original[:]
    for i in range(4):
        update_byte(i, bytes_data[i])
    update_info()
    status.config(text="Восстановлено", fg="green")

def update_byte(i, byte):
    binary = format(byte, '08b')
    for j in range(8):
        if binary[j] == '1':
            bit_labels[i][j].config(text="1", bg="lightgreen")
        else:
            bit_labels[i][j].config(text="0", bg="lightgray")

def update_info():
    binary = " ".join([format(b, '08b') for b in bytes_data])
    binary_label.config(text=f"Двоичный: {binary}")
    
    checksum = sum(bytes_data)
    decimal_label.config(text=f"Десятичная: {checksum}")
    hex_label.config(text=f"Шестнадцатеричная: 0x{checksum:03X}")



tn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Сгенерировать", command=generate, 
         bg="lightblue", width=12).pack(side="left", padx=5)
tk.Button(btn_frame, text="Изменить бит", command=flip,
         bg="lightyellow", width=12).pack(side="left", padx=5)
tk.Button(btn_frame, text="Восстановить", command=restore,
         bg="lightgreen", width=12).pack(side="left", padx=5)




binary_label = tk.Label(root, font=("Courier", 9))
binary_label.pack(pady=5)

decimal_label = tk.Label(root, font=("Courier", 9))
decimal_label.pack()

hex_label = tk.Label(root, font=("Courier", 9))
hex_label.pack()

status = tk.Label(root, font=("Arial", 10))
status.pack(pady=5)


generate()
root.mainloop()




