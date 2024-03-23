#https://youtu.be/_lTmNDSjc_8?list=PLSiLeKadTQ7nLJxpQo1-944miQKlheu-v
from tkinter import *
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import Tk
window =Tk()
window.geometry('800x600')
fr1 = Frame(width='390', height='599',bg='red')
fr1.place(x=0,y=0)

fr2 = Frame(width='390', height='599',bg='blue')
fr2.place(x=393,y=1)

bt1 = Button(fr1,text='button1',fg='black',bg='white',cursor='heart',width=30)
bt1.place(x=10,y=10)

bt2 = Button(fr2,text='button2',fg='red',bg='black',cursor='hand',width=30)
bt2.place(x=10,y=10)

bt3 = Button(fr2,text='button3',fg='black',bg='white',cursor='hand',width=20)
bt3.place(x=10,y=220)

l1 = Label(fr1,text='im learning',fg='white',bg='green',font=40)
l1.place(x=10,y=50) 
l2 = Label(fr2,text='josephine',fg='white',bg='black',font=40)
l2.place(x=10,y=50)
#https://youtu.be/7Dd_kp21VvY?list=PLSiLeKadTQ7nLJxpQo1-944miQKlheu-v  video 13
en1 = Entry(fr1, justify='center')
en1.place(x=10,y=100)
en2 = Entry(fr2, justify='center')
en2.place(x=10,y=90)
en3 = Entry(fr2, justify='center',fg='red',bg='black')
en3.place(x=10,y=130)
en4 = Entry(fr2, justify='center',fg='red',bg='black',font=10)
en4.place(x=10,y=180)
en4 = Entry(fr1, justify='center',fg='red',bg='black',font=10)
en4.place(x=10,y=140)

#https://youtu.be/JNX-kURRs8I?list=PLSiLeKadTQ7nLJxpQo1-944miQKlheu-v video 14
window.mainloop()

