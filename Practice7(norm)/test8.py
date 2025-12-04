import tkinter as tk
import random
import matplotlib.pyplot as plt

class SimpleChart:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Графики")
        
    
        tk.Button(self.root, text="Столбчатая", command=self.bar_chart).pack()
        tk.Button(self.root, text="Круговая", command=self.pie_chart).pack()
        tk.Button(self.root, text="Случайные данные", command=self.random_data).pack()
        
    def bar_chart(self):

        values = [random.randint(10, 50) for _ in range(5)]
        plt.bar(['A', 'B', 'C', 'D', 'E'], values)
        plt.title("Столбчатый график")
        plt.show()


    def pie_chart(self):


        values = [random.randint(10, 50) for _ in range(5)]
        plt.pie(values, labels=['A', 'B', 'C', 'D', 'E'])
        plt.title("Круговая диаграмма")
        plt.show()


    def random_data(self):
        print("Новые случайные данные созданы")


    def run(self):
        print("Новые случайные данные созданы")



    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = SimpleChart()
    app.run()




        