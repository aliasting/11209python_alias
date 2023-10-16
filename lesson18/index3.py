'''
學習Canvas
'''
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)        
        self.title("Image")
        self.geometry("300x250")
        self.configure(background='#E79460')

class MyFrame(ttk.LabelFrame):
    def __init__(self,master,title,**kwargs):
        super().__init__(master,text=title,**kwargs)
        #self.configure(background='#9E7A7A')
        ttk.Radiobutton(self,text="左邊",value='left').grid(column=0,row=0,padx=10)
        ttk.Radiobutton(self,text="中間",value='center').grid(column=1,row=0,padx=10)
        ttk.Radiobutton(self,text="右邊",value='right').grid(column=2,row=0,padx=10)
        self.pack(padx=10,pady=10)
        #self.pack(expand=1, fill='x',padx=10,pady=10)


def main():    
    window = Window()
    myFrame = MyFrame(window,"對齊方式")
    window.mainloop()

if __name__ == "__main__":
    main()