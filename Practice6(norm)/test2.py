import tkinter as tk
import random


root = tk.Tk()
root.title("Задание 2: Работа Сбитневой Дарьи")
root.geometry("450x450")


tk.Label(root, text="Задание 2: Работа Сбитневой Дарьи", 
         font=("Arial", 14, "bold"), fg="blue").pack(pady=5)

tk.Label(root, text="4 случайных байта (32 бита)", 
         font=("Arial", 10)).pack()

bytes_data = [0, 0, 0, 0]
bit_labels = []


frame = tk.Frame(root)
frame.pack(pady=15)

for i in range(4):
    byte_frame = tk.Frame(frame)
    byte_frame.grid(row=0, column=i, padx=5)
    
    tk.Label(byte_frame, text=f"Байт {i+1}", 
            font=("Arial", 10, "bold")).pack()
    
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
    
    update_formats(ones)

def reset():
    """Сбросить все в 0"""
    for i in range(4):
        bytes_data[i] = 0
        for j in range(8):
            bit_labels[i][j].config(text="0", bg="lightgray")
    
    update_formats(0)

def update_formats(ones):


    binary_text = "Двоичный:      "
    binary_text += " ".join([format(b, '08b') for b in bytes_data])


    decimal_text = "Десятичный:    "
    decimal_text += " ".join([f"{b:3d}" for b in bytes_data])


    hex_text = "Шестнадцатеричный: "
    hex_text += " ".join([f"0x{b:02X}" for b in bytes_data])


    if not hasattr(root, 'format_labels'):
        root.format_labels = []
        
        for text in [binary_text, decimal_text, hex_text]:
            label = tk.Label(format_frame, text=text, 
                           font=("Courier", 9), anchor="w")
            label.pack(anchor="w", pady=2)
            root.format_labels.append(label)
    else:
        texts = [binary_text, decimal_text, hex_text]
        for i, label in enumerate(root.format_labels):
            label.config(text=texts[i])


    ones_label.config(text=f"Единиц: {ones}/32")
    
    # Цвет счетчика
    if ones > 24:
        ones_label.config(fg="darkgreen")
    elif ones > 16:
        ones_label.config(fg="blue")
    elif ones > 8:
        ones_label.config(fg="orange")
    else:
        ones_label.config(fg="red")




btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Сгенерировать", command=generate,
         bg="lightblue", width=15).pack(side="left", padx=5)

tk.Button(btn_frame, text="Сбросить", command=reset,
         bg="lightcoral", width=15).pack(side="left", padx=5)


format_frame = tk.LabelFrame(root, text="Представление данных")
format_frame.pack(pady=10, padx=20, fill="x")


ones_label = tk.Label(root, text="Единиц: 0/32",
                     font=("Arial", 10, "bold"))
ones_label.pack(pady=5)


info_text = "1 байт = 8 бит | Всего: 4 байта = 32 бита | 1=зеленый, 0=серый"
tk.Label(root, text=info_text, font=("Arial", 8), fg="gray").pack(pady=5)


generate()

root.mainloop()



