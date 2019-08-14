from tkinter import * # opens the tkinter class

root = Tk()
root.title("Navigation Panel")



# camera buttons
up_arrow = Button(root, text = "   Up   ",fg = "white", bg= "blue")
down_arrow = Button(root, text = " Down ",fg = "white", bg= "blue")
left_arrow = Button(root, text = " Left ",fg = "white", bg= "blue")
right_arrow = Button(root, text = "Right",fg = "white", bg= "blue")
#camera button locations
up_arrow.grid(row=10, column=11)
down_arrow.grid(row=12, column=11)
left_arrow.grid(row=11, column=1)
right_arrow.grid(row=11, column=12)
#camera label
camera_label = Label(root,text="Camera Control")
#camera label location
camera_label.grid(row=13, column=11)


#scale
var = IntVar()

x = Scale(root, from_=100, to=1,resolution=1,activebackground='blue',length=100, variable= var, fg="blue")

x.grid(row=14,column=330)

var = IntVar()

y = Scale(root, from_=100, to=1,resolution=1,activebackground='blue',length=100, variable= var, fg="blue")

y.grid(row=14,column=350)

var = IntVar()

z = Scale(root, from_=100, to=1,resolution=1,activebackground='blue',length=100, variable= var, fg="blue")

z.grid(row=14,column=370)

scale_label = Label(root,text="      Throttle")
#scale label location
scale_label.grid(row=17, column=350)































root.geometry("700x500")
root.mainloop()

































my_window.mainloop() #this keeps the window open

