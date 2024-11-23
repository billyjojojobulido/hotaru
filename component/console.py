import customtkinter
import time


class Console(customtkinter.CTkTextbox):

    def __init__(self, root: customtkinter.CTk):
        super().__init__(root)


    def console_log(self, info_type: str, msg: str):
        if not msg or len(msg) == 0:
            return
        super().insert('end', "\n%s [%s] %s" % (time.strftime('%Y-%m-%d %H:%M:%S'), info_type, msg))
        super().update()


    def console_log_error(self, err: str):
        if not err or len(err) == 0:
            return
        super().configure(text_color="red")
        super().insert('end', "\n%s [%s] %s" % (time.strftime('%Y-%m-%d %H:%M:%S'), "ERROR", err))
        super().update()