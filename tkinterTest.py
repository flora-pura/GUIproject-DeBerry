from tkinter import *

top = Tk()
playlist = []

def addSong():
    playlist.append(E1.get())
    E1.delete(0, END)

def printList():
    print(playlist)

def exportPlaylist():
    with open('playlist.txt', 'w') as f:
        for song in playlist:
            f.write("%s\n" % song)

#this is a lable widget
L1 = Label(top, text="Hello, world!")
L1.grid(column = 0, row = 1)

#this is a text entry widget
E1 = Entry(top, bd = 5)
E1.grid(column = 0, row = 2)

#this is a button widget
B1 = Button(text=" + ", bg = "#B4E9FF", command = addSong)
B1.grid(column = 1, row = 2)

B2 = Button(text = "Print List", bg = "#D9B1FF", fg = "white", command = printList)
B2.grid(column = 0, row = 3)

B3 = Button(text = "Export List", bg = "#FFD4FE", command = exportPlaylist)
B3.grid(column = 1, row = 3) 


top.mainloop()
