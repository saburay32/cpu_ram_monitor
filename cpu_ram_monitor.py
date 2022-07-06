import tkinter as tk
from tkinter import ttk
import sys




class Application(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.attributes('-alpha', 0.75)
        self.attributes('-topmost', True)
        self.overrideredirect(True)
        self.resizable(False,False)
        self.title('CPU-RAM monitor bar')

        self.set_ui()

    def set_ui(self):
        exit_but = ttk.Button(self, text='Exit', command = self.app_exit)
        exit_but.pack(fill=tk.X)

        self.bar2 = ttk.LabelFrame(self, text='Manual')
        self.bar2.pack(fill=tk.X)

        ttk.Button(self.bar2, text='move').pack(side=tk.LEFT)

    def app_exit(self):
        self.destroy()
        sys.exit()
        
''''''