from tkinter import *
root = Tk()
root.geometry("655x333")
f1 = Frame(root, bg="grey", borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT, fill="y")

f2 = Frame(root, borderwidth=8, bg="grey", relief=SUNKEN)
f2.pack(side=TOP, fill="x")

l1 = Label(f1, text="Project Tkinter - Pycharm",bg='grey')
l1.pack( pady=142)

l2 = Label(f2, text="Welcome to sublime text", font="Helvetica 16 bold", fg="red", pady=22)
l2.pack()

root.mainloop()