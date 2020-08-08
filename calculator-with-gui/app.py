#! /usr/bin/python3

# Stevon Wright December 2019 GUI Calculator using tkinter
import tkinter as tk             # GUI library
try:
    from Libraries import NewWindow  # Necessary method: add_widgets
except ImportError:
    from .Libraries import NewWindow


class App(tk.Tk, NewWindow.NewWindow):
    ''' Main application window (the Root window) '''

    def __init__(self):
        tk.Tk.__init__(self)
        self.calculation = tk.StringVar()
        self.config_window()
        self.add_widgets()

    def start(self):
        ''' Starts the program '''
        self.mainloop()


if __name__ == "__main__":
    root = Main()
    root.start()
