import global_var as g
from utility import export_json, import_json, toggle_tabs
import basic_tab, income_tab, stock_tab, NISA_tab, iDeCo_tab, DC_tab, retirement_tab
import housing_tab, daily_tab, special_tab, car_tab, education_tab, nursing_care_tab
import simulator
import tkinter as tk
from tkinter import ttk, messagebox, filedialog

def HP(window):

    """  タイトル  """
    window.title("ライフプランシミュレーター")
    window.geometry("600x600")


    """  タブ  """
    # 基本情報
    g.notebook = ttk.Notebook(window)
    g.notebook.pack(padx=10, pady=10, fill="both", expand=True)
    basic_tab.create()
    # 給与タブ
    income_tab.create()
    # 投資タブ
    stock_tab.create()
    # NISAタブ
    NISA_tab.create()
    # iDeCoタブ
    iDeCo_tab.create()
    # 企業年金タブ
    DC_tab.create()
    # 退職金タブ
    retirement_tab.create()
    # 住居タブ
    housing_tab.create()
    # 日常タブ
    daily_tab.create()
    # 特別支出タブ
    special_tab.create()
    # 車タブ
    car_tab.create()
    # 教育タブ
    education_tab.create()
    # 介護タブ
    nursing_care_tab.create()
    
    # タブの表示状態の更新
    toggle_tabs()


    """  ボタンフレーム  """
    button_frame = ttk.Frame(window)
    button_frame.pack(pady=10)

    # ボタンスタイル設定
    style = ttk.Style()
    style.theme_use('clam')  # 'clam', 'alt', 'default', 'classic' などから選択
    style.configure('TButton', padding=6)
    style.map('Import.TButton', 
                    foreground=[('active', 'white'), ('!active', 'white')],
                    background=[('active', '#1976D2'), ('!active', '#2196F3')])
    style.map('Export.TButton',
                    foreground=[('active', 'white'), ('!active', 'white')],
                    background=[('active', '#388E3C'), ('!active', '#4CAF50')])

    import_button = ttk.Button(
        button_frame, 
        text="Import", 
        command=import_json,
        style='Import.TButton'
    )
    import_button.pack(side="left", padx=5)
    
    export_button = ttk.Button(
        button_frame, 
        text="Export", 
        command=export_json,
        style='Export.TButton'
    )
    export_button.pack(side="left", padx=5)

    execute_button = ttk.Button(
        button_frame, 
        text="シミュレーション開始", 
        command=simulator.run
    )
    execute_button.pack(side="left", padx=5)


    """  フッター  """
    tk.Label(
        window,
        text="Copyright © 2025 Life Plan Simulator",
        bg="#f0f0f0",
        fg="#999999"
    ).pack(side="bottom", pady=10)

