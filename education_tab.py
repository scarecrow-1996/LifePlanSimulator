import global_var as g
from tkinter import ttk, messagebox, filedialog

def create():
    g.education_tab = ttk.Frame(g.notebook)
    g.notebook.add(g.education_tab, text="教育")
    
    education_frame = ttk.LabelFrame(g.education_tab, text="教育費情報を入力してください", padding=10)
    education_frame.pack(padx=10, pady=10, fill="both", expand=True)
    
    # Comming Soon
    ttk.Label(education_frame, text="Comming Soon..").pack(anchor="w", pady=(0,5))
    pass
