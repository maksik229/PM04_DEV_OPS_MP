import tkinter as tk
import random
import math

class SimpleFileGenerator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Генератор файлов")
        self.window.geometry("500x400")
        
    
        tk.Label(self.window, text="Задание 1 - работа Сбитневой Дарьи", 
                font=("Arial", 12, "bold")).pack(pady=10)
        

        tk.Label(self.window, text="Создает файл с текстом, числами и функцией sin(x)").pack()



        tk.Label(self.window, text="Текст:").pack()
        self.text_box = tk.Text(self.window, height=3, width=50)
        self.text_box.pack()
        self.text_box.insert("1.0", "Пример текста для записи в файл.")


        tk.Label(self.window, text="Сколько чисел:").pack()
        self.num_entry = tk.Entry(self.window, width=10)
        self.num_entry.pack()
        self.num_entry.insert(0, "10")



        tk.Label(self.window, text="Функция (шаг 0.5, от 0 до 10):").pack()



        self.status = tk.Label(self.window, text="Готов")
        self.status.pack()
    
    def make_file(self):
        try:


            text = self.text_box.get("1.0", tk.END).strip()
            num_count = int(self.num_entry.get())



            filename = "result.txt"

            with open(filename, 'w', encoding='utf-8') as f:

                f.write("Файл создан Сбитневой Дарьей\n")
                f.write("=" * 30 + "\n\n")


                f.write("ТЕКСТ:\n")
                f.write(text + "\n\n")


                f.write("СЛУЧАЙНЫЕ ЧИСЛА:\n")
                for i in range(num_count):
                    num = random.randint(1, 100)
                    f.write(f"{i+1}. {num}\n")
                f.write("\n")



                f.write("ФУНКЦИЯ sin(x):\n")
                for x in [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]:
                    y = math.sin(x)
                    f.write(f"sin({x:.1f}) = {y:.3f}\n")




                self.status.config(text=f"Файл '{filename}' создан!", fg="green")
            
        except:
            self.status.config(text="Ошибка! Проверьте ввод", fg="red")
    
    def run(self):
        self.window.mainloop()



if __name__ == "__main__":
    app = SimpleFileGenerator()
    app.run()
                




        
        
        