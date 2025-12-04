import tkinter as tk
import random

class SimpleFileGenerator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Генератор файлов")
        self.window.geometry("400x300")
        
        
        tk.Label(self.window, text="Задание 3 - Сбитнева Дарья", 
                font=("Arial", 12, "bold")).pack(pady=10)
        


        tk.Label(self.window, text="Количество строк:").pack()
        self.row_entry = tk.Entry(self.window)
        self.row_entry.pack()
        self.row_entry.insert(0, "10")
        
        tk.Label(self.window, text="Значения (через пробел):").pack()
        self.values_entry = tk.Entry(self.window, width=40)
        self.values_entry.pack()
        self.values_entry.insert(0, "10 20 30 40 50 60 70 80 90 100")



        tk.Button(self.window, text="Случайные значения", 
                 command=self.random_values).pack(pady=5)
        
        tk.Button(self.window, text="Создать файлы", 
                 command=self.create_files, bg="lightblue").pack(pady=10)
        



        self.status = tk.Label(self.window, text="Готов")
        self.status.pack()
    
    def random_values(self):
        """Создать случайные значения"""
        try:
            count = int(self.row_entry.get())
            values = [str(random.randint(0, 100)) for _ in range(count)]
            self.values_entry.delete(0, tk.END)
            self.values_entry.insert(0, " ".join(values))
        except:
            pass
    
    def create_files(self):
        """Создать текстовые файлы"""
        try:




            count = int(self.row_entry.get())
            values_str = self.values_entry.get()
            values = values_str.split()


            if len(values) > count:
                values = values[:count]
            elif len(values) < count:
                values = values + ["0"] * (count - len(values))


            
            with open("table.txt", "w", encoding="utf-8") as f:
                f.write("Таблица измерений\n")
                f.write("=" * 30 + "\n")
                f.write("Номер | Результат\n")
                f.write("-" * 30 + "\n")
                
                for i, val in enumerate(values, 1):
                    f.write(f"{i:5} | {val:>8}\n")



            
            with open("table.csv", "w", encoding="utf-8") as f:
                f.write("Номер измерения,Результат\n")
                for i, val in enumerate(values, 1):
                    f.write(f"{i},{val}\n")






            self.status.config(text="Файлы table.txt и table.csv созданы!", fg="green")

            print("Созданы файлы:")
            print("1. table.txt - таблица для просмотра")
            print("2. table.csv - данные для Excel")
            print(f"Значения: {values}")
            
        except:
            self.status.config(text="Ошибка! Проверьте ввод", fg="red")
    
    def run(self):
        self.window.mainloop()



if __name__ == "__main__":
    app = SimpleFileGenerator()
    app.run()

        
        