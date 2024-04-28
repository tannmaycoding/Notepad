"""
This is a Notepad Using Tkinter.
Here, you can write text, open files, save files, make new files.

Modules Used:
    os.path,
    everything from tkinter,
    showinfo from tkinter.messagebox,
    askopenfilename, asksavefilename from tkinter.filedialog

Functions made:
    save: for saving files,
    new: for making new files,
    opening: for opening files,
    quitApp: for quitting the app,
    cut: for cutting selected text,
    copy: for copying selected text,
    paste: for pasting selected text,
    about: for opening about page
"""

import os.path
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename

root = Tk()
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.geometry("644x444")
root.title("Notepad")


def save():
    global file
    if file is None:
        file = asksaveasfilename(initialfile='Untitled.txt',
                                 defaultextension=".txt",
                                 filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

        if file == "":
            file = NONE

        else:
            with open(file, "w") as f:
                f.write(text.get(1.0, END))

            root.title(os.path.basename(file) + " - Notepad")

    else:
        with open(file, "w") as f:
            f.write(text.get(1.0, END))


def new():
    global file
    root.title("Untitled - Notepad")
    file = None
    text.delete(1.0, END)


def opening():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file == "":
        file = None

    else:
        root.title(os.path.basename(file) + " - Notepad")
        text.delete(1.0, END)
        with open(file, "r") as f:
            text.insert(1.0, f.read())


def quitApp():
    root.destroy()


def cut():
    text.event_generate("<<Cut>>")


def copy():
    text.event_generate("<<Copy>>")


def pasteText():
    text.event_generate("<<Paste>>")


def about():
    showinfo("Notepad", "Notepad By Tannmay")


text = Text(font="arial 14 normal", borderwidth=5)
file = None
text.grid(sticky=N + S + E + W)
scrollBarY = Scrollbar(text)
scrollBarY.pack(side=RIGHT, fill=Y)
scrollBarY.config(command=text.yview)
text.config(yscrollcommand=scrollBarY.set)

menu = Menu()
m1 = Menu(menu, tearoff=0)
m1.add_command(label="New", command=new)
m1.add_command(label="Save", command=save)
m1.add_command(label="Open", command=opening)
menu.add_separator()
m1.add_command(label="Exit", command=quitApp)

m2 = Menu(menu, tearoff=0)
m2.add_command(label="Cut", command=cut)
m2.add_command(label="Copy", command=copy)
m2.add_command(label="Paste", command=pasteText)

m3 = Menu(menu, tearoff=0)
m3.add_command(label="About Notepad", command=about)

root.config(menu=menu)
menu.add_cascade(menu=m1, label="File")
menu.add_cascade(menu=m2, label="Edit")
menu.add_cascade(menu=m3, label="Help")

root.mainloop()
