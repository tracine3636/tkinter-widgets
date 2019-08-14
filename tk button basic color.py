from tkinter import * # opens the tkinter class



def onclick():
    print("Button Clicked")



root = Tk()  #just means open window




button1 = Button(root, text = "button 1", command = onclick,fg = "yellow", bg = "red")






button1.pack()





root.mainloop()

































my_window.mainloop() #this keeps the window open

