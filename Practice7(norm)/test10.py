import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt

class SimpleDataVisualizer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Визуализатор данных")
        self.root.geometry("1000x700")
        
        self.df = None
        
        self.create_widgets()
    
    def create_widgets(self):
    
        control_frame = tk.Frame(self.root, width=300, bg='lightgray')
        control_frame.pack(side=tk.LEFT, fill=tk.Y)




        tk.Label(control_frame, text="Загрузить данные", bg='lightgray').pack(pady=10)
        tk.Button(control_frame, text="CSV", command=self.load_csv).pack(pady=5, fill='x', padx=10)
        tk.Button(control_frame, text="Excel", command=self.load_excel).pack(pady=5, fill='x', padx=10)


        self.info_text = tk.Text(control_frame, height=10, width=35)
        self.info_text.pack(pady=10, padx=10)



        tk.Label(control_frame, text="Тип графика", bg='lightgray').pack(pady=10)
        
        self.graph_type = tk.StringVar(value="line")
        
        tk.Radiobutton(control_frame, text="Линейный", variable=self.graph_type, 
                      value="line").pack(anchor='w', padx=20)
        tk.Radiobutton(control_frame, text="Столбчатый", variable=self.graph_type, 
                      value="bar").pack(anchor='w', padx=20)
        tk.Radiobutton(control_frame, text="Круговая", variable=self.graph_type, 
                      value="pie").pack(anchor='w', padx=20)
        



        tk.Label(control_frame, text="Столбцы", bg='lightgray').pack(pady=10)
        
        tk.Label(control_frame, text="X:").pack(anchor='w', padx=20)
        self.x_var = tk.StringVar()
        self.x_combo = tk.Listbox(control_frame, height=4, exportselection=False)
        self.x_combo.pack(fill='x', padx=20)
        
        tk.Label(control_frame, text="Y:").pack(anchor='w', padx=20, pady=(10,0))
        self.y_var = tk.StringVar()
        self.y_combo = tk.Listbox(control_frame, height=4, exportselection=False)
        self.y_combo.pack(fill='x', padx=20)


        tk.Button(control_frame, text="Построить график", 
                 command=self.plot_graph).pack(pady=20, padx=10, fill='x')
        



        self.plot_frame = tk.Frame(self.root)
        self.plot_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
    
    def load_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            try:
                self.df = pd.read_csv(file_path)
                self.update_data_info()
            except Exception as e:
                print(f"Ошибка: {e}")
    
    def load_excel(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
        if file_path:
            try:
                self.df = pd.read_excel(file_path)
                self.update_data_info()
            except Exception as e:
                print(f"Ошибка: {e}")
    
    def update_data_info(self):
        if self.df is not None:

            self.x_combo.delete(0, tk.END)
            self.y_combo.delete(0, tk.END)




            for col in self.df.columns:
                self.x_combo.insert(tk.END, col)
                self.y_combo.insert(tk.END, col)



            info = f"Файл загружен\n"
            info += f"Строк: {self.df.shape[0]}\n"
            info += f"Столбцов: {self.df.shape[1]}\n\n"
            info += "Столбцы:\n"
            for col in self.df.columns:
                info += f"- {col}\n"
            
            self.info_text.delete(1.0, tk.END)
            self.info_text.insert(1.0, info)
    
    def plot_graph(self):
        if self.df is None:
            print("Сначала загрузите данные")
            return
        

        x_selection = self.x_combo.curselection()
        y_selection = self.y_combo.curselection()
        
        if not x_selection or not y_selection:
            print("Выберите столбцы для X и Y")
            return
        
        x_col = self.df.columns[x_selection[0]]
        y_col = self.df.columns[y_selection[0]]



        plt.figure(figsize=(10, 6))
        
        graph_type = self.graph_type.get()
        
        if graph_type == "line":
            plt.plot(self.df[x_col], self.df[y_col], marker='o')
            plt.title(f"Линейный график: {y_col} vs {x_col}")
            
        elif graph_type == "bar":
            plt.bar(self.df[x_col].astype(str), self.df[y_col])
            plt.title(f"Столбчатый график: {y_col} по {x_col}")
            plt.xticks(rotation=45)
            
        elif graph_type == "pie":
            if len(self.df) > 10:
                print("Для круговой диаграммы лучше не более 10 значений")
                return
            plt.pie(self.df[y_col], labels=self.df[x_col].astype(str), autopct='%1.1f%%')
            plt.title(f"Круговая диаграмма: {y_col}")
        
        plt.xlabel(x_col)
        if graph_type != "pie":
            plt.ylabel(y_col)
        
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = SimpleDataVisualizer()
    app.run()
        
        
        
        