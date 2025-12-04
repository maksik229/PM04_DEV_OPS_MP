import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import random

def update_time():
    """Обновляет время"""
    now = datetime.now()
    time_label.config(text=now.strftime("%H:%M:%S"))
    date_label.config(text=now.strftime("%d.%m.%Y, %A"))
    root.after(1000, update_time)

def update_calendar():
    """Обновляет календарь"""
    now = datetime.now()
    month = now.month
    year = now.year
    day = now.day
    
    calendar_text.delete(1.0, tk.END)
    
    # Заголовок
    months = ["Январь","Февраль","Март","Апрель","Май","Июнь",
              "Июль","Август","Сентябрь","Октябрь","Ноябрь","Декабрь"]
    calendar_text.insert(tk.END, f"{months[month-1]} {year}\n")
    calendar_text.insert(tk.END, "-"*20 + "\n")
    
    # Первый день месяца
    first_day = datetime(year, month, 1)
    start_weekday = first_day.weekday()
    
    # Дни недели
    calendar_text.insert(tk.END, "Пн Вт Ср Чт Пт Сб Вс\n")
    
    # Пустые дни
    days_text = "   " * start_weekday
    
    # Дни месяца
    days_in_month = 31 if month in [1,3,5,7,8,10,12] else 30
    if month == 2:
        days_in_month = 29 if year % 4 == 0 else 28
    
    for d in range(1, days_in_month + 1):
        if d == day:
            days_text += f"[{d:2}]"
        else:
            days_text += f" {d:2} "
        
        if (start_weekday + d) % 7 == 0:
            days_text += "\n"
    
    calendar_text.insert(tk.END, days_text)

def check_password():
    """Проверяет пароль"""
    login = login_entry.get()
    password = password_entry.get()
    
    if login == "admin" and password == "12345":
        messagebox.showinfo("Успех", "Доступ разрешен!")
        status_label.config(text="✓ Вход выполнен", fg="green")
    else:
        messagebox.showerror("Ошибка", "Неверный логин или пароль!")
        status_label.config(text="✗ Ошибка входа", fg="red")

def get_weather():
    """Показывает погоду"""
    city = city_entry.get()
    if not city:
        city = "Москва"
    
    # Случайные погодные данные
    temp = random.randint(-10, 30)
    conditions = ["☀️ Солнечно", "⛅ Облачно", "☁️ Пасмурно", 
                  "🌧️ Дождь", "⛈️ Гроза", "❄️ Снег"]
    condition = random.choice(conditions)
    
    weather_info = f"""
Город: {city}
Температура: {temp}°C
Состояние: {condition}
Ветер: {random.randint(1, 10)} м/с
Влажность: {random.randint(30, 90)}%
"""
    
    weather_text.delete(1.0, tk.END)
    weather_text.insert(tk.END, weather_info)

# Создаем окно
root = tk.Tk()
root.title("Задание 6: Работа Сбитневой Дарьи")
root.geometry("450x550")

# Заголовок
tk.Label(root, text="Задание 6: Работа Сбитневой Дарьи", 
         font=("Arial", 14, "bold")).pack(pady=10)

# ===== КАЛЕНДАРЬ =====
tk.Label(root, text="Календарь", font=("Arial", 12, "bold")).pack()

# Время и дата
time_label = tk.Label(root, font=("Arial", 16, "bold"), fg="blue")
time_label.pack()

date_label = tk.Label(root, font=("Arial", 12))
date_label.pack(pady=5)

# Календарь
calendar_text = tk.Text(root, height=8, width=25, font=("Courier", 10))
calendar_text.pack(pady=10)

tk.Button(root, text="Обновить календарь", 
         command=update_calendar, bg="lightblue").pack()

# Разделитель
tk.Label(root, text="─"*50).pack(pady=10)

# ===== ПАРОЛЬ =====
tk.Label(root, text="Вход в систему", font=("Arial", 12, "bold")).pack()

# Логин
tk.Label(root, text="Логин:").pack()
login_entry = tk.Entry(root, width=20)
login_entry.pack()
login_entry.insert(0, "admin")

# Пароль
tk.Label(root, text="Пароль:").pack()
password_entry = tk.Entry(root, width=20, show="*")
password_entry.pack()

# Кнопка входа
tk.Button(root, text="Войти", command=check_password, 
         bg="lightgreen", width=10).pack(pady=5)

status_label = tk.Label(root, text="")
status_label.pack()

# Разделитель
tk.Label(root, text="─"*50).pack(pady=10)

# ===== ПОГОДА =====
tk.Label(root, text="Погода", font=("Arial", 12, "bold")).pack()

# Город
tk.Label(root, text="Город:").pack()
city_entry = tk.Entry(root, width=20)
city_entry.pack()
city_entry.insert(0, "Москва")

# Кнопка погоды
tk.Button(root, text="Узнать погоду", command=get_weather, 
         bg="lightblue", width=12).pack(pady=5)

# Информация о погоде
weather_text = tk.Text(root, height=6, width=30)
weather_text.pack(pady=10)

# Автоматическое обновление
update_time()
update_calendar()
get_weather()

# Запуск
root.mainloop()