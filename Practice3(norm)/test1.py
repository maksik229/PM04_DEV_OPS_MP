import tkinter as tk
from datetime import datetime

class SimpleControlPanel:
    def __init__(self, root):
        self.root = root
        self.root.title("Задание 1. Сбитнева Д.")
        self.root.geometry("400x450")
        
        self.status = "Offline"
        self.setup_ui()
    
    def setup_ui(self):
        
        tk.Label(self.root, text="Задание 1: Панель управления\nСбитнева Дарья").pack(pady=10)


        self.status_label = tk.Label(self.root, text="OFFLINE", font=("Arial", 16), fg="red")
        self.status_label.pack(pady=10)

        self.indicator = tk.Canvas(self.root, width=40, height=40, bg="gray")
        self.indicator.pack()
        self.indicator.create_oval(5, 5, 35, 35, fill="gray")

        frame = tk.Frame(self.root)
        frame.pack(pady=15)
        
        tk.Button(frame, text="Start", command=self.start, bg="lightgreen", width=8).pack(side=tk.LEFT, padx=2)
        tk.Button(frame, text="Pause", command=self.pause, bg="lightyellow", width=8).pack(side=tk.LEFT, padx=2)
        tk.Button(frame, text="Stop", command=self.stop, bg="lightcoral", width=8).pack(side=tk.LEFT, padx=2)
        tk.Button(frame, text="Offline", command=self.offline, bg="lightgray", width=8).pack(side=tk.LEFT, padx=2)



        tk.Label(self.root, text="Датчики:").pack()
        sensors_frame = tk.Frame(self.root)
        sensors_frame.pack(pady=5)
        
        self.temp_label = tk.Label(sensors_frame, text="Температура: 25°C")
        self.temp_label.pack()
        self.speed_label = tk.Label(sensors_frame, text="Обороты: 0 об/мин")
        self.speed_label.pack()


        tk.Label(self.root, text="Лог событий:").pack()
        self.log_text = tk.Text(self.root, height=6, width=40)
        self.log_text.pack(pady=5)
        
        self.add_log("Система запущена")
    
    def update_status(self, new_status):
        self.status = new_status
        colors = {"Offline": "red", "Start": "orange", "Run": "green", "Pause": "orange", "Stop": "red"}
        self.status_label.config(text=new_status.upper(), fg=colors.get(new_status, "black"))
        


        ind_colors = {"Offline": "gray", "Start": "yellow", "Run": "green", "Pause": "orange", "Stop": "red"}
        self.indicator.delete("all")
        self.indicator.create_oval(5, 5, 35, 35, fill=ind_colors.get(new_status, "gray"))
    
    def start(self):
        self.update_status("Start")
        self.add_log("Запуск")
        self.root.after(2000, self.run)  # Через 2 секунды -> Run
    
    def run(self):
        if self.status == "Start":
            self.update_status("Run")
            self.add_log("Работа")
    
    def pause(self):
        self.update_status("Pause")
        self.add_log("Пауза")
    
    def stop(self):
        self.update_status("Stop")
        self.add_log("Стоп")
    
    def offline(self):
        self.update_status("Offline")
        self.add_log("Оффлайн")
    
    def add_log(self, message):
        time = datetime.now().strftime("%H:%M:%S")
        self.log_text.insert(tk.END, f"[{time}] {message}\n")
        self.log_text.see(tk.END)



root = tk.Tk()
app = SimpleControlPanel(root)
root.mainloop()

       


        
       