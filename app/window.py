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

        # 数据变量
        self.audio_combo_list = None    # 机经音频选择下拉框
        self.audio_id = -1

        # 设置根窗口属性
        self.root.title("Hotaru")
        self.root.geometry("600x400")
        self.root.attributes("-alpha", 1)

        self.create_page()


    """
    界面功能初始化
    """
    def create_page(self):
        Label(self.root).grid(row=0, stick='W', pady=10)
        # 第一行选项 - 源文件
        Label(self.init_window_frame).grid(row=1, column=0, padx=30)
        Label(self.init_window_frame, text="请选择机经序号: ").grid(row=1, column=1, stick='W', pady=10)

        # self.src_entry.grid(row=1, column=1, stick='E')

        self.audio_combo_list = ttk.Combobox(
            self.init_window_frame,
            textvariable=self.audio_id,
            width=20,
        )
        self.audio_combo_list['values'] = (
            "70001", "70002", "70003", "70004", "70090"
        )
        self.audio_combo_list.current(0)   # 默认选择"一月"
        # self.audio_combo_list.bind("<<ComboboxSelected>>", self.get_month)

        self.audio_combo_list.grid(row=1, column=2, stick='W')

    def run(self):
        self.init_window_frame.mainloop()