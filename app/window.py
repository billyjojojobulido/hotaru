import os
import tkinter
from tkinter import ttk
from tkinter import Label, Tk, LabelFrame, Entry, Button, StringVar
from tkinter.filedialog import askopenfilename, askdirectory


class Window:

    def __init__(self):
        # attr初始化
        self.root = Tk()
        self.init_window_frame = LabelFrame(self.root, text="")
        self.init_window_frame.place(relx=0.1, rely=0.15, relwidth=0.8, relheight=0.7)

        # 设置根窗口属性
        self.root.title("Hotaru")
        self.root.geometry("600x400")
        self.root.attributes("-alpha", 1)

    def run(self):
        self.init_window_frame.mainloop()