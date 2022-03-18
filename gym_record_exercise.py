from tkinter import *

def getValues():
    if userName.get() !='' or cityName.get() !='' or a.get() !='':
        f = open("Tkinter/record.txt",'a')
        f.write(f"Name: {userName.get()}\nCity: {cityName.get()}\nAge: {a.get()}\n\n********************************\n\n")
        f.close()
        print(userName.get())
        print(cityName.get())
        print(a.get())
    else:
        print("Please Complete the form")


root = Tk()
root.geometry("444x222")
root.title("Gym Management System")
userName = StringVar()
cityName = StringVar()
a = StringVar()


name = Label(text='Enter Your Name',pady=15)
name.grid(row=0,column=0)

nameText = Entry(root,textvariable =  userName)
nameText.grid(row=0,column=1)

city = Label(text='Enter your city',pady=15)
city.grid(row=1,column=0)


cityValue = Entry(root,textvariable =  cityName)
cityValue.grid(row=1,column=1)


age = Label(text='Enter your age',pady=15)
age.grid(row=2,column=0)


ageValue = Entry(root,textvariable =  a)
ageValue.grid(row=2,column=1)

Button(text="Submit",command=getValues,width=25,bg='green',fg='white',borderwidth=2,relief=SUNKEN).grid(row=3,column=1)

root.mainloop()