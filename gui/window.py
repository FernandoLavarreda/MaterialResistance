# Fernando Lavarreda
# GUI to control the program

import tkinter as tk
import tkinter.ttk as ttk

class Main(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title = "Beam Selector FerLavarreda"
        self.geometry("400x200+100+100")
        self.resizable(False, False)
        self.iconbitmap(default="pass")
        
