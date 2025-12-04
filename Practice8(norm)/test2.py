import tkinter as tk
import random

class SimpleEWBGenerator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Генератор EWB")
        self.window.geometry("400x350")
        
      
        tk.Label(self.window, text="Задание 2 - Сбитнева Дарья", 
                font=("Arial", 12, "bold")).pack(pady=10)
        

        tk.Label(self.window, text="Шаг времени (сек):").pack()
        self.time_entry = tk.Entry(self.window)
        self.time_entry.pack()
        self.time_entry.insert(0, "0.001")
        
        tk.Label(self.window, text="Количество бит:").pack()
        self.bits_entry = tk.Entry(self.window)
        self.bits_entry.pack()
        self.bits_entry.insert(0, "8")
        
        tk.Label(self.window, text="Биты (0/1 через пробел):").pack()
        self.manual_entry = tk.Entry(self.window, width=30)
        self.manual_entry.pack()
        self.manual_entry.insert(0, "1 0 1 0 1 0 1 0")



        tk.Button(self.window, text="Создать случайные биты", 
                 command=self.random_bits, bg="lightblue").pack(pady=5)
        
        tk.Button(self.window, text="Создать файл EWB", 
                 command=self.create_file, bg="lightgreen", font=("Arial", 11)).pack(pady=10)
        


        self.status = tk.Label(self.window, text="Готов")
        self.status.pack()
    
    def random_bits(self):
        """Создать случайные биты"""
        try:
            count = int(self.bits_entry.get())
            bits = [str(random.randint(0, 1)) for _ in range(count)]
            self.manual_entry.delete(0, tk.END)
            self.manual_entry.insert(0, " ".join(bits))
        except:
            pass
    
    def create_file(self):
        """Создать файл EWB"""
        try:


            time_step = float(self.time_entry.get())
            bit_str = self.manual_entry.get()
            bits = [int(b) for b in bit_str.split()]


            filename = "ewb_signal.txt"
            
            with open(filename, 'w') as f:
                f.write("Time\tV1\n")
                
                current_time = 0.0
                for i in range(len(bits)):
                    voltage = 5 if bits[i] == 1 else 0
                    f.write(f"{current_time:.3f}\t{voltage}\n")
                    current_time += time_step




            self.status.config(text=f"Файл '{filename}' создан!", fg="green")



            print("Создан файл EWB:")
            print(f"Биты: {bits}")
            print(f"Файл: {filename}")
            
        except:
            self.status.config(text="Ошибка! Проверьте ввод", fg="red")
    
    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = SimpleEWBGenerator()
    app.run()
            
            
        