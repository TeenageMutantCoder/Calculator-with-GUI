import tkinter as tk              # GUI Library
from tkinter import colorchooser  # Color choosing capabilities
from . import ThemeMenu           # Theme submenu


class ColorMenu(tk.Menu):
    ''' Color submenu. Submenu of View submenu '''

    def __init__(self, parent):
        tk.Menu.__init__(self, parent)
        self.parent = parent
        self.window = self.parent.parent.parent
        self.color = None

        thememenu = ThemeMenu.ThemeMenu(self)
        self.add_cascade(label="Choose theme", menu=thememenu)
        self.theme = thememenu.theme

        self.add_command(label="Set colors", command=self.choose_color)

    def choose_color(self):
        self.color = colorchooser.askcolor(initialcolor=self.color)
