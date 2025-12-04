import tkinter as tk
import base64

root = tk.Tk()
root.title("Задание 11: Работа Сбитневой Дарьи")
root.geometry("500x500")


tk.Label(root, text="Задание 11: Работа Сбитневой Дарьи", 
         font=("Arial", 14, "bold"), fg="blue").pack(pady=5)


tk.Label(root, text="Текст:").pack()
input_text = tk.Text(root, height=4, width=50)
input_text.pack()
input_text.insert("1.0", "Привет")


enc_var = tk.StringVar(value="UTF-8")
encodings = ["UTF-8", "Windows-1251", "KOI8-R", "ISO-8859-1", "ASCII", "Base64"]

frame = tk.Frame(root)
frame.pack()
for enc in encodings:
    tk.Radiobutton(frame, text=enc, variable=enc_var, 
                  value=enc).pack(side="left")
    


def convert():
    text = input_text.get("1.0", "end-1c")
    enc = enc_var.get()
    
    try:
        if enc == "Base64":
            result = base64.b64encode(text.encode()).decode()
            data = text.encode()
        elif enc == "ASCII":
            result = text.encode('ascii', 'replace').decode()
            data = result.encode()
        else:
            enc_map = {"UTF-8": "utf-8", "Windows-1251": "cp1251", 
                      "KOI8-R": "koi8-r", "ISO-8859-1": "iso-8859-1"}
            result = text.encode(enc_map[enc], 'replace').decode(enc_map[enc])
            data = text.encode(enc_map[enc], 'replace')
        
        binary = " ".join(f"{b:08b}" for b in data)
        hex_val = " ".join(f"{b:02X}" for b in data)
        
    except Exception as e:
        result = f"Ошибка: {e}"
        binary = hex_val = ""
    
    result_label.config(text=f"Результат: {result}")
    binary_label.config(text=f"Двоичное: {binary[:100]}..." if len(binary) > 100 else f"Двоичное: {binary}")
    hex_label.config(text=f"Шестнадцатеричное: {hex_val[:100]}..." if len(hex_val) > 100 else f"Шестнадцатеричное: {hex_val}")



tk.Button(root, text="Конвертировать", command=convert,
         bg="lightblue").pack(pady=10)




result_label = tk.Label(root, text="", wraplength=400)
result_label.pack()

binary_label = tk.Label(root, text="", wraplength=400, font=("Courier", 8))
binary_label.pack(pady=5)

hex_label = tk.Label(root, text="", wraplength=400, font=("Courier", 8))
hex_label.pack()





tk.Label(root, text="UTF-8, Windows-1251, KOI8-R, ISO-8859-1, ASCII, Base64", 
         font=("Arial", 8), fg="gray").pack(pady=10)



input_text.bind("<KeyRelease>", lambda e: convert())


convert()

root.mainloop()


