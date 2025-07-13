import global_var as g
import json
import csv
import random
import platform
import numpy as np
import matplotlib as mpl
from matplotlib.ticker import FuncFormatter, FixedLocator
import matplotlib.pyplot as plt
from itertools import accumulate
import pandas as pd
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, filedialog
from collections import defaultdict

def update_global_param_from_var():
    """  基本タブ  """
    # 基本情報
    g.params["birth"]["year"] = int(g.birth_year_var.get())
    g.params["birth"]["month"] = int(g.birth_month_var.get())
    g.params["start"]["year"] = int(g.start_year_var.get())
    g.params["start"]["month"] = int(g.start_month_var.get())
    g.params["end"]["year"] = int(g.end_year_var.get())
    g.params["end"]["month"] = int(g.end_month_var.get())
    g.params["cash"]["amount"] = int(g.cash_amount_var.get())
    g.params["cash"]["rate"] = float(g.cash_rate_var.get())

    # オプション
    g.params["option"]["init"] = g.init_option.get()
    g.params["option"]["income"] = g.income_option.get()
    g.params["option"]["stock"] = g.stock_option.get()
    g.params["option"]["NISA"] = g.NISA_option.get()
    g.params["option"]["iDeCo"] = g.iDeCo_option.get()
    g.params["option"]["DC"] = g.DC_option.get()
    g.params["option"]["retirement"] = g.retirement_option.get()
    g.params["option"]["housing"] = g.housing_option.get()
    g.params["option"]["daily"] = g.daily_option.get()
    g.params["option"]["special"] = g.special_option.get()
    g.params["option"]["car"] = g.car_option.get()
    g.params["option"]["education"] = g.education_option.get()
    g.params["option"]["nursing_care"] = g.nursing_care_option.get()

    """  給与  """

    """  住居  """

    """  日常  """

    """  教育  """

    """  介護  """

def set_var_from_global_param():
    g.birth_year_var.set(str(g.params["birth"]["year"]))
    g.birth_month_var.set(str(g.params["birth"]["month"]))
    g.start_year_var.set(str(g.params["start"]["year"]))
    g.start_month_var.set(str(g.params["start"]["month"]))
    g.end_year_var.set(str(g.params["end"]["year"]))
    g.end_month_var.set(str(g.params["end"]["month"]))
    g.cash_amount_var.set(str(g.params["cash"]["amount"]))
    g.cash_rate_var.set(str(g.params["cash"]["rate"]))
    # オプション
    g.init_option.set(g.params["option"]["init"])
    g.income_option.set(g.params["option"]["income"])
    g.stock_option.set(g.params["option"]["stock"])
    g.DC_option.set(g.params["option"]["NISA"])
    g.NISA_option.set(g.params["option"]["DC"])
    g.iDeCo_option.set(g.params["option"]["iDeCo"])
    g.DC_option.set(g.params["option"]["DC"])
    g.retirement_option.set(g.params["option"]["retirement"])
    g.housing_option.set(g.params["option"]["housing"])
    g.daily_option.set(g.params["option"]["daily"])
    g.special_option.set(g.params["option"]["special"])
    g.car_option.set(g.params["option"]["car"])
    g.education_option.set(g.params["option"]["education"])
    g.nursing_care_option.set(g.params["option"]["nursing_care"])

def toggle_tabs():
    # チェックボックスの状態に応じてタブを表示/非表示
    # すべてのタブを一度削除
    for tab in [g.income_tab, g.stock_tab, g.NISA_tab, g.iDeCo_tab, g.DC_tab, g.retirement_tab, g.housing_tab, g.daily_tab, g.special_tab, g.car_tab, g.education_tab, g.nursing_care_tab]:
        try:
            g.notebook.forget(tab)
        except:
            pass

    # チェックされたオプションのみタブ追加
    if g.income_option.get():
        g.notebook.add(g.income_tab, text="給与")
    if g.stock_option.get():
        g.notebook.add(g.stock_tab, text="投資")
    if g.NISA_option.get():
        g.notebook.add(g.NISA_tab, text="NISA")
    if g.iDeCo_option.get():
        g.notebook.add(g.iDeCo_tab, text="iDeCo")
    if g.DC_option.get():
        g.notebook.add(g.DC_tab, text="DC")
    if g.retirement_option.get():
        g.notebook.add(g.retirement_tab, text="退職金")
    if g.housing_option.get():
        g.notebook.add(g.housing_tab, text="住居")
    if g.daily_option.get():
        g.notebook.add(g.daily_tab, text="日常")
    if g.special_option.get():
        g.notebook.add(g.special_tab, text="特別")
    if g.car_option.get():
        g.notebook.add(g.car_tab, text="車")
    if g.education_option.get():
        g.notebook.add(g.education_tab, text="教育")
    if g.nursing_care_option.get():
        g.notebook.add(g.nursing_care_tab, text="介護")

