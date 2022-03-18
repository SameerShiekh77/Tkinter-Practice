from tkinter import *

root = Tk()
root.geometry("654x621")


def hello():
    print("hello tkinter")

frame = Frame(root,borderwidth=6,bg='grey',relief=SUNKEN  )
frame.pack(side=LEFT,anchor='nw')


b1 = Button(frame,text='CLICK ME',borderwidth=5,fg='red',command =hello)
b1.pack(side=LEFT, padx=25,)

b2 = Button(frame,text='CLICK ME',borderwidth=5,fg='red')
b2.pack(side=LEFT, padx=25,)

b3 = Button(frame,text='CLICK ME',borderwidth=5,fg='red')
b3.pack(side=LEFT, padx=25,)

b4 = Button(frame,text='CLICK ME',borderwidth=5,fg='red')
b4.pack(side=LEFT, padx=25,)

root.mainloop()