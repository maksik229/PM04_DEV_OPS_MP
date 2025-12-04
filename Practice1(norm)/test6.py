import tkinter as tk

def show_value(value):
    value_label.config(text=f"Значение: {value}")

root = tk.Tk()
root.title("Задание 6")
root.geometry("300x250")

tk.Label(root, text="Задание 6\nСбитнева Дарья").pack(pady=10)

value_label = tk.Label(root, text="Значение: 50", font=("Arial", 14))
value_label.pack(pady=10)
trackbar = tk.Scale(root, from_=0, to=100, command=show_value)
trackbar.set(50)
trackbar.pack(pady=20)

root.mainloop()