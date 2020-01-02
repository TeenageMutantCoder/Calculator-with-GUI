import tkinter as tk       # GUI library
# from .. import Basic       # Allows user to set symbols layout to basic
# from .. import Scientific  # Allows user to set symbols layout to advanced


class ModeMenu(tk.Menu):
    ''' Mode submenu. Submenu of View submenu '''

    def __init__(self, parent):
        tk.Menu.__init__(self, parent)
        self.parent = parent
        self.window = self.parent.parent.parent

        # TODO: Add mode-change and layout-change methods
        self.layout = tk.IntVar()
        self.layout.set(0)
        self.add_radiobutton(label="Basic", variable=self.layout, value=0, command=self.set_basic)
        self.add_radiobutton(label="Scientific", variable=self.layout, value=1, command=self.set_scientific)

        self.add_separator()

        self.mode = tk.IntVar()
        self.mode.set(0)
        self.add_radiobutton(label="Degrees", variable=self.mode, value=0)
        self.add_radiobutton(label="Radians", variable=self.mode, value=1)

    def set_basic(self):
        pass

    def set_scientific(self):
        pass
