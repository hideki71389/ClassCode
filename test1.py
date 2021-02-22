import json

with open("./table.json", encoding="utf_8") as js:
    dict = json.load(js)
    dict_m = dict["monday"]
    print(dict_m["second"])

"""    tree = ttk.Treeview(tab1)

    # 列インデックスの作成
    tree["columns"] = (1, 2, 3, 4, 5, 6, 7)
    # 表スタイルの設定(headingsはツリー形式ではない、通常の表形式)
    tree["show"] = "headings"
    # 各列の設定(インデックス,オプション(今回は幅を指定))
    for i in range(1, 8):
        tree.column(i, width=50)
    # 各列のヘッダー設定(インデックス,テキスト)
    tree.heading(1, text="土曜日")
    tree.heading(2, text="月曜日")
    tree.heading(3, text="火曜日")
    tree.heading(4, text="水曜日")
    tree.heading(5, text="木曜日")
    tree.heading(6, text="金曜日")
    tree.heading(7, text="日曜日")

    # レコードの作成
    # 1番目の引数-配置場所（ツリー形式にしない表設定ではブランクとする）
    # 2番目の引数-end:表の配置順序を最下部に配置
    #             (行インデックス番号を指定することもできる)
    # 3番目の引数-values:レコードの値をタプルで指定する
    tree.insert("", "end", values=("2017/5/1", "食費", 3500))
    tree.insert("", "end", values=("2017/5/10", "光熱費", 7800))
    tree.insert("", "end", values=("2017/5/10", "住宅費", 64000))

    # ツリービューの配置
    tree.pack()
"""
