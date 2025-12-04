import tkinter as tk
import random
import threading
import time

class AutoUpdateApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Сбитневая Дарья - Статус работы")
        self.root.geometry("500x400")
        self.root.configure(bg='#f0f0f0')
        
        # Исходные данные
        self.data = {
            "Пакеты в обработке": 7,
            "Загруженные образцы": 9, 
            "Тесты завершены": 32
        }
        
        # Создаем переменные для хранения ссылок на виджеты
        self.value_labels = {}
        self.is_running = True
        
        self.setup_ui()
        self.start_auto_update()
        
    def setup_ui(self):
        # Заголовок
        title_label = tk.Label(self.root, 
                               text="Задание 2: Работа Сбитневой Дарьи", 
                               font=("Arial", 16, "bold"),
                               bg='#f0f0f0',
                               fg='#333333')
        title_label.pack(pady=20)
        
        # Создаем рамку для отображения статуса
        status_frame = tk.Frame(self.root, bg='white', relief=tk.RAISED, borderwidth=3)
        status_frame.pack(pady=20, padx=40, fill=tk.BOTH, expand=True)
        
        # Заголовок внутри рамки
        frame_title = tk.Label(status_frame, 
                              text="Текущий ", 
                              font=("Arial", 14, "bold"),
                              bg='white',
                              fg='#2c3e50')
        frame_title.pack(pady=15)
        
        # Создаем стилизованные блоки для каждой метрики
        metrics = [
            {"title": "Пакеты в обработке", "color": "#3498db"},
            {"title": "Загруженные образцы", "color": "#2ecc71"},
            {"title": "Тесты завершены", "color": "#e74c3c"}
        ]
        
        # Отображаем каждую метрику
        for metric in metrics:
            metric_frame = tk.Frame(status_frame, bg='white')
            metric_frame.pack(pady=10, padx=20, fill=tk.X)
            
            # Название метрики
            title_label = tk.Label(metric_frame,
                                  text=metric["title"],
                                  font=("Arial", 12),
                                  bg='white',
                                  fg='#34495e')
            title_label.pack(side=tk.LEFT)
            
            # Значение метрики
            value = self.data[metric["title"]]
            value_label = tk.Label(metric_frame,
                                  text=str(value),
                                  font=("Arial", 14, "bold"),
                                  bg='white',
                                  fg=metric["color"])
            value_label.pack(side=tk.RIGHT)
            
            # Сохраняем ссылку на метку
            self.value_labels[metric["title"]] = value_label
        
        # Панель управления
        control_frame = tk.Frame(self.root, bg='#f0f0f0')
        control_frame.pack(pady=10)
        
        # Кнопка остановки/запуска автообновления
        self.update_btn = tk.Button(control_frame,
                                   text="⏸ Остановить автообновление",
                                   command=self.toggle_auto_update,
                                   bg="#4CAF50",
                                   fg="white",
                                   font=("Arial", 10))
        self.update_btn.pack(pady=5)
        
        # Кнопка ручного обновления
        tk.Button(control_frame,
                 text="🔄 Обновить сейчас",
                 command=self.manual_update,
                 bg="#2196F3",
                 fg="white",
                 font=("Arial", 10)).pack(pady=5)
        
        # Информационная панель
        info_frame = tk.Frame(self.root, bg='#e8f4f8', relief=tk.GROOVE, borderwidth=2)
        info_frame.pack(pady=10, padx=40, fill=tk.X)
        
        self.info_label = tk.Label(info_frame,
                                 text="🔄 Автообновление включено. Следующее обновление через 2 сек...",
                                 font=("Arial", 9),
                                 bg='#e8f4f8',
                                 fg='#2c3e50',
                                 wraplength=400)
        self.info_label.pack(pady=8)
        
        # Статусная строка
        self.status_label = tk.Label(self.root,
                                   text="Статус: Активно | Последнее обновление: --:--:--",
                                   font=("Arial", 8),
                                   bg='#f0f0f0',
                                   fg='#7f8c8d')
        self.status_label.pack(pady=5)
        
        # Футер
        footer_label = tk.Label(self.root,
                               text="© Сбитневая Дарья - Система мониторинга (Автообновление)",
                               font=("Arial", 8),
                               bg='#f0f0f0',
                               fg='#7f8c8d')
        footer_label.pack(pady=5)
    
    def generate_new_values(self):
        """Генерирует новые случайные значения"""
        # Пакеты в обработке: 5-15
        self.data["Пакеты в обработке"] = random.randint(5, 15)
        
        # Загруженные образцы: 5-20
        self.data["Загруженные образцы"] = random.randint(5, 20)
        
        # Тесты завершены: увеличиваем на 1-5
        self.data["Тесты завершены"] += random.randint(1, 5)
    
    def update_display(self):
        """Обновляет отображение всех значений"""
        for title, label in self.value_labels.items():
            label.config(text=str(self.data[title]))
        
        # Обновляем время
        current_time = time.strftime("%H:%M:%S")
        self.status_label.config(text=f"Статус: {'Активно' if self.is_running else 'Остановлено'} | Последнее обновление: {current_time}")
    
    def auto_update_loop(self):
        """Цикл автоматического обновления"""
        while True:
            time.sleep(2)  # Ждем 2 секунды
            if self.is_running:
                # Генерируем новые значения
                self.generate_new_values()
                
                # Обновляем интерфейс в основном потоке
                self.root.after(0, self.update_display)
                
                # Обновляем информационную панель
                next_time = time.strftime("%H:%M:%S", time.localtime(time.time() + 2))
                self.info_label.config(
                    text=f"✅ Данные обновлены. Следующее обновление в {next_time}")
    
    def start_auto_update(self):
        """Запускает поток автообновления"""
        self.auto_update_thread = threading.Thread(target=self.auto_update_loop, daemon=True)
        self.auto_update_thread.start()
    
    def toggle_auto_update(self):
        """Включить/выключить автообновление"""
        self.is_running = not self.is_running
        
        if self.is_running:
            self.update_btn.config(text="⏸ Остановить автообновление", bg="#4CAF50")
            self.info_label.config(text="🔄 Автообновление возобновлено")
        else:
            self.update_btn.config(text="▶ Возобновить автообновление", bg="#f44336")
            self.info_label.config(text="⏸ Автообновление остановлено")
    
    def manual_update(self):
        """Ручное обновление данных"""
        self.generate_new_values()
        self.update_display()
        self.info_label.config(text="🔄 Данные обновлены вручную")
    
    def on_closing(self):
        """Обработчик закрытия окна"""
        self.is_running = False
        self.root.destroy()

# Создаем и запускаем приложение
if __name__ == "__main__":
    root = tk.Tk()
    app = AutoUpdateApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()