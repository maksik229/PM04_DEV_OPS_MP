import tkinter as tk

def update_color(v=None):
    r = red.get()
    g = green.get()
    b = blue.get()
    color = f'#{r:02x}{g:02x}{b:02x}'
    color_box.config(bg=color)
    rgb_label.config(text=f"RGB({r}, {g}, {b})")

root = tk.Tk()
root.title("Задание 8 работа Сбитневой Дарьи")
root.geometry("450x400")
tk.Label(root, text="Задание 8: Цвет по RGB\nСбитнева Дарья", 
        font=("Arial", 12)).pack(pady=10)
color_box = tk.Label(root, width=40, height=5, bg="#808080", relief="solid")
color_box.pack(pady=15)
rgb_label = tk.Label(root, text="RGB(128, 128, 128)", font=("Arial", 12))
rgb_label.pack()

def create_horizontal_slider(label_text, default_value):
    frame = tk.Frame(root)
    frame.pack(pady=5, padx=20, fill="x")
    
    tk.Label(frame, text=label_text, width=8).pack(side=tk.LEFT)
    
    slider = tk.Scale(frame, from_=0, to=255, orient=tk.HORIZONTAL,
                     command=update_color, length=250)
    slider.set(default_value)
    slider.pack(side=tk.LEFT, fill="x", expand=True)
    
    value_label = tk.Label(frame, text=str(default_value), width=4)
    value_label.pack(side=tk.LEFT)
    
    def update_label(val):
        value_label.config(text=val)
    
    slider.config(command=lambda v: (update_label(v), update_color()))
    return slider


red = create_horizontal_slider("Красный:", 128)
green = create_horizontal_slider("Зеленый:", 128)
blue = create_horizontal_slider("Синий:", 128)


tk.Button(root, text="Сброс", 
          command=lambda: (red.set(128), green.set(128), blue.set(128), update_color())
         ).pack(pady=20)

root.mainloop()