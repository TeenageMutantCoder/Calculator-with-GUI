import tkinter as tk    # GUI Library
from . import FileMenu  # File submenu
from . import EditMenu  # Edit submenu
from . import ViewMenu  # View submenu
from . import HelpMenu  # Help Submenu


class Menubar(tk.Menu):
    ''' Menu for the program '''

    def __init__(self, parent):
        tk.Menu.__init__(self, parent)
        self.parent = parent
        self.window = self.parent

        self.filemenu = FileMenu.FileMenu(self)
        self.add_cascade(label="File", menu=self.filemenu)

        self.editmenu = EditMenu.EditMenu(self)
        self.add_cascade(label="Edit", menu=self.editmenu)

        self.viewmenu = ViewMenu.ViewMenu(self)
        self.add_cascade(label="View", menu=self.viewmenu)

        # Variables stored for later user customization of window
        self.color = self.viewmenu.color
        self.theme = self.viewmenu.theme

        self.helpmenu = HelpMenu.HelpMenu(self)
        self.add_cascade(label="Help", menu=self.helpmenu)
