from tkinter import *
# from pillow import ImageTk, Image
root = Tk()

# Width x Height
root.geometry("733x433")

# width, height
root.minsize(300,100)

# width, height
root.maxsize(1200, 988)
root.title("MY GUI")
heading = Label(text="VS Code Editor")
heading.pack()

image = PhotoImage(file='image.png')
# for jpeg images
# image = Image.open('download.jpeg')

# photo = ImageTk.PhotoImage(image)

varun_label = Label(image=image)
varun_label.pack()
root.mainloop()
