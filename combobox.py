##https://youtu.be/JNX-kURRs8I?list=PLSiLeKadTQ7nLJxpQo1-944miQKlheu-v video 14
# from tkinter import *
# from tkinter import ttk
# import tkinter

# pro = Tk()
# pro.geometry('600x400')
# combo1 = ttk.Combobox(pro,value=('male', 'female', 'kid'),state='readonly')
# combo1.place(x=1,y=1)
# combo2 = ttk.Combobox(pro,value=('syria', 'algeria', 'egypt'),state='readonly')
# combo2.place(x=1,y=40)
# pro.mainloop()
#https://youtu.be/481zQBwTPq0?list=PLSiLeKadTQ7nLJxpQo1-944miQKlheu-v video 15
# pro = Tk()
# pro.geometry('600x400')

# lst1 = Listbox(pro)
# lst1.insert(0,'zero')
# lst1.insert(1,'michelkadi')
# lst1.insert(2,'amal')
# lst1.insert(3,'josephine')
# lst1.insert(4,'rita')

# # lst1.pack()
# lst1.place(x=10,y=50)
#https://youtu.be/VMWjgauZFKs?list=PLSiLeKadTQ7nLJxpQo1-944miQKlheu-v video16
# r1 = ttk.Radiobutton(pro,text='michel333',value=1)
# r1.pack()
# r2 = ttk.Radiobutton(pro,text='rita33333',value=2)
# r2.pack()
# r3 = ttk.Radiobutton(pro,text='josephine',value=3)
# r3.pack()
#https://youtu.be/XEy006IF_xc?list=PLSiLeKadTQ7nLJxpQo1-944miQKlheu-v video 17
# c1 =  Checkbutton(pro,text='man')
# c1.pack()
# c2 =  Checkbutton(pro,text='woman')
# c2.pack()
# c3 =  Checkbutton(pro,text='married')
# c3.pack()
#https://youtu.be/cqE3cXx-JVI?list=PLSiLeKadTQ7nLJxpQo1-944miQKlheu-v video 18
# mn = Menubutton(pro,text='learn',relief='groove')
# mn.pack()
# ss = Menu(mn)
# mn['menu'] = ss
# ss.add_checkbutton(label='html')
# ss.add_checkbutton(label='css')
# ss.add_checkbutton(label='python')
#https://youtu.be/u0TZRtzaW_I?list=PLSiLeKadTQ7nLJxpQo1-944miQKlheu-v video 19
from tkinter import *
from tkinter import ttk
from tkinter import Menu, Tk


pro = Tk()
menubar = Menu(pro)

f = Menu(menubar,tearoff=0)
f.add_command(label='python')
f.add_command(label='javascript')
f.add_command(label='css')
f.add_command(label='java')
menubar.add_cascade(label='File',menu=f)
pro.config(menu=menubar)
pro.mainloop()
#test fail on menu
# import tkinter as tk
# from tkinter import Menu

# # root window
# root = tk.Tk()
# root.title('Menu Demo')

# # create a menubar
# menubar = Menu(root)
# root.config(menu=menubar)

# # create a menu
# file_menu = Menu(menubar)

# # add a menu item to the menu
# file_menu.add_command(
#     label='Exit',
#     command=root.destroy
# )


# # add the File menu to the menubar
# menubar.add_cascade(
#     label="File",
#     menu=file_menu
# )

root.mainloop()