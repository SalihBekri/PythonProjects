from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from AlgorithBrain import encode, decode
from alphabet import get_lang_info
from ConnectingToMedia import via_email


INFO_FONT = ("courier", 13, "italic")
FONT = ("arial", 12, "bold")
BACKGROUND_COLOR_2 = "#3d3c99"
FONT_COLOR = "#17b286"


class MainGui:
    def __init__(self, shift_num, lang_name):
        self.shift_num = shift_num
        self.lang_name = lang_name
        # Window
        self.main_win = Tk()
        self.main_win.title("Ceaser Cipher")
        self.main_win.config(bg=BACKGROUND_COLOR_2, pady=20, padx=20)
        self.main_win.resizable(False, False)
        main_icon = PhotoImage(file="images/ceaser.png")
        self.main_win.iconphoto(False, main_icon)
        # LABELS
        self.label_1 = Label(text="Enter your message here:", bg=BACKGROUND_COLOR_2, font=FONT, fg=FONT_COLOR)
        self.label_1.grid(row=0, column=0)
        self.label_2 = Label(text="Via:", bg=BACKGROUND_COLOR_2, font=FONT, fg=FONT_COLOR)
        self.label_2.grid(row=2, column=0)
        self.label_2.grid_remove()
        self.label_3 = Label(text=f"{lang_name} \u005c {shift_num}", bg=BACKGROUND_COLOR_2, font=INFO_FONT, fg="white")
        self.label_3.place(x=0, y=0)
        self.label_4 = Label(text=f"Enter your media info here:", bg=BACKGROUND_COLOR_2, font=FONT, fg=FONT_COLOR)
        self.label_4.grid(row=3, column=0)
        self.label_4.grid_remove()
        # Combobox
        self.media_box = Combobox(width=17)
        self.media_box.grid(row=2, column=1)
        self.media_box.config(values=["Email", "SMS", "Telegram"])
        self.media_box.grid_remove()
        # Entry
        self.entry_1 = Entry(width=30)
        self.entry_1.grid(row=3, column=1)
        self.entry_1.grid_remove()

        # TEXT
        self.message_text = Text(width=25, height=15)
        self.message_text.grid(row=0, column=1, pady=20, padx=20)
        self.result_text = Text(width=25, height=15)
        self.result_text.grid(row=0, column=5, pady=20, padx=20)
        # RADIO BUTTONS
        self.selection_var = StringVar()
        self.selection_var.set("")
        self.encode = Radiobutton(text="Encode",
                                  bg=BACKGROUND_COLOR_2,
                                  font=INFO_FONT,
                                  value="encode",
                                  variable=self.selection_var,
                                  command=self.activate_btn,
                                  tristatevalue=0

                                  )
        self.encode.grid(row=0, column=2)
        self.decode = Radiobutton(text="Decode",
                                  bg=BACKGROUND_COLOR_2,
                                  font=INFO_FONT,
                                  value="decode",
                                  variable=self.selection_var,
                                  command=self.activate_btn,
                                  tristatevalue=0
                                  )
        self.decode.grid(row=0, column=3)
        # BUTTONS
        self.btn_1 = Button(text="GO",
                            bg=BACKGROUND_COLOR_2,
                            font=FONT,
                            fg=FONT_COLOR,
                            bd=1,
                            width=20,
                            state="disabled",
                            command=self.print_value)
        self.btn_1.grid(row=0, column=4)
        self.btn_2 = Button(text="Would you like to send your message?",
                            bg=BACKGROUND_COLOR_2,
                            fg=FONT_COLOR,
                            font=FONT,
                            command=self.activate_email)
        self.btn_2.grid(row=1, column=0, pady=20)
        self.btn_2.grid_remove()
        self.btn_3 = Button(text="Send",
                            bg=BACKGROUND_COLOR_2,
                            fg=FONT_COLOR,
                            font=FONT,
                            width=20,
                            command=self.send_email)
        self.btn_3.grid(row=4, column=0, columnspan=2)
        self.btn_3.grid_remove()

        self.main_win.mainloop()

    def print_value(self):
        """It takes the text inside the message_text widget
         and pass it to algorithm brain if it was filtered properly"""
        if self.message_text.get(1.0, END).replace(" ", "").replace("\n", "") != "":
            if self.selection_var.get() == "encode":
                encoded = encode(self.shift_num,
                                 self.message_text.get(1.0, END).replace("\n", ""),
                                 get_lang_info(self.lang_name))
                self.result_text.delete(1.0, END)
                self.result_text.insert(1.0, encoded)
            else:
                decoded = decode(self.shift_num,
                                 self.message_text.get(1.0, END).replace("\n", ""),
                                 get_lang_info(self.lang_name))
                self.result_text.delete(1.0, END)
                self.result_text.insert(1.0, decoded)
            self.btn_2.grid()

        else:
            messagebox.showwarning(title="Error", message="Please insert a message!")

    def activate_btn(self):
        self.btn_1.config(state="normal")

    def activate_email(self):
        self.label_4.grid()
        self.media_box.grid()
        self.label_2.grid()
        self.entry_1.grid()
        self.btn_3.grid()

    def send_email(self):
        via_email(self.result_text.get(1.0, END), self.entry_1.get())

