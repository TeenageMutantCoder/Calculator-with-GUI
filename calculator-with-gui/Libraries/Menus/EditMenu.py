import tkinter as tk


class EditMenu(tk.Menu):
    ''' Edit Submenu '''

    def __init__(self, parent):
        tk.Menu.__init__(self, parent)
        self.parent = parent
        self.window = self.parent.parent

        # TODO: Add insert command that adds symbols and stuff
        self.add_command(label="Copy", command=self.copy)
        self.add_command(label="Cut", command=self.cut)
        self.add_command(label="Paste", command=self.paste)

        self.add_separator()

        self.add_command(label="Clear All", command=self.clear)
        self.add_command(label="Insert...", command=self.insert_special)

    def copy(self, *args, **kwargs):
        ''' Copies contents of entry box into clipboard '''
        self.window.clipboard_clear()
        self.window.clipboard_append(self.window.calculation.get())

    def cut(self, *args, **kwargs):
        ''' Copies entry box into clipboard then clears the entrybox '''
        self.window.clipboard_clear()
        self.window.clipboard_append(self.window.calculation.get())
        self.clear()

    def paste(self, *args, **kwargs):
        ''' Pastes contents of clipboard into entry box '''
        current = self.window.calculation.get()
        self.window.calculation.set(current + self.window.clipboard_get())

    def clear(self):
        ''' Clears entry box '''
        self.window.calculation.set("")

    def insert_special(self):
        pass
