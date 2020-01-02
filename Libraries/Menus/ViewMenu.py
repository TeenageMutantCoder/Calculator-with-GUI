import tkinter as tk     # GUI Library
from . import ModeMenu   # Mode submenu
from . import ColorMenu  # Color submenu


class ViewMenu(tk.Menu):
    ''' View submenu '''

    def __init__(self, parent):
        tk.Menu.__init__(self, parent)
        self.parent = parent
        self.window = self.parent.parent

        modemenu = ModeMenu.ModeMenu(self)
        self.add_cascade(label="Set mode", menu=modemenu)

        colormenu = ColorMenu.ColorMenu(self)
        self.add_cascade(label="Set color", menu=colormenu)
        self.color = colormenu.color
        self.theme = colormenu.theme
