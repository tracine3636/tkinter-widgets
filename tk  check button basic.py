
from tkinter import * # opens the tkinter class

root = Tk()  #just means open window

def oneclick():
    print("checkbox clicked")

button1 = Checkbutton(root, text = "button 1", command= oneclick)


button1.pack()



root.mainloop()

































my_window.mainloop() #this keeps the window open

