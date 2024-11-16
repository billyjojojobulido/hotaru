import os
import tkinter
from tkinter import ttk
from tkinter import Label, Tk, LabelFrame, Entry, Button, StringVar
from tkinter.filedialog import askopenfilename, askdirectory
from audio_manager.utils import get_config_file


class Window:

    def __init__(self):
        # attr初始化
        self.root = Tk()
        self.init_window_frame = LabelFrame(self.root, text="")
        self.init_window_frame.place(relx=0.1, rely=0.075, relwidth=0.8, relheight=0.85)

        # 数据变量
        self.audio_combo_list = None    # 机经音频选择下拉框
        self.audio_id = -1

        # 设置根窗口属性
        self.root.title("Hotaru")
        self.root.attributes("-alpha", 1)

        self.center_window(600, 400)

        self.create_page()


    """
    界面功能初始化
    """
    def create_page(self):
        Label(self.root).grid(row=0, sticky='W', pady=10)
        # 第一行选项 - 源文件
        Label(self.init_window_frame).grid(row=1, column=0, padx=30)
        Label(self.init_window_frame, text="请选择机经序号: ").grid(row=1, column=1, sticky='W', pady=10)

        # self.src_entry.grid(row=1, column=1, sticky='E')

        self.audio_combo_list = ttk.Combobox(
            self.init_window_frame,
            textvariable=self.audio_id,
            state='readonly',
            width=25,
        )

        self.audio_combo_list.focus()

        config_data = get_config_file()

        self.audio_combo_list['values'] = (
            [str(x["id"]) + " " + x["file_name"] for x in config_data]
        )
        self.audio_combo_list.current(0)   # 默认选择第一个
        self.audio_combo_list.bind("<<ComboboxSelected>>", self.on_select)

        self.audio_combo_list.grid(row=1, column=2, sticky='E')

    def on_select(self, event):
        # 阻止选中文本
        self.audio_combo_list.event_generate('<Escape>')  # 尝试生成一个退出事件以清除可能的焦点状态
        event.widget.selection_clear()

    def create_button(self, name, callback):
        return ttk.Button(self.root, text=name, command=callback)

    def on_click_audio_chosen():
        print("音频已被选择")

    def on_click_audio_play():
        print("开始播放音频")

    def on_click_play_next():
        print("开始播放下一段音频")


    """
    调整屏幕大小 和 位置
    """
    def center_window(self, width, height):
        # 获取屏幕尺寸以及计算位置
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        self.root.geometry(f'{width}x{height}+{x}+{y}')


    # 获取音频下拉框的内容 (str)
    def get_audio_id(self, event):
        self.audio_id = self.audio_combo_list.get()

    def run(self):
        self.init_window_frame.mainloop()