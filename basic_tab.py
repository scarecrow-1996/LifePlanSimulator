
import global_var as g
import utility
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from datetime import datetime


def calculate_age(target_year, target_month):
    try:
        birth_year = int(g.birth_year_var.get())
        birth_month = int(g.birth_month_var.get())
        
        if birth_month < 1 or birth_month > 12:
            return None, "月は1-12で入力"
        
        age_years = target_year - birth_year
        age_months = target_month - birth_month
        
        if age_months < 0:
            age_years -= 1
            age_months += 12
        
        if age_years < 0:
            return None, "生前の日付"
            
        return (age_years, age_months), None
    except ValueError:
        return None, "有効な数値を入力"

def update_age_displays():
    # 現在年齢
    current_date = datetime.now()
    current_age, error = calculate_age(current_date.year, current_date.month)
    if error:
        g.current_age_label.config(text=f"現在年齢: {error}", foreground="red")
    else:
        years, months = current_age
        g.current_age_label.config(
            text=f"現在年齢: {years}歳{months}ヶ月",
            foreground="blue"
        )
    
    # 開始時年齢
    try:
        start_year = int(g.start_year_var.get())
        start_month = int(g.start_month_var.get())
        start_age, error = calculate_age(start_year, start_month)
        if error:
            g.start_age_label.config(text=f"開始時年齢: {error}", foreground="red")
        else:
            years, months = start_age
            g.start_age_label.config(
                text=f"開始時年齢: {years}歳{months}ヶ月",
                foreground="green"
            )
    except ValueError:
        g.start_age_label.config(text="開始時年齢: 無効な値", foreground="red")
    
    # 終了時年齢
    try:
        end_year = int(g.end_year_var.get())
        end_month = int(g.end_month_var.get())
        end_age, error = calculate_age(end_year, end_month)
        if error:
            g.end_age_label.config(text=f"終了時年齢: {error}", foreground="red")
        else:
            years, months = end_age
            g.end_age_label.config(
                text=f"終了時年齢: {years}歳{months}ヶ月",
                foreground="green"
            )
    except ValueError:
        g.end_age_label.config(text="終了時年齢: 無効な値", foreground="red")

