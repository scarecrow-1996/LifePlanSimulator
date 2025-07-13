import global_var as g
import utility
import os

def run():
    print("シミュレーション開始")

    """  初期化  """
    if not os.path.exists(g.out_dir):
        os.mkdir(g.out_dir)

    if g.init_option.get():
        if os.path.exists(g.csv_out_data):
            os.remove(g.csv_out_data)
            print(f"✅ '{g.csv_out_data}' の初期化に成功しました。")
        else:
            print(f"❌ '{g.csv_out_data}' は見つかりませんでした。")

    """  シミュレーション処理  """
    # チェックされたオプションのみ実行
    if g.income_option.get():
        print("収入 Comming Soon..")
    if g.stock_option.get():
        print("投資 Comming Soon..")
    if g.NISA_option.get():
        print("NISA Comming Soon..")
    if g.iDeCo_option.get():
        print("iDeCo Comming Soon..")
    if g.DC_option.get():
        print("DC Comming Soon..")
    if g.retirement_option.get():
        print("退職金 Comming Soon..")
    if g.housing_option.get():
        print("住居 Comming Soon..")
    if g.daily_option.get():
        print("日常 Comming Soon..")
    if g.special_option.get():
        print("特別 Comming Soon..")
    if g.car_option.get():
        print("車 Comming Soon..")
    if g.education_option.get():
        print("教育 Comming Soon..")
    if g.nursing_care_option.get():
        print("介護 Comming Soon..")


    """  データ解析処理  """
    utility.sort_csv_file(g.csv_out_data, g.csv_out_data)
    utility.covert_to_graph_data_from_simulate_data(g.csv_out_data, g.csv_out_graph)
    # common.out_graph_from_graph_data(g.csv_out_graph, g.png_out_graph)
    utility.out_graph_from_graph_data(g.csv_out_graph)


    """  レポート作成処理  """
    pass


    print("completed!")


