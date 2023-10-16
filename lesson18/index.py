'''
學習Canvas
'''
import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.geometry("400x250+300+300")
        self.title("Lines")
        self.configure(background='#E79460')

class MyFrame(tk.Frame):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)
        self.configure(background='#9E7A7A')
        canvas = tk.Canvas(self)
        canvas.create_line(15, 30, 200, 30)
        canvas.create_line(300, 35, 300, 200, dash=(4, 2))
        canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85)
        canvas.pack(expand=1,fill='both')
        self.pack(expand=1, fill='both')


def main():    
    window = Window()
    myFrame = MyFrame(window)
    window.mainloop()

if __name__ == "__main__":
    main()