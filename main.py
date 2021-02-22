import tkinter as tk
from tkinter import ttk
import json


def init_notebook(notebook):
    names = ["時間割", "授業開始", "授業終了"]
    """
    クラス化しても良かったのですが、あまり再利用することがない処理のため関数にしました。

    無闇にクラス化すると、"self"をたくさん書かなくてはいけなくなったりします。
    """

    tab1 = ttk.Frame(notebook)
    tab2 = ttk.Frame(notebook)
    tab3 = ttk.Frame(notebook)
    tabs = [tab1, tab2, tab3]
    i = 0

    # 時間割タブ(tab1)
    for vr in range(0, 5):
        for hr in range(0, 7):
            table = ttk.Button(tab1, text="ele")
            table.grid(column=hr, row=vr, sticky=(tk.N, tk.W, tk.E, tk.S))

    # 授業開始タブ(tab2)
    # 授業終了タブ(tab3)
    i = 0
    for tab in tabs:
        name = names[i]
        i += 1
       # button = ttk.Button(tab, text="ボタン")
        # button.pack()
        notebook.add(tab, text=name)

    return notebook


def init_tab(tab):
    button = ttk.Button(tab, text="ボタン")
    tab.add(button)


class ScrolledCanvas(tk.Canvas):
    """
    スクロールバー付きのキャンバスは再利用の機会は高そうなので、個別のクラスに纏める。

    スクロールを付けるクラスの拡張方法は、他にもあり
    異なるアプローチですが ScrolledText のソース等も参考にしてみて下さい。
    """

    def __init__(self, master, *args, **kw):
        super().__init__(master, *args, **kw)

        bar_y = ttk.Scrollbar(self, orient=tk.VERTICAL)
        bar_y.pack(side=tk.RIGHT, fill=tk.Y)
        bar_y.config(command=self.yview)

        bar_x = ttk.Scrollbar(self, orient=tk.HORIZONTAL)
        bar_x.pack(side=tk.BOTTOM, fill=tk.X)
        bar_x.config(command=self.yview)

        self.config(
            yscrollcommand=bar_y.set,
            xscrollcommand=bar_x.set,
            scrollregion=self.bbox("all"),
        )
        # ※ ウィジェットをクラス化する際の注意点
        # ここでこのクラスのコンテナである canvas の pack()/grid() 等のレイアウトは呼びません。
        # 例えば grid() を呼び出すと、pack() では使えないクラスになってしまいます。


class MainWindow(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # XXX:
        # 例えば、ここで master.title() を呼び出すと、親にはToplevelしか取れなくなるので
        # クラス内では親のメソッドを呼び出すのは控えます。
        # そうすることで、Toplevel以外の親を持つことができ
        # このクラス自体を他のクラスの部品の一部として扱えるようになります。

        canvas = ScrolledCanvas(self)
        canvas.pack(fill=tk.BOTH, expand=True)  # <- 配置は利用側で決める

        notebook = init_notebook(ttk.Notebook(self))
        notebook.pack(fill=tk.BOTH, expand=True)

        canvas.create_window((10, 10),
                             window=notebook, anchor=tk.NW, width=canvas.cget('width'))

        self.canvas = canvas
        self.notebook = notebook


def main():
    root = tk.Tk()
    root.geometry("800x800")
    root.title("テスト")

    win = MainWindow(root)
    win.pack(fill=tk.BOTH, expand=True)

    root.mainloop()


if __name__ == '__main__':
    main()
