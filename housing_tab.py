import global_var as g
from tkinter import ttk, messagebox, filedialog

def create():
    g.housing_tab = ttk.Frame(g.notebook)
    g.notebook.add(g.housing_tab, text="住居")
    
    housing_frame = ttk.LabelFrame(g.housing_tab, text="住まい情報を入力してください", padding=10)
    housing_frame.pack(padx=10, pady=10, fill="both", expand=True)
    
    # Comming Soon
    ttk.Label(housing_frame, text="Comming Soon..").pack(anchor="w", pady=(0,5))
    pass
