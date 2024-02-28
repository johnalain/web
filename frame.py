#https://youtu.be/_lTmNDSjc_8?list=PLSiLeKadTQ7nLJxpQo1-944miQKlheu-v
from tkinter import *
window =Tk()
window.geometry('800x600')
fr1 = Frame(width='390', height='599',bg='red')
fr1.place(x=0,y=0)

fr2 = Frame(width='390', height='599',bg='blue')
fr2.place(x=393,y=1)

bt1 = Button(fr1,text='button1',fg='black',bg='white',cursor='heart')
bt1.place(x=10,y=10)

bt2 = Button(fr2,text='button2',fg='red',bg='black',cursor='hand')
bt2.place(x=10,y=10)

l1 = Label(fr1,text='im learning',fg='black',bg='white')
l1.place(x=10,y=50) 

window.mainloop()

