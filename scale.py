from tkinter import *



master = Tk()



def values():

    l.delete(0,END)

    c1=var.get()

    c2=var2.get()

    for i in range(c1,c2+1):

        l.insert(END,i)

    lb = Label(master,text="Scale 1= {}".format(c1),fg='red',font="(cursive,20)").grid(row=2,column=2)

    lb2 = Label(master,text="Scale 2= {}".format(c2),fg='red',font="(cursive,20)").grid(row=3,column=2)



var = IntVar()

w = Scale(master, from_=1, to=50,resolution=1,activebackground='red',length=200, variable= var)

w.grid(row=0,column=0)



l= Listbox(master, width=20)

l.grid(row=0,column=1)



var2 = IntVar()

e = Scale(master, from_=1,resolution=2, to=100, orient=HORIZONTAL,sliderlength=15,length=150,variable=var2)

e.grid(row=1,column=1 , columnspan=4)



btn = Button(text="Get values",bg='green' ,fg='white', command=values).grid(row=3,column=0,columnspan=4)

mainloop()

