import tkinter
import tkinter.messagebox
import customtkinter
from audio_manager.utils import get_config_file, construct_audio_loop, _test_audio_loop

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        ################
        ### 服务端部分 ###
        ################
        self.engine = None

        ################
        ### UI部分 ###
        ################
        # configure window
        self.title("Hotaru - v1.0.1")
        # self.geometry(f"{800}x{640}")

        self.geometry(f"{640}x{480}")

        self.textbox_index = 0

        # configure grid layout (4x4)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        # self.grid_rowconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure(0, weight=1)
        # self.grid_rowconfigure(1, weight=0)

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self)
        self.textbox.grid(row=0, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")

        # create tabview
        self.audio_frame = customtkinter.CTkScrollableFrame(self, label_text="音频控制台", width=250)
        self.audio_frame.grid(row=0, column=1, rowspan=2, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.audio_frame.grid_columnconfigure(0, weight=1)  # configure grid of individual tabs

        # 选择音频菜单
        customtkinter.CTkLabel(self.audio_frame, text="请选择机经序号").grid(row=0, column=0, padx=20, pady=(10, 10))

        self.combobox_1 = self._init_audio_option_menu()
        self.combobox_1.grid(row=1, column=0, padx=20, pady=(5, 5))

        self.string_input_button = customtkinter.CTkButton(self.audio_frame, text="选择",
                                                           command=self.start_engine)
        self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))


        self.audio_indicator = customtkinter.CTkLabel(self.audio_frame, text="-- 未选择音频 --")
        self.audio_indicator.grid(row=3, column=0, padx=20, pady=(10, 10))

        self.space_holder_1 =  customtkinter.CTkLabel(self.audio_frame, text=" ")
        self.space_holder_1.grid(row=4, column=0, padx=20, pady=(10, 10))


        self.play_button = customtkinter.CTkButton(self.audio_frame, text="播放",
                                                           command=self._play)
        self.play_button.grid(row=5, column=0, padx=20, pady=(10, 10))

        self.next_button = customtkinter.CTkButton(self.audio_frame, text="下一个",
                                                           command=self._next)
        self.next_button.grid(row=6, column=0, padx=20, pady=(10, 5))

        # create slider and progressbar frame
        self.slider_progressbar_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.slider_progressbar_frame.grid(row=1, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(4, weight=1)
        self.progressbar_2 = customtkinter.CTkProgressBar(self.slider_progressbar_frame)
        self.progressbar_2.grid(row=2, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")

        # create scrollable frame
        # self.scrollable_frame = customtkinter.CTkScrollableFrame(self, label_text="CTkScrollableFrame")
        # self.scrollable_frame.grid(row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        # self.scrollable_frame.grid_columnconfigure(0, weight=1)
        # self.scrollable_frame_switches = []
        # for i in range(5):
        #     switch = customtkinter.CTkSwitch(master=self.scrollable_frame, text=f"CTkSwitch {i}")
        #     switch.grid(row=i, column=0, padx=10, pady=(0, 20))
        #     self.scrollable_frame_switches.append(switch)

        # create checkbox and switch frame

        # set default values
        # self.scrollable_frame_switches[0].select()
        # self.scrollable_frame_switches[4].select()
        # self.optionmenu_1.set("CTkOptionmenu")
        # self.textbox.insert("0.0", "")


    def _init_audio_option_menu(self):
        config_data = get_config_file()
        options = [str(x["id"]) + " " + x["file_name"] for x in config_data] if config_data else []
        combobox = customtkinter.CTkOptionMenu(self.audio_frame, dynamic_resizing=False, 
                                           values=options, width=200)
        if options is not None and len(options) > 0:
            combobox.set(options[0])
        else:
            combobox.set("-- Empty --")
        return combobox

    def start_engine(self):
        audio_id_str = self.combobox_1.get()
        try:
            id = int(audio_id_str[:5])
            _test_audio_loop(id)
            audio_loop = construct_audio_loop(id)
            if audio_loop is None or audio_loop.next is None:
                print("A")
                self._audio_indicate_user("-- 该机经音频不存在 --")
                return
            self.engine = audio_loop.next()
            self._audio_indicate_user("-- 机经加载完毕 --")
        except FileNotFoundError:
            self._audio_indicate_user("-- 该机经音频不存在 --")
        except Exception as e:
            self._audio_indicate_user("-- 机经无法播放: {} --".format(repr(e)))
            

    def _play(self):
        if self.engine is None:
            self._audio_indicate_user("-- 还没加载音频文件 --")
            return
    
        # if self.engine.get_section_id() == 0:
        #     self._textbox_add(">> 开始播放 Briefing\n")
        # else:
        #     self._textbox_add(">> 开始播放 Dialogue: {}\n".format(self.engine.get_section_id()))
        
        self.engine.play_audio()
        if self.engine.is_tail():
            self._textbox_add(">> 播放结束, 点击'下一个'按钮重播\n")

    def _next(self):
        if self.engine is None:
            self._audio_indicate_user("-- 还没加载音频文件 --")
            return
        self.engine = self.engine.next()
        self._console_log_next(self.engine.get_section_id())
        
    def _console_log_next(self, sec_id: int):
        if sec_id == 0:
            self._textbox_add(">> 当前对话: Briefing\n")
        else:
            self._textbox_add(">> 当前对话: Dialogue: {}\n".format(sec_id))

    # 用来更新 "音频控制面板" 的提示文字
    def _audio_indicate_user(self, txt: str):
        self.audio_indicator.configure(text=txt)


    def _textbox_add(self, txt:str):
        self.textbox.insert("0.0", txt)
        self.textbox_index += 1

    # @deprecated
    @DeprecationWarning
    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())


    def run(self):
        self.mainloop()