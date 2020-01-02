import os
from tkinter import *
import tkinter as tk
import sqlite3
from tkinter import messagebox
from tkinter.filedialog import askdirectory

import File_Browser_GUI
import File_Browser_Main


def center_window(self, w, h):
    # pass in the Tkinter main frame
    # get users height and width
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    x = int((screen_width / 2) - (w / 2))
    y = int((screen_height / 2) - (h / 2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo


def ask_quit(self):
    if messagebox.askokcancel("Exit Program", "Okay to exit Application?"):
        # this closes app
        self.master.destroy()
        os._exit(0)


def ask_direct(self, e = None):
    askdirectory()