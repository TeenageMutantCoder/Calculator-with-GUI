import tkinter as tk      # GUI library
from tkinter import font  # Allows for font changes


class Entry(tk.Frame):
    ''' Entry box in calculator. Displays calculation. '''

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.window = self.parent
        self.font = font.Font(family="Times", weight="bold")

        self.entry = tk.Entry(self, textvariable=self.parent.calculation)
        self.entry.config(justify="right")
        self.entry.grid(column=0, row=0, columnspan=5, sticky="NSEW")
        self.entry.config(font=self.font)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

    def calculate(self, *args, **kwargs):
        ''' Calculates what was in the entry box '''
        try:
            self.parent.calculation.set(eval(self.parent.calculation.get()))
        except ZeroDivisionError:
            self.parent.calculation.set("Error")
        except SyntaxError:
            self.parent.calculation.set("Error")
        except NameError:
            self.parent.calculation.set("Error")

    def insert(self, char):
        ''' Inserts a character into entry box '''
        if self.parent.calculation.get() == "Error":
            self.parent.calculation.set(char)
        else:
            self.parent.calculation.set(self.parent.calculation.get() + char)

    def delete(self, *args, **kwargs):
        ''' Deletes a character from entry box '''
        if self.parent.calculation.get() == "Error":
            self.parent.calculation.set("")
        else:
            output = self.parent.calculation.get()
            self.parent.calculation.set(output[:-1])

    def clear(self, *args, **kwargs):
        ''' Clears entry box '''
        self.parent.calculation.set("")

    def resize(self, event):
        ''' Changes the font size proportinal to the widget size '''
        self.update_idletasks()
        self.font = font.Font(size=self.winfo_height())
        self.update()
