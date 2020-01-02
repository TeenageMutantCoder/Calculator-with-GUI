import tkinter as tk            # GUI Library
from tkinter import messagebox  # Allows a messagebox to be displayed on screen


class HelpMenu(tk.Menu):
    ''' Help submenu '''

    def __init__(self, parent):
        tk.Menu.__init__(self, parent)
        self.parent = parent
        self.window = self.parent.parent

        # TODO: Add help option windows
        self.add_command(label="About", command=self.about)
        self.add_command(label="How to Use", command=self.how_to_use)

    def about(self):
        message1 = "Created by Stevon Wright in December 2019. "
        message2 = "This was a project to learn tkinter and GUI, "
        message3 = "which I thought would help me improve in "
        message4 = "Python and programming in general."

        message = message1 + message2 + message3 + message4
        messagebox.showinfo(message=message, title="About", parent=self.window)

    def how_to_use(self):
        pass
