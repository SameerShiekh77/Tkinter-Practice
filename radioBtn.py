
from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("455x233")
root.title("Radiobutton ")
def order():

    tmsg.showinfo("Order Received!", f"We have received your order for {var.get()}. Thanks for ordering")

# var = IntVar()
var = StringVar()
var.set("Radio")
# var.set(1)
Label(root, text = "What would you like to have sir?",font="lucida 19 bold",
      justify=LEFT, padx=14).pack()
Radiobutton(root, text="Zinger", padx=14, variable=var, value="Zinger").pack(anchor="w")
Radiobutton(root, text="Tikka", padx=14, variable=var, value="Tikka").pack(anchor="w")
Radiobutton(root, text="Biryani", padx=14, variable=var, value="Biryani").pack(anchor="w")
Radiobutton(root, text="Samosa", padx=14, variable=var, value="Samosa").pack(anchor="w")

Button(text="Order Now", command=order).pack()
root.mainloop()
