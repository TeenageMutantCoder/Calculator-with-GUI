import tkinter as tk            # GUI library
from tkinter import filedialog  # File choosing capabilities
from .. import NewWindow        # Allows user to create multiple windows
import threading                # Allows completion of tasks simultaneously


class FileMenu(tk.Menu):
    ''' File submenu '''

    def __init__(self, parent):
        tk.Menu.__init__(self, parent)
        self.parent = parent
        self.window = self.parent.parent

        self.add_command(label="New Window", command=self.new_thread)
        self.add_command(label="Open", command=self.open_file)
        self.add_command(label="Quit", command=self.exit)

    def new_window(self):
        ''' Creates a new toplevel calculator window '''
        NewWindow.NewWindow(self.window)

    def new_thread(self, *args, **kwargs):
        ''' Creates a new thread, which allows for new windows and tasks '''
        newThread = threading.Thread(target=self.new_window, daemon=True)
        newThread.start()

    def open_file(self):
        filedialog.askopenfilename()

    def exit(self, *args, **kwargs):
        ''' Exits program '''
        # self.parent.quit()  # Doesnt end program. Only ends interactions.
        self.window.destroy()
