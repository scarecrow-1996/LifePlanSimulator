import global_var as g
from tkinter import ttk, messagebox, filedialog

def create():
    g.daily_tab = ttk.Frame(g.notebook)
    g.notebook.add(g.daily_tab, text="日常")
    
    daily_frame = ttk.LabelFrame(g.daily_tab, text="日常生活費情報を入力してください", padding=10)
    daily_frame.pack(padx=10, pady=10, fill="both", expand=True)
    
    # Comming Soon
    ttk.Label(daily_frame, text="Comming Soon..").pack(anchor="w", pady=(0,5))
    pass
