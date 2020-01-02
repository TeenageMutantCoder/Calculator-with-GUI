import tkinter as tk      # GUI library
from tkinter import font  # Allows for font changes


class Numbers(tk.Frame):
    ''' Frame with number buttons '''

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.window = self.parent
        self.font = font.Font(family="Times")

        numbers = [[7, 8, 9], [4, 5, 6], [1, 2, 3], [0, None, "."]]
        for row in numbers:
            for column in row:
                if column is None:
                    continue

                number = tk.Button(self, text=str(column))
                number.config(font=self.font)

                if column == 1:
                    number.config(command=lambda: self.insert("1"))
                elif column == 2:
                    number.config(command=lambda: self.insert("2"))
                elif column == 3:
                    number.config(command=lambda: self.insert("3"))
                elif column == 4:
                    number.config(command=lambda: self.insert("4"))
                elif column == 5:
                    number.config(command=lambda: self.insert("5"))
                elif column == 6:
                    number.config(command=lambda: self.insert("6"))
                elif column == 7:
                    number.config(command=lambda: self.insert("7"))
                elif column == 8:
                    number.config(command=lambda: self.insert("8"))
                elif column == 9:
                    number.config(command=lambda: self.insert("9"))
                elif column == 0:
                    number.config(command=lambda: self.insert("0"))
                    number.grid_configure(columnspan=2)
                elif column == ".":
                    number.config(command=lambda: self.insert("."))

                number.grid(column=row.index(column), row=numbers.index(row))
                number.grid_configure(sticky="NSEW")

                self.rowconfigure(numbers.index(row), weight=1)
                self.columnconfigure(row.index(column), weight=1)

    def insert(self, char):
        ''' Inserts a character into entry box '''
        if self.parent.calculation.get() == "Error":
            self.parent.calculation.set(char)
        else:
            self.parent.calculation.set(self.parent.calculation.get() + char)
        self.focus()

    def resize(self, event):
        ''' Changes the font size proportinal to the widget size '''
        self.update_idletasks()
        self.font = font.Font(size=self.winfo_height())
        self.update()
