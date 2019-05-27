# -*- coding: utf-8 -*-
"""
さんざん苦労した、「label等を配置した frame」のスクロール
Created on Fri May  10 16:48:43 2019

@author: bluep
"""
import tkinter as tk
import tkinter.ttk as ttk


class Frame(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title("colors")
        self.pack(fill=tk.BOTH, expand=1)
        # self.master.geometry("400x800")

        self.create_widgets()
        self.create_layout()
        self.create_bindings()

        self.set_colors(self.frame2)

    def create_widgets(self):
        # スクロール対象の canvas
        self.mycanvas = tk.Canvas(self)

        # 垂直スクロールバー
        self.myscb = tk.Scrollbar(
            self,
            orient='vertical',
            command=self.mycanvas.yview
            # スクロールバーをcanvasに接続↑
        )
        # self.mycanvas['yscrollcommand'] = self.myscb.set
        self.mycanvas.configure(yscrollcommand=self.myscb.set)
        # canvasのスクロール位置を、スクロールバーに反映↑

        # スクロール対象の frame（canvasの上に貼る）
        self.frame2 = tk.Frame(self.mycanvas)

    def create_layout(self):
        self.myscb.pack(side=tk.RIGHT, fill=tk.Y)
        # mycanvas.config(scrollregion=(0, 0, 500, 800))
        self.mycanvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        self.mycanvas.create_window((0, 0), window=self.frame2, anchor=tk.NW)

    def y_scroll(self, event):
        """
        <MouseWheel>にバインドした垂直スクロール動作
        """
        print("Wheel delta = ", event.delta)
        # self.mycanvas.yview('scroll', int(-1*event.delta/60), 'units')
        self.mycanvas.yview('scroll', 1 if event.delta < 0 else -1, 'units')
        """
        delta、マイナスがスクロールアップ
        windowsだと、１クリックが -120/120
        Macだと、1クリックで -1/1
        Mac/MagicMouseだと、-10～10くらい、フリクションあり
        ※現在は delta量は無視して、上か下かだけ設定している↑
        """

    def create_bindings(self):
        def set_scrollregion(event):
            self.mycanvas.configure(scrollregion=self.mycanvas.bbox("all"))
        # ↓frame2の大きさに合わせて、↑mycanvasのスクロール範囲を設定
        self.frame2.bind("<Configure>", set_scrollregion)

        self.mycanvas.bind("<MouseWheel>", self.y_scroll)
        self.frame2.bind("<MouseWheel>", self.y_scroll)

    def set_colors(self, myframe):
        """
        フレーム(myframe)の中に、カラー情報のラベルをセットする
        """
        colors = def_colors()
        for i, color in enumerate(colors):
            colorhex = "#{0:02x}{1:02x}{2:02x}".format(
                int(color[1]), int(color[2]), int(color[3])
            )

            label = tk.Label(myframe, text=color[0], bg="white", relief=tk.GROOVE)
            label.grid(row=i, column=0, sticky="news", padx="0.5m")
            label.bind("<MouseWheel>", self.y_scroll)

            label = tk.Label(myframe, text=color[0], bg=color[0], relief=tk.GROOVE)
            label.grid(row=i, column=1, sticky="news")
            label.bind("<MouseWheel>", self.y_scroll)

            label = tk.Label(myframe, text=colorhex, bg=colorhex, relief=tk.GROOVE)
            label.grid(row=i, column=2, sticky="news", ipadx=5)
            label.bind("<MouseWheel>", self.y_scroll)

            label = tk.Label(myframe, text=colorhex, bg="white", relief=tk.GROOVE)
            label.grid(row=i, column=3, sticky="news", ipadx=5)
            label.bind("<MouseWheel>", self.y_scroll)


def def_colors():
    wcolors = [
        ["spring green", "0", "255", "127"],
        ["SpringGreen", "0", "255", "127"],
        ["SpringGreen1", "0", "255", "127"],
        ["SpringGreen2", "0", "238", "118"],
        ["SpringGreen3", "0", "205", "102"],
        ["SpringGreen4", "0", "139", "69"],
        ["steel blue", "70", "130", "180"],
        ["SteelBlue", "70", "130", "180"],
        ["SteelBlue1", "99", "184", "255"],
        ["SteelBlue2", "92", "172", "238"],
        ["SteelBlue3", "79", "148", "205"],
        ["SteelBlue4", "54", "100", "139"],
        ["tan", "210", "180", "140"],
        ["tan1", "255", "165", "79"],
        ["tan2", "238", "154", "73"],
        ["tan3", "205", "133", "63"],
        ["tan4", "139", "90", "43"],
        ["thistle", "216", "191", "216"],
        ["thistle1", "255", "225", "255"],
        ["thistle2", "238", "210", "238"],
        ["thistle3", "205", "181", "205"],
        ["thistle4", "139", "123", "139"],
        ["tomato", "255", "99", "71"],
        ["tomato1", "255", "99", "71"],
        ["tomato2", "238", "92", "66"],
        ["tomato3", "205", "79", "57"],
        ["turquoise", "64", "224", "208"],
        ["turquoise1", "0", "245", "255"],
        ["turquoise2", "0", "229", "238"],
        ["turquoise3", "0", "197", "205"],
        ["turquoise4", "0", "134", "139"],
        ["violet", "238", "130", "238"],
        ["violet red", "208", "32", "144"],
        ["VioletRed", "208", "32", "144"],
        ["VioletRed1", "255", "62", "150"],
        ["VioletRed2", "238", "58", "140"],
        ["VioletRed3", "205", "50", "120"],
        ["VioletRed4", "139", "34", "82"],
        ["wheat", "245", "222", "179"],
        ["wheat1", "255", "231", "186"],
        ["wheat2", "238", "216", "174"],
        ["wheat3", "205", "186", "150"],
        ["wheat4", "139", "126", "102"],
        ["white", "255", "255", "255"],
        ["white smoke", "245", "245", "245"],
        ["WhiteSmoke", "245", "245", "245"],
        ["yellow", "255", "255", "0"],
        ["yellow green", "154", "205", "50"],
        ["yellow1", "255", "255", "0"],
        ["yellow2", "238", "238", "0"],
        ["yellow3", "205", "205", "0"],
        ["yellow4", "139", "139", "0"],
        ["white", "170", "76", "143"],
    ]
    return wcolors


# ----------------
if __name__ == "__main__":
    root = tk.Tk()
    f = Frame(master=root)
    # f.pack(fill=tk.BOTH, expand=1)
    f.mainloop()
