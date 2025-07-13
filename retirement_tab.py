import global_var as g
from tkinter import ttk, messagebox, filedialog

def create():
    g.retirement_tab = ttk.Frame(g.notebook)
    g.notebook.add(g.retirement_tab, text="retirement")
    
    retirement_frame = ttk.LabelFrame(g.retirement_tab, text="retirement情報を入力してください", padding=10)
    retirement_frame.pack(padx=10, pady=10, fill="both", expand=True)
    
    # Comming Soon
    ttk.Label(retirement_frame, text="Comming Soon..").pack(anchor="w", pady=(0,5))
    pass
