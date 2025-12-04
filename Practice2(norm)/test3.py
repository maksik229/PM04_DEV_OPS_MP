import tkinter as tk

class SimpleRadio:
    def __init__(self, root):
        self.root = root
        self.root.title("Задание 3. Сбитнева Д.")
        self.root.geometry("500x350")
        
        self.freq = 88.0
        
        self.setup_ui()
    
    def setup_ui(self):
       
        tk.Label(self.root, text="Задание 3: Шкала радио\nСбитнева Дарья").pack(pady=10)

        self.freq_label = tk.Label(self.root, text="88.0 МГц", font=("Arial", 20))
        self.freq_label.pack()


        self.canvas = tk.Canvas(self.root, width=400, height=150, bg="white")
        self.canvas.pack(pady=10)
        self.draw_scale()
        

        frame = tk.Frame(self.root)
        frame.pack(pady=10)
       
        stations = [88.0, 90.0, 92.0, 94.0, 96.0, 98.0, 100.0, 102.0, 104.0, 106.0]
        for station in stations:
            tk.Button(frame, text=str(station), width=4,
                     command=lambda s=station: self.set_freq(s)).pack(side=tk.LEFT, padx=2)
            

        control_frame = tk.Frame(self.root)
        control_frame.pack(pady=10)
        
        tk.Button(control_frame, text="<", command=lambda: self.set_freq(self.freq-0.1)).pack(side=tk.LEFT, padx=10)
        tk.Button(control_frame, text=">", command=lambda: self.set_freq(self.freq+0.1)).pack(side=tk.LEFT, padx=10)
    
    def draw_scale(self):
        self.canvas.delete("all")
        w, h = 400, 150


        self.canvas.create_line(30, 100, w-30, 100, width=3)
        

        for i in range(88, 109, 2):
            x = 30 + (i-88) * (w-60) / 20
            self.canvas.create_line(x, 95, x, 105, width=2)
            self.canvas.create_text(x, 120, text=str(i))


        x = 30 + (self.freq-88) * (w-60) / 20
        self.canvas.create_polygon(x, 40, x-10, 95, x+10, 95, fill="red")
        self.canvas.create_text(x, 25, text=f"{self.freq:.1f}", font=("Arial", 10, "bold"))
    
    def set_freq(self, new_freq):


        self.freq = max(88.0, min(108.0, new_freq))

        self.freq_label.config(text=f"{self.freq:.1f} МГц")
        self.draw_scale()

root = tk.Tk()
app = SimpleRadio(root)
root.mainloop()