def export_json():
    update_global_param_from_var()
    try:
        file_path = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
            title="設定ファイルとして保存"
        )
        
        if file_path:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(g.params, f, ensure_ascii=False, indent=4)
            
            messagebox.showinfo("成功", f"データをJSONファイルに保存しました:\n{file_path}")
            
    except ValueError as e:
        messagebox.showerror("エラー", f"正しい値を入力してください:\n{str(e)}")
    except Exception as e:
        messagebox.showerror("エラー", f"ファイルの保存中にエラーが発生しました:\n{str(e)}")

def import_json():
    try:
        file_path = filedialog.askopenfilename(
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
            title="読み込む設定ファイルを選択"
        )
        
        if file_path:
            with open(file_path, 'rt', encoding='utf-8') as f:
                g.params = json.load(f)		# JSONのファイル内容をdictに変換する。
                set_var_from_global_param()

            # タブの表示状態を更新
            toggle_tabs()
            
            messagebox.showinfo("成功", f"JSONファイルからデータを読み込みました:\n{file_path}")
            
    except json.JSONDecodeError:
        messagebox.showerror("エラー", "無効なJSONファイルです")
    except Exception as e:
        messagebox.showerror("エラー", f"ファイルの読み込み中にエラーが発生しました:\n{str(e)}")


