from tkinter import *


def name():
    print("My name is tkinter")

def hello():
    print("Hello Sir")

def greet():
    print("Good Morning")

def bye():
    print("Good Bye")

root = Tk()

root.geometry('752x545')

b1 = Button(root, text='Click Me',command=name)
b1.pack(side=LEFT, anchor='nw',pady=15,padx=10)
b2 = Button(root, text='Click Me',command=hello)
b2.pack(side=LEFT, anchor='nw',pady=15,padx=10)
b3 = Button(root, text='Click Me',command=greet)
b3.pack(side=LEFT, anchor='nw',pady=15,padx=10)
b4 = Button(root, text='Click Me',command=bye)
b4.pack(side=LEFT, anchor='nw',pady=15,padx=10)

root.mainloop()