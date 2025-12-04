import tkinter as tk

class SimpleToggle:
    def __init__(self, root):
        self.root = root
        self.root.title("Задание 2. Сбитнева Д.")
        self.root.geometry("300x300")
        
        self.state = False  # False = Выкл, True = Вкл
        
        self.create_widgets()
    
    def create_widgets(self):
        tk.Label(self.root, text="Задание 2: Переключатель\nСбитнева Дарья").pack(pady=10)
        
        self.status = tk.Label(self.root, text="ВЫКЛ", fg="red", font=("Arial", 14))
        self.status.pack(pady=20)
        
        
        self.canvas = tk.Canvas(self.root, width=150, height=70, bg="lightgray")
        self.canvas.pack()
        self.draw_button()
        
        self.canvas.bind("<Button-1>", self.toggle)
        
        self.counter = 0
        self.counter_label = tk.Label(self.root, text="Переключений: 0")
        self.counter_label.pack(pady=10)
    
    def draw_button(self):
        self.canvas.delete("all")

        color = "green" if self.state else "red"
        self.canvas.create_rectangle(10, 10, 140, 60, fill=color)

        circle_x = 120 if self.state else 30
        self.canvas.create_oval(circle_x-20, 20, circle_x+20, 50, fill="white")

        text = "ON" if self.state else "OFF"
        self.canvas.create_text(75, 35, text=text, fill="white", font=("Arial", 12, "bold"))
    def toggle(self, event):
        self.state = not self.state
        self.draw_button()
        
        self.status.config(text="ВКЛ" if self.state else "ВЫКЛ", 
                          fg="green" if self.state else "red")
        
        self.counter += 1
        self.counter_label.config(text=f"Переключений: {self.counter}")


root = tk.Tk()
app = SimpleToggle(root)
root.mainloop()
        
        
       