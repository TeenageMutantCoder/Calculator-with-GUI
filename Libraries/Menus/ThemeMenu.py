import tkinter as tk


class ThemeMenu(tk.Menu):
    ''' Theme submenu. Submenu of Color Submenu '''

    # TODO: Add preset themes and a color chooser
    def __init__(self, parent):
        tk.Menu.__init__(self, parent)
        self.parent = parent
        self.window = self.parent.parent.parent.parent
        self.theme = "Default"

        self.add_command(label="Default", command=lambda: self.set_theme("Default"))
        self.add_command(label="Modern", command=lambda: self.set_theme("Modern"))
        self.add_command(label="Old-school", command=lambda: self.set_theme("Old-school"))

    def set_theme(self, theme):
        self.theme = theme
