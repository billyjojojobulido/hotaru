import customtkinter
from audio_manager import get_config_file

FONT_TITLE = ("Helvetica", 16, "bold")

class AudioPanel(customtkinter.CTkFrame):
            
    def __init__(self, root: customtkinter.CTk, start_engine):
        super().__init__(root)

        self.label_audio_group = customtkinter.CTkLabel(master=self, text="音频控制台", font=FONT_TITLE)
        self.label_audio_group.grid(row=0, column=0, padx=10, pady=5)

        customtkinter.CTkLabel(self, text="请选择机经序号" ).grid(row=1, column=0, padx=20)

        self.combobox_1 = self._init_audio_option_menu()
        self.combobox_1.grid(row=2, column=0, padx=20, pady=(5, 5))

        self.string_input_button = customtkinter.CTkButton(self, text="选择",
                                                           command=start_engine)
        self.string_input_button.grid(row=3, column=0, padx=20, pady=(10, 10))


        self.audio_indicator = customtkinter.CTkLabel(self, text="-- 未选择音频 --")
        self.audio_indicator.grid(row=4, column=0, padx=20, pady=(10, 10))

        self.space_holder_1 =  customtkinter.CTkLabel(self, text=" ")
        self.space_holder_1.grid(row=5, column=0, padx=20, pady=(10, 10))

    
    #region 初始化GUI相关
    def _init_audio_option_menu(self):
        config_data = get_config_file()
        options = [str(x["id"]) + " " + x["file_name"] for x in config_data] if config_data else []
        combobox = customtkinter.CTkOptionMenu(self, dynamic_resizing=False, 
                                           values=options)
        if options is not None and len(options) > 0:
            combobox.set(options[0])
        else:
            combobox.set("-- Empty --")
        return combobox
    #endregion