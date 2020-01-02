from tkinter import *
import File_Browser_Main
import File_Browser_Function

def load_gui(self):
    #EntryBoxes
    self.txt_browse1 = Entry(self.master, text='', width=70)
    self.txt_browse1.grid(row=1, column=2, rowspan=2, columnspan=10, padx=(10, 20), pady=(25, 10), sticky=N + E + W)

    self.txt_browse2 = Entry(self.master, text='', width=70)
    self.txt_browse2.grid(row=2, column=2, rowspan=2, columnspan=10, padx=(10, 20), pady=(25, 10), sticky=N + E + W)

    #buttons
    self.btn_browse1 = Button(self.master, width=12, height=1, text="Browse...", command=lambda: File_Browser_Function.ask_direct(self))
    self.btn_browse1.grid(row=1, column=1, padx=(15, 0), pady=(25, 10), sticky=W)

    self.btn_browse2 = Button(self.master, width=12, height=1, text="Browse...")
    self.btn_browse2.grid(row=2, column=1, padx=(15, 0), pady=(25, 10), sticky=W)

    self.btn_CheckFiles = Button(self.master, width=12, height=2, text="check for files..")
    self.btn_CheckFiles.grid(row=3, column=1, padx=(15, 0), pady=(25, 10), sticky=W+S)

    self.btn_close = Button(self.master, width=12, height=2, text="Close", command=lambda: File_Browser_Function.ask_quit(self))
    self.btn_close.grid(row=3, column=10, padx=(15, 0), pady=(25, 10), sticky=E)


if __name__ == "__main__":
    pass
