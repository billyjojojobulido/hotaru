import customtkinter
from audio_manager import get_config_file

FONT_TITLE = ("Helvetica", 16, "bold")

class SettingPanel(customtkinter.CTkFrame):
            
    def __init__(self, root: customtkinter.CTk, auto_play_event, turbo_event, count_down_event):
        super().__init__(root)
        
        self.label_setting_group = customtkinter.CTkLabel(master=self, text="设置面板", font=FONT_TITLE)
        self.label_setting_group.grid(row=0, column=0, padx=10, pady=5)

        self.auto_play = customtkinter.CTkSwitch(master=self, text="点击下一个时自动播放", command=auto_play_event)
        self.auto_play.grid(row=1, column=0, padx=20, pady=10)

        self.turbo = customtkinter.CTkSwitch(master=self, text="挑战模式: 1.5倍速播放", command=turbo_event)
        self.turbo.configure(state="disabled")
        self.turbo.grid(row=2, column=0, padx=20, pady=10)

        self.count_down = customtkinter.CTkSwitch(master=self, text="播放结束后五秒倒计时", command=count_down_event)
        self.count_down.configure(state="disabled")
        self.count_down.grid(row=3, column=0, padx=20, pady=10)