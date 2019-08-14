

from tkinter import *



root = Tk()



var = IntVar()

w = Scale(root, from_=1, to=50,resolution=1,activebackground='red',length=200, variable= var)

w.grid(row=0,column=0)































mainloop()
