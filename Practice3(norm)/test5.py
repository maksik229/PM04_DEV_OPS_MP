import tkinter as tk
import random
from datetime import datetime

def update_all():
    """Обновляет все данные автоматически"""
    
    new_tests = random.randint(1, 30)
    tests_value.config(text=str(new_tests))

    reagents_emojis = ["💬", "💧", "⚗️", "🧪", "🔬"]
    reagents_emoji.config(text=random.choice(reagents_emojis))

    supplies_emojis = ["💭", "🗑️", "📦", "🔄", "♻️"]
    supplies_emoji.config(text=random.choice(supplies_emojis))


    time_label.config(text=f"Обновлено: {datetime.now().strftime('%H:%M:%S')}")


    root.after(3000, update_all)


root = tk.Tk()
root.title("BSO Dashboard - Сбитнева Дарья")
root.geometry("400x300")



tk.Label(root, 
        text="Задание 5: Работа Сбитневой Дарьи",
        font=("Arial", 14, "bold")).pack(pady=10)


tk.Label(root, text="BSO", font=("Arial", 18, "bold")).pack(pady=5)


main_frame = tk.Frame(root)
main_frame.pack(pady=20, padx=20)


test_frame = tk.Frame(main_frame)
test_frame.pack(fill='x', pady=10)

tk.Label(test_frame, text="Tests in Process", 
         font=("Arial", 11, "bold"), width=20, anchor='w').pack(side='left')
tests_value = tk.Label(test_frame, text="20", 
                      font=("Arial", 16, "bold"), fg='blue', width=10)
tests_value.pack(side='left')
tk.Label(test_frame, text="QC", font=("Arial", 10), fg='gray').pack(side='right')



reagent_frame = tk.Frame(main_frame)
reagent_frame.pack(fill='x', pady=10)

tk.Label(reagent_frame, text="Reagents", 
         font=("Arial", 11, "bold"), width=20, anchor='w').pack(side='left')
reagents_emoji = tk.Label(reagent_frame, text="💬", 
                         font=("Arial", 20), width=10)
reagents_emoji.pack(side='left')
tk.Label(reagent_frame, text="Calibration", 
         font=("Arial", 10), fg='gray').pack(side='right')


supply_frame = tk.Frame(main_frame)
supply_frame.pack(fill='x', pady=10)

tk.Label(supply_frame, text="Supplies & Waste", 
         font=("Arial", 11, "bold"), width=20, anchor='w').pack(side='left')
supplies_emoji = tk.Label(supply_frame, text="💭", 
                         font=("Arial", 20), width=10)
supplies_emoji.pack(side='left')
tk.Label(supply_frame, text="Process Path", 
         font=("Arial", 10), fg='gray').pack(side='right')



time_label = tk.Label(root, text="Обновлено: --:--:--", 
                     font=("Arial", 9), fg='gray')
time_label.pack(pady=10)


tk.Button(root, text="Обновить сейчас", 
         command=update_all, bg='lightblue').pack(pady=5)


root.after(1000, update_all)  # Первое обновление через 1 секунду

root.mainloop()


    
   