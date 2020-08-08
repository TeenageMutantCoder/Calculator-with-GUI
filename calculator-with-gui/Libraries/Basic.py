import tkinter as tk      # GUI library
from tkinter import font  # Allows for font changes


class Basic(tk.Frame):
    ''' Basic calculator configuration: simple symbols and math operators '''

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.window = self.parent
        self.font = font.Font(family="Times")

        symbols = [["del", "clear"], ["+", "-"], ["*", "/"], ["(", ")"], ["="]]
        for row in symbols:
            for column in row:
                symbol = tk.Button(self, text=str(column))
                symbol.config(font=self.font)

                if column == "del":
                    symbol.config(command=lambda: self.delete())
                elif column == "clear":
                    symbol.config(command=lambda: self.clear())
                elif column == "+":
                    symbol.config(command=lambda: self.insert("+"))
                elif column == "-":
                    symbol.config(command=lambda: self.insert("-"))
                elif column == "*":
                    symbol.config(command=lambda: self.insert("*"))
                elif column == "/":
                    symbol.config(command=lambda: self.insert("/"))
                elif column == "(":
                    symbol.config(command=lambda: self.insert("("))
                elif column == ")":
                    symbol.config(command=lambda: self.insert(")"))
                elif column == "=":
                    symbol.config(command=lambda: self.calculate())
                    symbol.grid_configure(columnspan=2)

                symbol.grid(column=row.index(column), row=symbols.index(row))
                symbol.grid_configure(sticky="NSEW")
                self.rowconfigure(symbols.index(row), weight=1)
                self.columnconfigure(row.index(column), weight=1)

    def calculate(self, *args):
        ''' Calculates what was in the entry box '''
        try:
            self.parent.calculation.set(eval(self.parent.calculation.get()))
        except ZeroDivisionError:
            self.parent.calculation.set("Error")
        except SyntaxError:
            self.parent.calculation.set("Error")

    def insert(self, char):
        ''' Inserts a character into entry box '''
        if self.parent.calculation.get() == "Error":
            self.parent.calculation.set(char)
        else:
            self.parent.calculation.set(self.parent.calculation.get() + char)
        self.focus()

    def clear(self):
        self.parent.calculation.set("")

    def delete(self):
        ''' Deletes a character from entry box '''
        if self.parent.calculation.get() == "Error":
            self.parent.calculation.set("")
        else:
            output = self.parent.calculation.get()
            self.parent.calculation.set(output[:-1])

    def resize(self, event):
        ''' Changes the font size proportinal to the widget size '''
        self.update_idletasks()
        self.font = font.Font(size=self.winfo_height())
        self.update()