import global_var as g
from tkinter import ttk, messagebox, filedialog

def create():
    g.nursing_care_tab = ttk.Frame(g.notebook)
    g.notebook.add(g.nursing_care_tab, text="住居")
    
    nurse_care_frame = ttk.LabelFrame(g.nursing_care_tab, text="住まい情報を入力してください", padding=10)
    nurse_care_frame.pack(padx=10, pady=10, fill="both", expand=True)
    
    # Comming Soon
    ttk.Label(nurse_care_frame, text="Comming Soon..").pack(anchor="w", pady=(0,5))
    pass
