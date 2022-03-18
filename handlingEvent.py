from tkinter import *

def sameer(event):
    print(event.char)
    print(f"You clicked on the button at {event.char}, {event.y}")

def focusControl(event):
    print(f"You clicked on the button at {event.keycode}")
root = Tk()
root.title("Events in Tkinter")
root.geometry("644x334")

widget = Button(root, text='Click me please')
widget.pack()

e = Entry(root)
e.pack()
e2 = Entry(root)
e2.pack()
e.bind('<Key>',focusControl)
# e.bind('<Return>',focusControl)
widget.bind('<Return>', focusControl)
# widget.bind('<Double-1>', quit)
root.mainloop()


