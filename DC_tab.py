import global_var as g
from tkinter import ttk, messagebox, filedialog

def create():
    g.DC_tab = ttk.Frame(g.notebook)
    g.notebook.add(g.DC_tab, text="DC")
    
    DC_frame = ttk.LabelFrame(g.DC_tab, text="企業年金情報を入力してください", padding=10)
    DC_frame.pack(padx=10, pady=10, fill="both", expand=True)
    
    # Comming Soon
    ttk.Label(DC_frame, text="Comming Soon..").pack(anchor="w", pady=(0,5))
    pass
