from tkinter import *

class ScrollbarTest:

    def draw_scrollbar(self):
        root = Tk()
        root.title("Scrollbar Demo")
        root.geometry("150x200")
        
        w = Label(root, text ='Welcome!!',
                font = "50") 

        w.pack()
        
        scroll_bar = Scrollbar(root)

        scroll_bar.pack( side = RIGHT,
                        fill = Y )
        
        mylist = Listbox(root, 
                        yscrollcommand = scroll_bar.set )
        
        for line in range(1, 26):
            mylist.insert(END, "Student " + str(line))

        mylist.pack( side = LEFT, fill = BOTH )

        scroll_bar.config( command = mylist.yview )
        
        root.mainloop()

test = ScrollbarTest()
test.draw_scrollbar()