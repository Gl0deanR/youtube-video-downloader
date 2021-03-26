import pytube
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tkinter.messagebox

gui = Tk()
gui.geometry("500x100")
gui.title("Download YouTube Video - GR@beLIKE")

def getFolderPath():
    folder_selected = filedialog.askdirectory()
    folderPath.set(folder_selected)

folderPath = StringVar()
videoLink = StringVar()

ab = Label(gui, text="YouTube Video Link")
ab.grid(row=0,column=0)

abE = Entry(gui,textvariable=videoLink)
abE.grid(row=0,column=1)

a = Label(gui, text="Path to save to")
a.grid(row=1,column=0)

E = Entry(gui,textvariable=folderPath)
E.grid(row=1,column=1)

btnFind = ttk.Button(gui, text="Browse folder",command=getFolderPath)
btnFind.grid(row=1,column=3)


def doStuff():
    url_to_download = videoLink.get()
    path_to_download = folderPath.get()
    youtube = pytube.YouTube(url_to_download)
    video = youtube.streams.get_highest_resolution()
    video.download(path_to_download)

    tkinter.messagebox.showinfo('DONE!','Video downloaded!')


c = ttk.Button(gui ,text="Download", command=doStuff)
c.grid(row=5,column=1)
gui.mainloop()
