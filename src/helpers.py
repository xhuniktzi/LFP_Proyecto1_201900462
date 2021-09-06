from tkinter import Tk


def define_geometry(master: Tk, width: int, height: int) -> str:
    x_win = master.winfo_screenwidth() // 2 - width // 2
    y_win = master.winfo_screenheight() // 2 - height // 2
    data_geometry = '{}x{}+{}+{}'.format(width, height, x_win, y_win)
    return data_geometry
