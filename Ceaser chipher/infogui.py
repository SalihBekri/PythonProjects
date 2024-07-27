from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import alphabet

BACKGROUND_COLOR = "#001c30"
FONT = ("arial", 15, "normal")
FONT_COLOR = "white"


class InfoGui:
    def __init__(self):
        self.lang_name = ""
        self.shift_number = 0
        self.go_to_main = False
        # WINDOW
        self.win = Tk()
        self.win.title("Information Tab")
        icon_photo = PhotoImage(file="images/info.png")
        self.win.iconphoto(False, icon_photo)
        self.win.config(bg=BACKGROUND_COLOR, pady=50, padx=50)
        self.win.resizable(False, False)
        # LABELS
        self.lang_label = Label(text="Pick a language:", font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
        self.lang_label.grid(row=0, column=0)
        self.shift_label = Label(text="Pick a shift number:", font=FONT, fg=FONT_COLOR, bg=BACKGROUND_COLOR)
        self.shift_label.grid(row=1, column=0, pady=20)
        # COMBO BOX
        self.lang_combobox = Combobox(width=17)
        self.lang_combobox.grid(row=0, column=1)
        self.lang_combobox.config(values=alphabet.get_lang_names())
        # ENTRY
        self.shift_entry = Entry()
        self.shift_entry.grid(row=1, column=1, pady=20)
        # BUTTONS
        self.save_btn = Button(width=13, text="Save",
                               font=FONT,
                               fg="white",
                               bg=BACKGROUND_COLOR,
                               command=self.save_info)
        self.save_btn.grid(row=2, column=1)
        self.exit_button = Button(width=13, text="Exit",
                                  font=FONT,
                                  fg="white",
                                  bg=BACKGROUND_COLOR,
                                  command=self.exit_program)
        self.exit_button.grid(row=2, column=0)

        self.win.mainloop()

    def save_info(self):
        """first it checks if user hasn't filled all the entries and if he did it saves the info to be used by other
        classes."""
        self.shift_number = int(self.shift_entry.get().replace(" ", ""))
        self.lang_name = self.lang_combobox.get()
        response = self.check_entries(self.shift_number, self.lang_name)
        if response:
            self.go_to_main = True
            self.win.destroy()

    def check_entries(self, shift_number, lang_name) -> bool:
        try:
            shift_number = int(shift_number)
        except ValueError:
            messagebox.showwarning(title="Error", message="Please enter a valid shift number")
        else:
            if lang_name == "" or lang_name not in alphabet.get_lang_names():
                messagebox.showwarning(title="Empty Entry!", message="Please fill all entries")
            else:
                response = messagebox.askokcancel(title="Confirmation Window",
                                                  message=f"The language you picked is: {lang_name}\nThe shift number is: {shift_number}")
                if response:
                    return True

    def exit_program(self):
        """It shuts down the program"""
        self.win.destroy()
