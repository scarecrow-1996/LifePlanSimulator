import global_var as g
from tkinter import ttk, messagebox, filedialog

def create():
    g.stock_tab = ttk.Frame(g.notebook)
    g.notebook.add(g.stock_tab, text="stock")
    
    stock_frame = ttk.LabelFrame(g.stock_tab, text="stock情報を入力してください", padding=10)
    stock_frame.pack(padx=10, pady=10, fill="both", expand=True)
    
    # Comming Soon
    ttk.Label(stock_frame, text="Comming Soon..").pack(anchor="w", pady=(0,5))
    pass
