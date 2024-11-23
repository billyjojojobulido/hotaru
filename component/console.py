import customtkinter
import time

FONT=("微软雅黑", 11)

class Console(customtkinter.CTkTextbox):

    def __init__(self, root: customtkinter.CTk):
        super().__init__(root, font=FONT)


    def console_log(self,  msg: str, info_type="INFO"):
        if not msg or len(msg) == 0:
            return
        super().insert('end', "\n%s [%s] %s" % (time.strftime('%Y-%m-%d %H:%M:%S'), info_type, msg))
        super().update()


    def console_log_error(self, err: str):
        if not err or len(err) == 0:
            return
        super().configure(text_color="red")
        super().insert('end', "\n%s [%s] %s" % (time.strftime('%Y-%m-%d %H:%M:%S'), err, "ERROR"))
        super().update()