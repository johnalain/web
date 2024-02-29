#https://youtu.be/_lTmNDSjc_8?list=PLSiLeKadTQ7nLJxpQo1-944miQKlheu-v
from tkinter import *

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

l1 = Label(fr1,text='im learning',fg='white',bg='green',font=40)
l1.place(x=10,y=50) 
l2 = Label(fr2,text='josephine',fg='white',bg='black',font=40)
l2.place(x=10,y=50)
#https://youtu.be/7Dd_kp21VvY?list=PLSiLeKadTQ7nLJxpQo1-944miQKlheu-v  video 13
window.mainloop()

