import global_var as g
import GUI
import tkinter as tk
from datetime import datetime

def init_global_var():
    g.csv_out_data = "out/data.csv"     # 生データ名
    g.csv_out_graph = "out/graph.csv"   # グラフ生成用データ名
    g.opng_out_graph = "out/graph.png"  # シミュレーション結果png
    
    g.current_year = datetime.now().year
    g.current_month = datetime.now().month

    g.params = {
        "birth":{
            "year":g.current_year-18,
            "month":1
        },
        "start":{
            "year":g.current_year,
            "month":g.current_month
        },
        "end":{
            "year":g.current_year+72,
            "month":12
        },
        "cash":{
            "amount":50,
            "rate":0.2
        },
        "option":{
            "init":True,
            "income":True,
            "stock":False,
            "NISA":False,
            "iDeCo":False,
            "DC":False,
            "retirement":False,
            "housing":False,
            "daily":False,
            "special":False,
            "car":False,
            "education":False,
            "nursing_care":False
        }
    }

if __name__ == "__main__":
    # グローバル変数の初期化
    init_global_var()
    # メインウィンドウの作成
    main_window = tk.Tk()
    GUI.HP(main_window)
    main_window.mainloop()