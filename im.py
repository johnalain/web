from tkinter import *

from PIL import ImageTk, Image

def mik():
    print("Hello,newworld")
    print("learning pythond")
pro =Tk()
pro.geometry('880x230')
pro.title("Hello World")
pro.resizable(800,400)

b1 = Button(pro, text="click me", command=mik)
b1.pack()
l1 = Label(pro, text="Hello World", fg='white', bg='blue')
l1.pack()
l2 = Label(pro, text="im the instructor")

im1 = ImageTk.PhotoImage(Image.open("img.jpeg"))
# im2 = ImageTk.PhotoImage(Image.open("horse/download.jpeg"))
# im3 = ImageTk.PhotoImage(Image.open("horse/download.jpeg"))
# im4 = ImageTk.PhotoImage(Image.open("horse/download.jpeg"))

my_label = Label(image=im1)
my_label.place(x=40,y=40)
# my_label.grid(row=0, column=0,columnspan=2)



pro.mainloop()