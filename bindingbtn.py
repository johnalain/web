#https://youtu.be/X3uxtPOodbA
import tkinter as tk
root = tk.Tk()
root.geometry('400x400')
root.title('tkinter hub')
def popup_menu(e):
    menu_bar=tk.Menu(x=e.x_root, y=e.y_root)
    

menu_but=tk.Button(root, text='michel',bd=0,font=('Bold, 25'))
menu_but.pack(side=tk.TOP,anchor=tk.W,pady=20,padx=20)
menu_but.bind('<Button-1>',popup_menu)

menu_bar=tk.Menu(root,tearoff=False)
menu_bar.add_command(label='Open Folder')
#https://youtu.be/X3uxtPOodbA?t=275

root.mainloop()