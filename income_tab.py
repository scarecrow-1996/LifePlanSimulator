import global_var as g
from tkinter import ttk, messagebox, filedialog

def create():
    g.income_tab = ttk.Frame(g.notebook)
    g.notebook.add(g.income_tab, text="給与")
    
    income_frame = ttk.LabelFrame(g.income_tab, text="給与情報を入力してください", padding=10)
    income_frame.pack(padx=10, pady=10, fill="both", expand=True)
    
    # Comming Soon
    ttk.Label(income_frame, text="Comming Soon..").pack(anchor="w", pady=(0,5))
    pass
