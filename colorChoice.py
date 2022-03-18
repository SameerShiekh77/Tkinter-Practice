from tkinter import *


root = Tk()

root.geometry("500x252")

root.title("Color Choice ")

Label(root, text='Choose your color').grid(row=0,column=4)

Checkbutton(root,text='Azure').grid(row=1,column=1)
Checkbutton(root,text='Green').grid(row=2,column=1)
Checkbutton(root,text='Black').grid(row=3,column=1)
Checkbutton(root,text='White').grid(row=4,column=1)

root.mainloop()