import global_var as g
from tkinter import ttk, messagebox, filedialog

def create():
    g.NISA_tab = ttk.Frame(g.notebook)
    g.notebook.add(g.NISA_tab, text="NISA")
    
    NISA_frame = ttk.LabelFrame(g.NISA_tab, text="NISA情報を入力してください", padding=10)
    NISA_frame.pack(padx=10, pady=10, fill="both", expand=True)
    
    # Comming Soon
    ttk.Label(NISA_frame, text="Comming Soon..").pack(anchor="w", pady=(0,5))
    pass
