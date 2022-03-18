from tkinter import *

def getVals():
    if nameValue.get() != '' or genderValue.get() != '' or phoneValue.get() != '' or paymentModeValue.get() != '' or cityValue.get() != '':
        print("Form Submitted Successfully")         
        with open('travels.txt', 'a') as f:
            f.write(f"Name: {nameValue.get()}\nGender: {genderValue.get()}\nPhone:{phoneValue.get()}\nCity:{cityValue.get()}\nPayment Mode: {paymentModeValue.get()}\n\n*****************************\n")
       
    else:
        print("Please Complete Form")
         

root = Tk()
root.title("Travel Checker GUI Program")
root.geometry("545x464")

root.minsize(550,430)
root.maxsize(600,450)
# heading
Label(text="Welcome To PIA Travels",font="Arial 24 bold").grid(row=0,column=2)

# Create and Pack labels  fand Fandm
name = Label(text="Full Name",pady=15,font='Times 15').grid(row=1,column=1)
gender = Label(text="Gender",pady=15,font='Times 15').grid(row=2,column=1)
phone = Label(text="Phone",pady=15,font='Times 15').grid(row=3,column=1)
city = Label(text="City",pady=15,font='Times 15').grid(row=4,column=1)
paymentMode = Label(text="Payment Mode",pady=15,font='Times 15').grid(row=5,column=1)

#Create Tkinter Variables

nameValue = StringVar()
genderValue = StringVar()
phoneValue = StringVar()
cityValue = StringVar()
foodServiceValue = IntVar()
paymentModeValue = StringVar()


# Create Entries fand Fandm

nameEntry = Entry(root,width=30,textvariable=nameValue).grid(row=1,column=2)
genderEntry = Entry(root,width=30,textvariable=genderValue).grid(row=2,column=2)
phoneEntry = Entry(root,width=30,textvariable=phoneValue).grid(row=3,column=2)
cityEntry = Entry(root,width=30,textvariable=cityValue).grid(row=4,column=2)
paymentModeEntry = Entry(root,width=30,textvariable=paymentModeValue).grid(row=5,column=2)

# Checkbox button

checkBtn = Checkbutton(root,font='Times 14 italic',text='Do you want to prebook meals?')
checkBtn.grid(row=6,column=2,pady=12)

    # Submit Button

Button(root,text='Submit Record!!',bg='green',font='Arial 15',borderwidth=2,fg='white',relief=RAISED,command=getVals).grid(row=7,column=0,columnspan=2)

Button(root,width=30,text='Quit!!',bg='red',font='Arial 15',borderwidth=2,fg='white',relief=SUNKEN,command=root.quit).grid(row=7,column=2,columnspan=3)


root.mainloop()