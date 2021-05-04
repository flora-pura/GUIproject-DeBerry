from tkinter import *

top = Tk()
playlist = []

def addSong():
    playlist.append(E1.get())

def printList():
    print(playlist)

#this is a lable widget
L1 = Label(top, text="Hello, world!")
L1.grid(column= 0, row= 1)

#this is a text entry widget
E1 = Entry(top, bd = 5)
E1.grid(column = 0, row = 2)

#this is a button widget
B1 = Button(text="Add to Playlist", bg = "light blue", command = addSong)
B1.grid(column = 1, row = 2)

B2 = Button("Export List", bg = "green", command = printList)
B2.grid(column=1, row =1)




top.mainloop()
