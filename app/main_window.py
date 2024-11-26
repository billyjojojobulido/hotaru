import customtkinter
from audio_manager import get_config_file, construct_audio_loop
from component import Console, AudioPanel, SettingPanel, ControllerPanel

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

FONT_TITLE = ("Helvetica", 16, "bold")
VERSION ="Hotaru - v1.0.4"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        ################
        #region 服务端部分 ###
        ################
        self.engine = None
        #endregion


        ################
        #region UI部分 ###
        ################
        # configure window
        self.title(VERSION)
        # self.geometry(f"{800}x{640}")

        self.geometry(f"{720}x{480}")
        #endregion

        ################
        #region 变量部分 ###
        ################
        self._auto_play_enabled = False
        self._turbo_enabled = False
        self._count_down_enabled = False
        self.textbox_index = 0
        #endregion

        # configure grid layout (4x4)
        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(1, weight=1)
        # self.grid_rowconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)


        #region 显示器部分GUI
        self.textbox = Console(self)
        self.textbox.grid(row=0, column=0, rowspan=2, padx=(20, 10), pady=(20, 10), sticky="nsew")
        #endregion


        #region 选择音频菜单GUI
        self.audio_frame = AudioPanel(self, start_engine=self.start_engine)
        self.audio_frame.grid(row=0, column=1, rowspan=2, padx=(20, 20), pady=(20, 10), sticky="nsew")
        self.audio_frame.grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        #endregion


        #region 设置面板GUI
        self.setting_frame = SettingPanel(self, auto_play_event=self._on_click_auto_play, turbo_event=self._on_click_turbo, 
                                          count_down_event=self._on_click_count_down)
        self.setting_frame.grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.setting_frame.grid(row=2, column=1, padx=(20, 20), pady=(10, 20), sticky="nsew")
        #endregion

        #region 播放面板GUI
        self.controller_frame = ControllerPanel(self, play_event=self._play, next_event=self._next)
        self.controller_frame.grid(row=2, column=0, padx=(20, 10), pady=(10, 20), sticky="nsew")
        #endregion


    #region 播放功能相关
    def start_engine(self):
        audio_id_str = self.audio_frame.get_audio_id()
        try:
            id = int(audio_id_str[:5])
            audio_loop = construct_audio_loop(id)
            if not audio_loop.next().is_valid() :
                self.textbox.console_log_error("该机经音频不存在")
                return
            self.engine = audio_loop.next()
            self.textbox.console_log("机经加载完毕")
        except FileNotFoundError:
            self.textbox.console_log_error("该机经音频不存在")
        except Exception as e:
            self.textbox.console_log_error("机经无法播放: {} --".format(repr(e)))

    def _play(self):
        if self.engine is None:
            self.textbox.console_log_error("未加载音频文件")
            return
    
        self.engine.play_audio()
        if self.engine.is_tail():
            self.textbox.console_log("播放结束, 点击'下一个'按钮重播")


    def _next(self):
        if self.engine is None:
            self.textbox.console_log_error("未加载音频文件")
            return
        self.engine = self.engine.next()
        self._console_log_next(self.engine.get_section_id())
        if self._auto_play_enabled:
            self._play()

    #endregion


    #region 设置面板相关函数
    def _on_click_auto_play(self):
        self._auto_play_enabled = not self._auto_play_enabled

    def _on_click_turbo(self):
        self._turbo_enabled = not self._turbo_enabled
    
    def _on_click_count_down(self):
        self._count_down_enabled = not self._count_down_enabled

    #endregion 
        

    #region GUI文字更新 + console输出相关函数

    def _console_log_next(self, sec_id: int):
        if sec_id == 0:
            self.textbox.console_log("当前对话: Briefing")
        else:
            self.textbox.console_log("当前对话: Dialogue: {}".format(sec_id))

    #endregion

    def run(self):
        self.mainloop()