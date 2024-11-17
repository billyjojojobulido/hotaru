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
        self.title("CustomTkinter complex_example.py")
        self.geometry(f"{800}x{640}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure((1), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self)
        self.textbox.grid(row=0, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")

        # create tabview
        self.audio_frame = customtkinter.CTkScrollableFrame(self, label_text="音频控制台", width=250)
        self.audio_frame.grid(row=0, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.audio_frame.grid_columnconfigure(0, weight=1)  # configure grid of individual tabs

        # 选择音频菜单
        customtkinter.CTkLabel(self.audio_frame, text="请选择机经序号").grid(row=0, column=0, padx=20, pady=(10, 10))

        self.combobox_1 = self._init_audio_option_menu()
        self.combobox_1.grid(row=1, column=0, padx=20, pady=(5, 5))

        self.string_input_button = customtkinter.CTkButton(self.audio_frame, text="选择",
                                                           command=self.start_engine)
        self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))


        self.audio_indicator = customtkinter.CTkLabel(self.audio_frame, text="未选择音频")
        self.audio_indicator.grid(row=3, column=0, padx=20, pady=(10, 10))

        self.play_button = customtkinter.CTkButton(self.audio_frame, text="播放",
                                                           command=self._play)
        self.play_button.grid(row=4, column=0, padx=20, pady=(10, 10))

        self.next_button = customtkinter.CTkButton(self.audio_frame, text="下一个",
                                                           command=self._next)
        self.next_button.grid(row=5, column=0, padx=20, pady=(10, 10))

        # create slider and progressbar frame
        self.slider_progressbar_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.slider_progressbar_frame.grid(row=1, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(4, weight=1)
        self.seg_button_1 = customtkinter.CTkSegmentedButton(self.slider_progressbar_frame)
        self.seg_button_1.grid(row=0, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        self.progressbar_2 = customtkinter.CTkProgressBar(self.slider_progressbar_frame)
        self.progressbar_2.grid(row=2, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        self.slider_2 = customtkinter.CTkSlider(self.slider_progressbar_frame, orientation="vertical")
        self.slider_2.grid(row=0, column=0, rowspan=5, padx=(10, 10), pady=(10, 10), sticky="ns")
        self.progressbar_3 = customtkinter.CTkProgressBar(self.slider_progressbar_frame, orientation="vertical")
        self.progressbar_3.grid(row=0, column=1, rowspan=5, padx=(10, 20), pady=(10, 10), sticky="ns")

        # create scrollable frame
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self, label_text="CTkScrollableFrame")
        self.scrollable_frame.grid(row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        self.scrollable_frame_switches = []
        for i in range(5):
            switch = customtkinter.CTkSwitch(master=self.scrollable_frame, text=f"CTkSwitch {i}")
            switch.grid(row=i, column=0, padx=10, pady=(0, 20))
            self.scrollable_frame_switches.append(switch)

        # create checkbox and switch frame

        # set default values
        self.scrollable_frame_switches[0].select()
        self.scrollable_frame_switches[4].select()
        # self.optionmenu_1.set("CTkOptionmenu")
        self.slider_2.configure(command=self.progressbar_3.set)
        self.textbox.insert("0.0", "CTkTextbox\n\n" + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.\n\n" * 20)
        self.seg_button_1.configure(values=["CTkSegmentedButton", "Value 2", "Value 3"])
        self.seg_button_1.set("Value 2")


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
        self.engine.play_audio()

    def _next(self):
        if self.engine is None:
            self._audio_indicate_user("-- 还没加载音频文件 --")
            return
        print("播放下一个")
        self.engine = self.engine.next()

    # 用来更新 "音频控制面板" 的提示文字
    def _audio_indicate_user(self, txt: str):
        self.audio_indicator.configure(text=txt)

    # @deprecated
    @DeprecationWarning
    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())


    def run(self):
        self.mainloop()