from tkinter import *
App_root = Tk()

App_root.geometry("1000x1200")
App_root.minsize(500,600)
App_root.maxsize(1700,2000)


Title = Label(text="Aptech Latest News",font=("Times",24))
Title.pack()

Pic1 = PhotoImage(file="/Users/asp.APTECHNK1/Documents/Sameer Data/Python Presentation/Tkinter/image2.png")
Pic1_Label = Label(App_root,image=Pic1)
Pic1_Label.pack(side=LEFT,anchor='w')

Details1 = Label(text='''3D printing, or additive\n manufacturing, is the construction \nof a three-dimensional object from a CAD model or a digital 3D model.\n"" The term "3D printing" can refer to a variety\n of processes in which material is deposited, \njoined or solidified \nunder computer control to create a three-dimensional object," \n" with material being added together \n(such as plastics, liquids or powder grains being fused together), " \n"typically layer by layer.''',font=("Times",12))
Details1.pack(side=RIGHT,anchor='e')

# Pic2 = PhotoImage(file = "image2.png")
# Pic2_Label = Label(image=Pic2)
# Pic2_Label.pack()

App_root.mainloop()
