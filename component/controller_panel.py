import customtkinter

FONT_TITLE = ("Helvetica", 16, "bold")

class ControllerPanel(customtkinter.CTkFrame):
            
    def __init__(self, root: customtkinter.CTk, play_event, next_event):
        super().__init__(root)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_rowconfigure(2, weight=1)

        customtkinter.CTkLabel(self, text=" ").grid(row=0, column=0)

        self.count_down_bar = customtkinter.CTkProgressBar(self)
        self.count_down_bar.grid(row=1, column=1, columnspan=3,padx=(40, 40), pady=(10, 10), sticky="ew")


        self.play_button = customtkinter.CTkButton(self, text="播放",
                                                           command=play_event)
        self.play_button.grid(row=2, column=1, padx=(20, 10),pady=(10, 10))

        self.next_button = customtkinter.CTkButton(self, text="下一个",
                                                           command=next_event)
        self.next_button.grid(row=2, column=2, padx=(10, 20), pady=(10, 10))