def create():
    g.birth_tab = ttk.Frame(g.notebook)
    g.notebook.add(g.birth_tab, text="基本情報")
    
    base_frame = ttk.LabelFrame(g.birth_tab, text="基本情報を入力してください", padding=10)
    base_frame.pack(padx=10, pady=10, fill="both", expand=True)

    # 月のリストを準備
    months = [str(i) for i in range(1, 13)]  # ['1', '2', ..., '12']

    # 生年月入力
    ttk.Label(base_frame, text="生年月").pack(anchor="w", pady=(0,5))
    birth_date_frame = ttk.Frame(base_frame)
    birth_date_frame.pack(fill="x", pady=5)

    g.birth_year_var = tk.StringVar(value=str(g.params["birth"]["year"]))
    ttk.Combobox(
        birth_date_frame,
        textvariable=g.birth_year_var,
        values = [str(year_i) for year_i in range(g.current_year-120, g.current_year+120)],  # 選択可能な値のリスト
        width=5,        # 幅
        justify=tk.RIGHT,
        state='readonly'  # ユーザーが直接編集できないように
    ).grid(row=0, column=1, padx=5, sticky="w")
    ttk.Label(birth_date_frame, text="年").grid(row=0, column=2, sticky="w")


    g.birth_month_var = tk.StringVar(value=str(g.params["birth"]["month"]))
    month_combobox = ttk.Combobox(
        birth_date_frame,
        textvariable=g.birth_month_var,
        values=months,      # 選択可能な値のリスト
        width=3,            # 幅
        justify=tk.RIGHT,
        state='readonly'    # ユーザーが直接編集できないように
    )
    month_combobox.grid(row=0, column=3, sticky="w")
    ttk.Label(birth_date_frame, text="月").grid(row=0, column=4, sticky="w")
    # 値変更時のイベントハンドリング
    # month_combobox.bind('<<ComboboxSelected>>', lambda e: update_age_displays())

    g.current_age_label = ttk.Label(
        birth_date_frame, 
        text="現在年齢: -",
        foreground="blue"
    )
    g.current_age_label.grid(row=0, column=5, padx=10, sticky="e")


    # シミュレーション期間
    ttk.Label(base_frame, text="シミュレーション期間").pack(anchor="w", pady=(10,5))
    
    # 開始時期
    start_frame = ttk.Frame(base_frame)
    start_frame.pack(fill="x", pady=5)
    ttk.Label(start_frame, text="開始:").grid(row=0, column=0, sticky="w")
    
    g.start_year_var = tk.StringVar(value=str(g.params["start"]["year"]))
    ttk.Combobox(
        start_frame,
        textvariable=g.start_year_var,
        values = [str(year_i) for year_i in range(g.current_year-120, g.current_year+120)],  # 選択可能な値のリスト
        width=5,        # 幅
        justify=tk.RIGHT,
        state='readonly'  # ユーザーが直接編集できないように
    ).grid(row=0, column=1, padx=5, sticky="w")
    ttk.Label(start_frame, text="年").grid(row=0, column=2, sticky="w")
    
    g.start_month_var = tk.StringVar(value=str(g.params["start"]["month"]))
    ttk.Combobox(
        start_frame,
        textvariable=g.start_month_var,
        values=months,  # 選択可能な値のリスト
        width=3,        # 幅
        justify=tk.RIGHT,
        state='readonly'  # ユーザーが直接編集できないように
    ).grid(row=0, column=3, padx=5, sticky="w")
    ttk.Label(start_frame, text="月").grid(row=0, column=4, sticky="w")
    
    g.start_age_label = ttk.Label(
        start_frame, 
        text="開始時年齢: -",
        foreground="green"
    )
    g.start_age_label.grid(row=0, column=5, padx=10, sticky="e")
    
    # 終了時期
    end_frame = ttk.Frame(base_frame)
    end_frame.pack(fill="x", pady=5)
    ttk.Label(end_frame, text="終了:").grid(row=0, column=0, sticky="w")
    
    g.end_year_var = tk.StringVar(value=str(g.params["end"]["year"]))
    ttk.Combobox(
        end_frame,
        textvariable=g.end_year_var,
        values = [str(year_i) for year_i in range(g.current_year-120, g.current_year+120)],  # 選択可能な値のリスト
        width=5,        # 幅
        justify=tk.RIGHT,
        state='readonly'  # ユーザーが直接編集できないように
    ).grid(row=0, column=1, padx=5, sticky="w")
    ttk.Label(end_frame, text="年").grid(row=0, column=2, sticky="w")
    
    # 月
    g.end_month_var = tk.StringVar(value=str(g.params["end"]["month"]))
    # ドロップダウンリスト（Combobox）の作成
    ttk.Combobox(
        end_frame,
        textvariable=g.end_month_var,
        values=months,  # 選択可能な値のリスト
        width=3,        # 幅
        justify=tk.RIGHT,
        state='readonly'  # ユーザーが直接編集できないように
    ).grid(row=0, column=3, padx=5, sticky="w")
    ttk.Label(end_frame, text="月").grid(row=0, column=4, sticky="w")
    
    g.end_age_label = ttk.Label(
        end_frame, 
        text="終了時年齢: -",
        foreground="green"
    )
    g.end_age_label.grid(row=0, column=5, padx=10, sticky="e")

    # 変数監視
    # パラメーターの更新
    g.birth_year_var.trace_add("write", lambda *args: update_age_displays())
    g.birth_month_var.trace_add("write", lambda *args: update_age_displays())
    g.start_year_var.trace_add("write", lambda *args: update_age_displays())
    g.start_month_var.trace_add("write", lambda *args: update_age_displays())
    g.end_year_var.trace_add("write", lambda *args: update_age_displays())
    g.end_month_var.trace_add("write", lambda *args: update_age_displays())

    update_age_displays()
    
    # 貯蓄額（現金）
    ttk.Label(base_frame, text="貯金額").pack(anchor="w", pady=(10,5))
    cash_frame = ttk.Frame(base_frame)
    cash_frame.pack(fill="x", pady=5)
    ttk.Label(cash_frame, text="現金:").grid(row=0, column=0, sticky="w")
    g.cash_amount_var = tk.StringVar(value=str(g.params["cash"]["amount"]))
    ttk.Entry(
        cash_frame, 
        textvariable=g.cash_amount_var,
        width=10,
        justify=tk.RIGHT
    ).grid(row=0, column=1, padx=5, sticky="w")
    ttk.Label(cash_frame, text="万円").grid(row=0, column=2, sticky="w")
    
    ttk.Label(cash_frame, text="　　預貯金金利:").grid(row=0, column=4, sticky="e")
    g.cash_rate_var = tk.StringVar(value=str(g.params["cash"]["rate"]))
    ttk.Entry(
        cash_frame, 
        textvariable=g.cash_rate_var,
        width=6,
        justify=tk.RIGHT
    ).grid(row=0, column=5, padx=5, sticky="w")
    ttk.Label(cash_frame, text="%").grid(row=0, column=6, sticky="w")
    
    
    # オプション設定欄
    options_frame = ttk.LabelFrame(g.birth_tab, text="オプション設定", padding=10)
    options_frame.pack(padx=10, pady=10, fill="both", expand=True)

    # 設定系
    g.init_option = tk.BooleanVar(value=g.params["option"]["init"])
    # 収入系
    g.income_option = tk.BooleanVar(value=g.params["option"]["income"])
    g.stock_option = tk.BooleanVar(value=g.params["option"]["stock"])
    g.NISA_option = tk.BooleanVar(value=g.params["option"]["NISA"])
    g.iDeCo_option = tk.BooleanVar(value=g.params["option"]["iDeCo"])
    g.DC_option = tk.BooleanVar(value=g.params["option"]["DC"])
    g.retirement_option = tk.BooleanVar(value=g.params["option"]["retirement"])
    # 支出系
    g.housing_option = tk.BooleanVar(value=g.params["option"]["housing"])
    g.daily_option = tk.BooleanVar(value=g.params["option"]["daily"])
    g.special_option = tk.BooleanVar(value=g.params["option"]["special"])
    g.car_option = tk.BooleanVar(value=g.params["option"]["car"])
    g.education_option = tk.BooleanVar(value=g.params["option"]["education"])
    g.nursing_care_option = tk.BooleanVar(value=g.params["option"]["nursing_care"])

    ttk.Label(options_frame, text="設定系:").grid(row=0, column=0, sticky="w")
    ttk.Checkbutton(
        options_frame, 
        text="初期化", 
        variable=g.init_option,
    ).grid(row=0, column=1, sticky="w", pady=2, padx=5)

    ttk.Label(options_frame, text="収入系:").grid(row=1, column=0, sticky="w")
    ttk.Checkbutton(
        options_frame, 
        text="給与", 
        variable=g.income_option,
        command=utility.toggle_tabs
    ).grid(row=1, column=1, sticky="w", pady=2, padx=5)

    ttk.Checkbutton(
        options_frame, 
        text="投資", 
        variable=g.stock_option,
        command=utility.toggle_tabs
    ).grid(row=1, column=2, sticky="w", pady=2, padx=5)
    
    ttk.Checkbutton(
        options_frame, 
        text="NISA", 
        variable=g.NISA_option,
        command=utility.toggle_tabs
    ).grid(row=1, column=3, sticky="w", pady=2, padx=5)

    ttk.Checkbutton(
        options_frame, 
        text="iDeCo", 
        variable=g.iDeCo_option,
        command=utility.toggle_tabs
    ).grid(row=1, column=4, sticky="w", pady=2, padx=5)
    
    ttk.Checkbutton(
        options_frame, 
        text="DC", 
        variable=g.DC_option,
        command=utility.toggle_tabs
    ).grid(row=1, column=5, sticky="w", pady=2, padx=5)
    
    ttk.Checkbutton(
        options_frame, 
        text="退職金", 
        variable=g.retirement_option,
        command=utility.toggle_tabs
    ).grid(row=1, column=6, sticky="w", pady=2, padx=5)

    ttk.Label(options_frame, text="支出系:").grid(row=2, column=0, sticky="w")
    ttk.Checkbutton(
        options_frame, 
        text="住居", 
        variable=g.housing_option,
        command=utility.toggle_tabs
    ).grid(row=2, column=1, sticky="w", pady=2, padx=5)
    
    ttk.Checkbutton(
        options_frame, 
        text="日常", 
        variable=g.daily_option,
        command=utility.toggle_tabs
    ).grid(row=2, column=2, sticky="w", pady=2, padx=5)

    ttk.Checkbutton(
        options_frame, 
        text="特別", 
        variable=g.special_option,
        command=utility.toggle_tabs
    ).grid(row=2, column=3, sticky="w", pady=2, padx=5)

    ttk.Checkbutton(
        options_frame, 
        text="車", 
        variable=g.car_option,
        command=utility.toggle_tabs
    ).grid(row=2, column=4, sticky="w", pady=2, padx=5)

    ttk.Checkbutton(
        options_frame, 
        text="教育", 
        variable=g.education_option,
        command=utility.toggle_tabs
    ).grid(row=2, column=5, sticky="w", pady=2, padx=5)

    ttk.Checkbutton(
        options_frame, 
        text="介護", 
        variable=g.nursing_care_option,
        command=utility.toggle_tabs
    ).grid(row=2, column=6, sticky="w", pady=2, padx=5)