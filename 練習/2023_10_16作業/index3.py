import tkinter as tk
from tkinter import Misc, ttk
from PIL import Image, ImageTk
from tkinter.simpledialog import Dialog
import csv


class Window(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title("台積電")


class GetPassword(Dialog):
    def __init__(self, master, value) : 
        self.value=value
        super().__init__(master)
       
    def body(self, master):
        self.title("台積電")

        tk.Label(master, text="日期:").grid(row=0, sticky=tk.W)
        tk.Label(master, text="開盤價:").grid(row=1, sticky=tk.W)
        tk.Label(master, text="盤中高點:").grid(row=2, sticky=tk.W)
        tk.Label(master, text="盤中低點:").grid(row=3, sticky=tk.W)
        tk.Label(master, text="收盤價:").grid(row=4, sticky=tk.W)
        tk.Label(master, text="調整後收盤價:").grid(row=5, sticky=tk.W)
        tk.Label(master, text="成交量:").grid(row=6, sticky=tk.W)

        tk.Label(master, text=self.value[0]).grid(row=0, column=1,sticky=tk.E) 
        tk.Label(master, text=self.value[1]).grid(row=1, column=1,sticky=tk.E)
        tk.Label(master, text=self.value[2]).grid(row=2, column=1,sticky=tk.E)
        tk.Label(master, text=self.value[3]).grid(row=3, column=1,sticky=tk.E)
        tk.Label(master, text=self.value[4]).grid(row=4, column=1,sticky=tk.E)
        tk.Label(master, text=self.value[5]).grid(row=5, column=1,sticky=tk.E)
        tk.Label(master, text=self.value[6]).grid(row=6, column=1,sticky=tk.E)

        

    def buttonbox(self):
        """add standard button box.

        override if you do not want the standard buttons
        """

        box = tk.Frame(self)

        w = tk.Button(box, text="確認", width=10, command=self.ok, default=tk.ACTIVE)
        w.pack(side=tk.LEFT, padx=5, pady=5)
        w = tk.Button(box, text="取消", width=10, command=self.cancel)
        w.pack(side=tk.LEFT, padx=5, pady=5)

        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)

        box.pack()


class MyFrame(tk.LabelFrame):
    def __init__(self, master, title, **kwargs):
        super().__init__(master, text=title, **kwargs)
        self.pack(expand=1, fill="both", padx=10, pady=10)

        self.tree = ttk.Treeview(
            self, columns=["#1", "#2", "#3", "#4", "#5", "#6", "#7"], show="headings"
        )
        self.tree.heading("#1", text="日期")
        self.tree.heading("#2", text="開盤價")
        self.tree.heading("#3", text="盤中高點")
        self.tree.heading("#4", text="盤中低點")
        self.tree.heading("#5", text="收盤價")
        self.tree.heading("#6", text="調整後收盤價")
        self.tree.heading("#7", text="成交量")

        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.tree.config(yscrollcommand=self.scrollbar.set)

        with open("台積電.csv") as file:
            read = csv.DictReader(file)
            for n in read:
                date = n["Date"]
                op = n["Open"]
                high = n["High"]
                low = n["Low"]
                close = n["Close"]
                adjClose = n["Adj Close"]
                volume = n["Volume"]
                self.tree.insert(
                    "", tk.END, value=(date, op, high, low, close, adjClose, volume)
                )
            self.tree.pack()
        self.tree.bind("<<TreeviewSelect>>", self.item_selected)

    def item_selected(self, event):
        item_id = self.tree.selection()[0]
        item_dict = self.tree.item(item_id)
        y=item_dict["values"]
        dialog = GetPassword(self,value=y)



def main():
    window = Window()
    myFrame = MyFrame(window, "台積電")
    window.mainloop()


if __name__ == "__main__":
    main()
