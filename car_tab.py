import global_var as g
from tkinter import ttk, messagebox, filedialog

def create():
    g.car_tab = ttk.Frame(g.notebook)
    g.notebook.add(g.car_tab, text="car")
    
    car_frame = ttk.LabelFrame(g.car_tab, text="car情報を入力してください", padding=10)
    car_frame.pack(padx=10, pady=10, fill="both", expand=True)
    
    # Comming Soon
    ttk.Label(car_frame, text="Comming Soon..").pack(anchor="w", pady=(0,5))
    pass
