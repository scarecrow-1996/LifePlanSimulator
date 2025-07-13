import global_var as g
from tkinter import ttk, messagebox, filedialog

def create():
    g.special_tab = ttk.Frame(g.notebook)
    g.notebook.add(g.special_tab, text="special")
    
    special_frame = ttk.LabelFrame(g.special_tab, text="special情報を入力してください", padding=10)
    special_frame.pack(padx=10, pady=10, fill="both", expand=True)
    
    # Comming Soon
    ttk.Label(special_frame, text="Comming Soon..").pack(anchor="w", pady=(0,5))
    pass
