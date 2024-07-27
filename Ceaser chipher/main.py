from infogui import InfoGui
from mainGui import MainGui

info_window = InfoGui()
if info_window.go_to_main:
    MainGui(info_window.shift_number, info_window.lang_name)

