from tkinter import *

class CheckbuttonTest:

    def draw_checkbutton(self):
        root = Tk() 
        root.title("CheckButton Demo")
        root.geometry('500x400')

        w = Label(root, text ='Welcome!!', font = "50") 
        w.pack() 

        Checkbutton1 = IntVar() 
        Checkbutton2 = IntVar() 
        Checkbutton3 = IntVar() 

        Button1 = Checkbutton(root, text = "Tutorial", 
                            variable = Checkbutton1, 
                            onvalue = 1, 
                            offvalue = 0, 
                            height = 2, 
                            width = 10) 

        Button2 = Checkbutton(root, text = "Student", 
                            variable = Checkbutton2, 
                            onvalue = 1, 
                            offvalue = 0, 
                            height = 2, 
                            width = 10) 

        Button3 = Checkbutton(root, text = "Courses", 
                            variable = Checkbutton3, 
                            onvalue = 1, 
                            offvalue = 0, 
                            height = 2, 
                            width = 10) 
            
        Button1.pack() 
        Button2.pack() 
        Button3.pack() 

        mainloop()

test = CheckbuttonTest()
test.draw_checkbutton()