def sort_csv_file(input_filename, output_filename=None):
    # CSVファイルを読み込み
    with open(input_filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
    
    # 年（1列目）と月（2列目）でソート（整数として比較）
    sorted_rows = sorted(rows, key=lambda x: (int(x[0]), int(x[1])))
    
    # 結果を出力（標準出力またはファイル）
    if output_filename:
        with open(output_filename, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(sorted_rows)
        print(f"ソート結果を {output_filename} に保存しました")
    else:
        print("ソート結果:")
        for row in sorted_rows:
            print(','.join(row))
            
def covert_to_graph_data_from_simulate_data(input_filename, output_filename):
    # 再帰的にネストする辞書を生成
    def nested_dict():
        return defaultdict(nested_dict)

    csv_header = list()   
    # CSVファイルを読み込む
    with open(input_filename, 'r', newline='', encoding='utf-8') as infile:

        reader = csv.reader(infile)
        # 4次元辞書を初期化
        data_base = nested_dict()

        for row in reader:
            year = row[0]
            month = row[1]
            amount = int(row[2])
            money_type_str = row[3].split('.')[-1]  # "MoneyType.CASH" → "CASH"

            if year not in data_base:
                data_base[year] = {}
            if month not in data_base[year]:
                data_base[year][month] = {}
            if money_type_str not in data_base[year][month]:
                data_base[year][month][money_type_str] = list()
            if money_type_str not in csv_header:
                csv_header.append(money_type_str)

            # 要素の追加
            data_base[year][month][money_type_str].append(amount)

    with open(output_filename, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        csv_header.insert(0, 'date')
        writer.writerow(csv_header)  # 出力ファイルのヘッダー
        
        # 初期状態の資産情報を追加
        pass

        # シミュレーション結果を追加
        for year_i in data_base:
            for month_i in data_base[year_i]:
                date = f"{year_i}-{month_i}"
                money_type = list()
                for type_i in data_base[year_i][month_i]:
                    money_type.append(type_i)
                writer.writerow([date, sum(data_base[year_i][month_i][type_i])])

def out_graph_from_graph_data(input_filename, output_filename=None):
    # 日本語フォント設定
    os_name = platform.system()
    if os_name == 'Windows':
        mpl.rcParams['font.family'] = 'Meiryo'              # Windows
    elif os_name == 'Darwin':
        mpl.rcParams['font.family'] = 'Hiragino Sans'       # Mac
    elif os_name == 'Linux':
        mpl.rcParams['font.family'] = 'Noto Sans CJK JP'    # Linux

    # 折れ線グラフ用の色
    line_color = '#8a807d'
    # あらかじめ定義した10色のカラーパレット
    predefined_colors = [
        '#FF9999',  # 薄い赤
        '#66B3FF',  # 薄い青
        '#99FF99',  # 薄い緑
        '#FFCC99',  # 薄いオレンジ
        '#CC99FF',  # 薄い紫
        '#FFFF99',  # 薄い黄
        '#FF99CC',  # 薄いピンク
        '#99FFFF',  # 薄い水色
        '#D2B48C',  # 薄い茶色
        '#FF6666'   # 少し濃い赤
    ]

    # 禁止色の設定
    excluded_colors = predefined_colors + [line_color]

    # 表示色の生成関数
    def generate_random_color(excluded):
        while True:
            # ランダムな色を生成（16進数カラーコード）
            color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
            # 明るすぎず暗すぎない色を選ぶ（視認性確保）
            r, g, b = int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)
            brightness = (r * 299 + g * 587 + b * 114) / 1000
            if color not in excluded and 100 <= brightness <= 200:
                return color

    try:
        df = pd.read_csv(input_filename)  # CSVファイルを読み込み
        headers = df.columns.tolist()  # ヘッダーをリストとして取得
        
        if len(headers) < 2:
            print("❌ グラフ描画に必要なデータが不足しています")
            return

        date = df.iloc[:, 0].values  # 1列目をx軸データ
        
        # 積み上げグラフ用のデータと負債データを分離
        stack_headers = []
        line_headers = []
        
        # ヘッダー名から積み上げグラフ用と折れ線グラフ用を判別
        for header in headers[1:]:  # 最初の列はx軸なのでスキップ
            if '負債' in header:
                line_headers.append(header)
            else:
                stack_headers.append(header)
        
        # Y軸を通貨表記に設定
        def currency_formatter(x, pos):
            return f'¥{x:,.0f}'

        def currency_formatter2(x, pos):
                    return f'{x/10000:,.0f}万円'  # 万円単位に変換


        plt.figure(figsize=(12, 6))
        plt.margins(x=0)  # 左端の余白を削除
        plt.gca().yaxis.set_major_formatter(FuncFormatter(currency_formatter2))

        # 積み上げ面グラフの描画（スタック可能なデータがある場合）
        if stack_headers:
            stack_data = [df[header].values for header in stack_headers]

            # 累積データに変換
            cumulative_data = list()
            # ToDo:累積データの初期値を記入
            pass
            for arr_data in stack_data:
                cumulative_arr = np.fromiter(accumulate(arr_data), dtype=int)
                cumulative_data.append(cumulative_arr)

            # 色の決定: 最初の10個は定義済みカラー、それ以降は自動生成
            if len(stack_headers) <= len(predefined_colors):
                colors = predefined_colors[:len(stack_headers)]
            else:
                # 11個目以降は自動的に色を生成
                additional_colors = [generate_random_color(excluded_colors) for _ in range(len(stack_headers) - len(predefined_colors))]
                colors = predefined_colors + additional_colors
            
            plt.stackplot(
                date, *cumulative_data,
                labels=stack_headers,
                alpha=0.5,
                colors=colors
            )

        # 折れ線グラフの描画（負債データがある場合）
        if line_headers:
            for i, line_header in enumerate(line_headers):
                y_line = df[line_header].values
                
                plt.plot(date, y_line,
                        color=line_color,
                        linewidth=1.5,
                        marker='o',
                        markersize=3,
                        label=line_header,
                        zorder=2)

        # グラフの装飾
        plt.title('資産推移(シミュレーション結果)', fontsize=14)
        plt.legend(loc='upper left')
        plt.grid(axis='y', alpha=0.3)
        # X軸のラベル間引き設定（最初と最後のラベルを必ず表示）
        ax = plt.gca()
        n = len(date)
        step = max(1, n // 10)  # 10個程度に間引くが、最低1つは間隔を空ける
        indices = list(range(0, n, step)) + [n - 1]  # 最後のラベルを必ず含める
        indices = sorted(list(set(indices)))  # 重複を削除
        ax.xaxis.set_major_locator(FixedLocator(indices))  # 指定した位置にラベルを表示
        plt.xticks(rotation=50, ha='right')  # 横軸ラベルを斜め50度に
        
        # ラベルが重ならないようにレイアウト調整
        plt.tight_layout()

        if output_filename:
            # PNGで保存
            plt.savefig(output_filename, dpi=300, bbox_inches='tight')
        else:
            # グラフを表示
            plt.gcf().canvas.manager.set_window_title("シミュレーション結果")
            plt.show()

    except FileNotFoundError:
        print(f"❌ '{input_filename}' が存在しません。")
    except Exception as e:
        print(f"❌ エラーが発生しました: {str(e)}")