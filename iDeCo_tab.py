import global_var as g
from tkinter import ttk, messagebox, filedialog

def create():
    g.iDeCo_tab = ttk.Frame(g.notebook)
    g.notebook.add(g.iDeCo_tab, text="iDeCo")
    
    iDeCo_frame = ttk.LabelFrame(g.iDeCo_tab, text="iDeCo情報を入力してください", padding=10)
    iDeCo_frame.pack(padx=10, pady=10, fill="both", expand=True)
    
    # Comming Soon
    ttk.Label(iDeCo_frame, text="Comming Soon..").pack(anchor="w", pady=(0,5))
    pass
