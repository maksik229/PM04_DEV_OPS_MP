import tkinter as tk
import random

class SimpleElectricSim:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Электрическая симуляция")
        
  
        self.particles = []
        self.running = False


        self.canvas = tk.Canvas(self.root, width=600, height=500, bg='white')
        self.canvas.pack()


        tk.Button(self.root, text="Старт", command=self.start).pack(side=tk.LEFT)
        tk.Button(self.root, text="Стоп", command=self.stop).pack(side=tk.LEFT)
        tk.Button(self.root, text="Добавить", command=self.add).pack(side=tk.LEFT)
        tk.Button(self.root, text="Очистить", command=self.clear).pack(side=tk.LEFT)



        self.add()
    
    def add(self):
        """Добавить частицы"""
        for _ in range(20):
            x = random.randint(50, 550)
            y = random.randint(50, 450)

            if random.random() < 0.5:
                color = 'blue'
                charge = -1
            else:
                color = 'red'
                charge = 1
            
            self.particles.append({
                'x': x, 'y': y,
                'vx': random.uniform(-2, 2),
                'vy': random.uniform(-2, 2),
                'color': color,
                'charge': charge
            })
        
        self.draw()
    
    def clear(self):
        """Очистить всё"""
        self.particles = []
        self.draw()
    
    def draw(self):
        """Нарисовать частицы"""
        self.canvas.delete("all")



        self.canvas.create_rectangle(10, 10, 30, 490, fill='black')
        self.canvas.create_rectangle(570, 10, 590, 490, fill='black')

        for p in self.particles:
            self.canvas.create_oval(p['x']-5, p['y']-5, p['x']+5, p['y']+5, fill=p['color'])
    
    def update(self):
        """Обновить физику"""
        if not self.running:
            return
        
        for p in self.particles:


            p['vx'] += p['charge'] * 0.1



            p['x'] += p['vx']
            p['y'] += p['vy']


            if p['x'] < 40 or p['x'] > 560:
                p['vx'] *= -0.8
                p['x'] = max(40, min(560, p['x']))
            
            if p['y'] < 20 or p['y'] > 480:
                p['vy'] *= -0.8
                p['y'] = max(20, min(480, p['y']))
        
        self.draw()
        self.root.after(50, self.update)
    
    def start(self):
        """Начать"""
        self.running = True
        self.update()
    
    def stop(self):
        """Остановить"""
        self.running = False
    
    def run(self):
        """Запустить"""
        self.root.mainloop()

if __name__ == "__main__":
    sim = SimpleElectricSim()
    sim.run()




        
        