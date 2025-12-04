import tkinter as tk
import random
import matplotlib.pyplot as plt

class SimpleChartApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Простой график")
        self.root.geometry("800x600")
        
      
        self.categories = ['A', 'B', 'C', 'D', 'E']
        self.values = [25, 40, 30, 35, 20]


        self.create_widgets()
        
    def create_widgets(self):


        btn_frame = tk.Frame(self.root)
        btn_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)
        
        tk.Button(btn_frame, text="Столбчатая", command=self.show_bar).pack(pady=5)
        tk.Button(btn_frame, text="Круговая", command=self.show_pie).pack(pady=5)
        tk.Button(btn_frame, text="Случайные данные", command=self.random_data).pack(pady=5)
        tk.Button(btn_frame, text="Сохранить", command=self.save_chart).pack(pady=5)


        input_frame = tk.Frame(self.root)
        input_frame.pack(side=tk.LEFT, padx=10)
        
        tk.Label(input_frame, text="Данные (через запятую):").pack()
        self.data_entry = tk.Entry(input_frame, width=30)
        self.data_entry.pack(pady=5)
        self.data_entry.insert(0, "25,40,30,35,20")
        
        tk.Button(input_frame, text="Применить", command=self.apply_data).pack(pady=5)
    
    def show_bar(self):
        """Показать столбчатую диаграмму"""
        plt.figure(figsize=(8, 6))
        plt.bar(self.categories, self.values, color=['blue', 'red', 'green', 'orange', 'purple'])
        plt.title("Столбчатая диаграмма")
        plt.xlabel("Категории")
        plt.ylabel("Значения")
        plt.grid(True, alpha=0.3)
        plt.show()
    
    def show_pie(self):
        """Показать круговую диаграмму"""
        plt.figure(figsize=(8, 6))
        plt.pie(self.values, labels=self.categories, autopct='%1.1f%%')
        plt.title("Круговая диаграмма")
        plt.show()
    
    def random_data(self):
        """Случайные данные"""
        self.values = [random.randint(10, 100) for _ in range(5)]
        self.update_display()
        print("Созданы новые случайные данные:", self.values)
    
    def apply_data(self):
        """Применить введенные данные"""
        try:
            data = self.data_entry.get()
            self.values = [float(x.strip()) for x in data.split(',')]
            self.update_display()
        except:
            print("Ошибка в данных. Используйте формат: 10,20,30,40,50")
    
    def update_display(self):
        """Обновить поле ввода"""
        self.data_entry.delete(0, tk.END)
        self.data_entry.insert(0, ", ".join(map(str, self.values)))
    
    def save_chart(self):
        """Сохранить текущий график"""
        plt.figure(figsize=(8, 6))
        plt.bar(self.categories, self.values)
        plt.title("Сохраненный график")
        plt.savefig('chart.png')
        print("График сохранен как chart.png")
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = SimpleChartApp()
    app.run()
        
        