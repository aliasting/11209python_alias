import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datasource

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        try:
            datasource.download_youbike_data()
        except Exception:# as e可取消
            messagebox.showerror("錯誤",f'{e}\n將關閉應用程式\n請稍後再試')
            self.destroy()
            #print(e)取消
        

def main():
    window = Window()
    window.title('台北市youbike2.0')
    window.geometry('600x300')
    window.resizable(width=False,height=False) #固定視窗,無法大小   
    window.mainloop()

if __name__ == '__main__':
    main()