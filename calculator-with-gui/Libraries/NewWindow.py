import tkinter as tk      # GUI Library
import os
from PIL import ImageTk   # Allows for window icon
from PIL import Image     # Allows for window icon
from .Menus import Menu   # Program menu
from . import Entry       # Calculation entry box
from . import Numbers     # Number buttons
from . import Basic       # Basic calculator config
# from . import Scientific  # Scientific calculator config


class NewWindow(tk.Toplevel):
    ''' A new calculator GUI window '''

    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.parent = parent
        self.calculation = tk.StringVar()
        self.calculation.trace("w", self.remove_alpha)

        self.config_window()
        self.add_widgets()

    def config_window(self):
        ''' Set beginning window configurations '''
        self.title("Calculator GUI with OOP")
        self.geometry("500x300+300+300")
        self.minsize(200, 200)

        # Add program icon in top left corner
        image_path = os.path.relpath(os.path.join("calculator-with-gui", "Libraries", "Assets", "calculator2.png"))
        image = ImageTk.PhotoImage(Image.open(image_path))
        self.iconphoto(False, image)

    def add_widgets(self, symbols="Basic"):
        ''' Adds and places the widgets into the program window '''
        # Add menu
        self.option_add('*tearOff', tk.FALSE)
        self.menu = Menu.Menubar(self)
        self.config(menu=self.menu)

        self.bind("<Control-n>", self.menu.filemenu.new_thread)
        self.bind("<Control-q>", self.menu.filemenu.exit)
        self.bind("<Control-c>", self.menu.editmenu.copy)
        self.bind("<Control-x>", self.menu.editmenu.cut)
        self.bind("<Control-v>", self.menu.editmenu.paste)

        # Initialize and add entry box
        self.entry = Entry.Entry(self)
        self.entry.grid(column=0, row=0, columnspan=5, sticky="NSEW")
        self.entry.height = self.entry.winfo_height()
        self.entry.bind("<Configure>", self.entry.resize)

        self.bind("<Return>", lambda key: self.handle_key(key.char))
        self.bind("<BackSpace>", lambda key: self.handle_key(key.char))
        self.bind("<Control-BackSpace>", self.entry.clear)

        numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        symbols = ["+", "-", "*", "/", "(", ")"]
        keypad = ["Add", "Subtract", "Multiply", "Divide", "Equal", "Decimal"]
        keypad.append("Enter")
        chars = numbers + symbols
        keypad_keys = numbers + keypad
        for char in chars:
            self.bind(char, lambda char: self.handle_key(char.char))
        for key in keypad_keys:
            self.bind("<Key-KP_" + key + ">", lambda key: self.handle_key(key.char))

        self.bind("<Key>", lambda key: self.remove_alpha(key.char))

        # Initialize and add number buttons
        self.numbers = Numbers.Numbers(self)
        self.numbers.grid(column=0, row=1, rowspan=4, columnspan=3)
        self.numbers.grid_configure(sticky="NSEW")
        self.numbers.bind("<Configure>", self.numbers.resize)

        # Initialize and add basic symbols
        self.symbols = Basic.Basic(self)
        self.symbols.grid(column=3, row=1, rowspan=4, sticky="NSEW")
        self.symbols.bind("<Configure>", self.symbols.resize)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=3)
        self.columnconfigure(0, weight=2)
        self.columnconfigure(3, weight=1)

    def handle_key(self, key):
        if key == "=" or key == "\r":    # Enter key
            self.entry.calculate()

        elif str(self.focus_get()) != ".!entry.!entry":
            if key == "\x08":            # Backspace key
                self.entry.delete()
            elif key == "=" or key == "\r":    # Enter key
                self.entry.calculate()
            else:
                self.entry.insert(key)

        else:
            current = self.calculation.get() + key
            if "".join(current.split(key)) == "".join("Error".split(key)):
                self.calculation.set("")
                self.entry.insert(key)

    def remove_alpha(self, char):
        if char.isalpha():
            current = self.calculation.get()
            self.calculation.set(current.replace(char, ""))
