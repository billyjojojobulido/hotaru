import customtkinter


class Console(customtkinter.CTkTextbox):

    def __init__(self, root: customtkinter.CTk):
        super().__init__(root)