import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrow
from matplotlib.widgets import Button

class ElectricFieldSimulator:
    def __init__(self):
       
        self.fig, self.ax = plt.subplots(figsize=(10, 8))
        plt.title('Симулятор электрических полей')
        
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-10, 10)
        self.ax.grid(True, alpha=0.3)



        self.charges = []  # (x, y, q, circle, text)
        self.dragging = None
        self.show_field = True



        self.setup_buttons()





        self.fig.canvas.mpl_connect('button_press_event', self.on_click)
        self.fig.canvas.mpl_connect('button_release_event', self.on_release)
        self.fig.canvas.mpl_connect('motion_notify_event', self.on_move)




        self.add_charge(2, 2, 1)
        self.add_charge(-2, -2, -1)
        
        self.update()
    
    def setup_buttons(self):
        """Создание кнопок"""
        plt.subplots_adjust(bottom=0.2)





        btn_ax = plt.axes([0.1, 0.05, 0.15, 0.06])
        self.btn_plus = Button(btn_ax, '+ Заряд', color='red')
        self.btn_plus.on_clicked(lambda e: self.add_random_charge(1))
        
        btn_ax2 = plt.axes([0.3, 0.05, 0.15, 0.06])
        self.btn_minus = Button(btn_ax2, '- Заряд', color='blue')
        self.btn_minus.on_clicked(lambda e: self.add_random_charge(-1))




        btn_ax3 = plt.axes([0.5, 0.05, 0.15, 0.06])
        self.btn_clear = Button(btn_ax3, 'Очистить', color='gray')
        self.btn_clear.on_clicked(self.clear)
    
    def add_charge(self, x, y, q):
        """Добавить заряд"""
        color = 'red' if q > 0 else 'blue'
        circle = Circle((x, y), 0.3, color=color, alpha=0.8)
        self.ax.add_patch(circle)
        
        sign = '+' if q > 0 else '-'
        text = self.ax.text(x, y, sign, ha='center', va='center', 
                           fontsize=12, color='white')
        
        self.charges.append([x, y, q, circle, text])
    
    def add_random_charge(self, q):
        """Добавить случайный заряд"""
        x, y = np.random.uniform(-8, 8, 2)
        self.add_charge(x, y, q)
        self.update()
    
    def clear(self, event=None):
        """Очистить все"""
        for _, _, _, circle, text in self.charges:
            circle.remove()
            text.remove()
        self.charges.clear()
        self.update()
    
    def calculate_field(self, x, y):
        """Рассчитать поле в точке"""
        Ex, Ey = 0, 0
        for cx, cy, q, _, _ in self.charges:
            dx, dy = x - cx, y - cy
            r = np.sqrt(dx**2 + dy**2)
            if r > 0.5:
                E = 9e9 * abs(q) / (r**2)
                if q > 0:
                    Ex += E * dx / r
                    Ey += E * dy / r
                else:
                    Ex -= E * dx / r
                    Ey -= E * dy / r
        return Ex, Ey
    
    def update(self):


        for artist in self.ax.collections[:]:
            artist.remove()




        if self.show_field:
            for x in np.linspace(-9, 9, 15):
                for y in np.linspace(-9, 9, 15):
                    Ex, Ey = self.calculate_field(x, y)
                    mag = np.sqrt(Ex**2 + Ey**2)
                    if mag > 0:
                        dx, dy = Ex/mag*0.3, Ey/mag*0.3
                        arrow = FancyArrow(x, y, dx, dy, width=0.08, color='green', alpha=0.6)
                        self.ax.add_patch(arrow)
        
        self.fig.canvas.draw()
    
    def find_charge(self, x, y):
        """Найти заряд в точке"""
        for i, (cx, cy, _, _, _) in enumerate(self.charges):
            if np.sqrt((x-cx)**2 + (y-cy)**2) <= 0.3:
                return i
        return -1
    
    def on_click(self, event):
        """Обработка клика"""
        if event.inaxes != self.ax: return
        
        idx = self.find_charge(event.xdata, event.ydata)
        
        if event.button == 1:  # Левый клик
            self.dragging = idx if idx >= 0 else None
        
        elif event.button == 3 and idx >= 0:  # Правый клик - удалить
            _, _, _, circle, text = self.charges[idx]
            circle.remove()
            text.remove()
            self.charges.pop(idx)
            self.update()
    
    def on_release(self, event):
        """Отпустили кнопку"""
        self.dragging = None
    
    def on_move(self, event):
        """Движение мыши"""
        if self.dragging is not None and event.inaxes == self.ax:
            self.charges[self.dragging][0] = event.xdata
            self.charges[self.dragging][1] = event.ydata
            self.charges[self.dragging][3].center = (event.xdata, event.ydata)
            self.charges[self.dragging][4].set_position((event.xdata, event.ydata))
            self.update()
    
    def run(self):
        """Запустить"""
        plt.show()

if __name__ == "__main__":
    print("Симулятор электрических полей")
    print("Левый клик - перемещать, Правый клик - удалять")
    sim = ElectricFieldSimulator()
    sim.run()
        
        
        