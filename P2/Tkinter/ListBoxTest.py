from tkinter import *

class ListBoxTest:

    def draw_listbox(self):
        # create a root window.
        top = Tk()
        top.title("ListBox Demo")
        # create listbox object
        listbox = Listbox(top, height = 10, 
                        width = 15, 
                        bg = "white",
                        activestyle = 'dotbox', 
                        font = "Helvetica",
                        fg = "green")

        # Define the size of the window.
        top.geometry("300x250")  

        # Define a label for the list.  
        label = Label(top, text = " FOOD ITEMS") 

        # insert elements by their
        # index and names.
        listbox.insert(1, "Nachos")
        listbox.insert(2, "Sandwich")
        listbox.insert(3, "Burger")
        listbox.insert(4, "Pizza")
        listbox.insert(5, "Burrito")

        # pack the widgets
        label.pack()
        listbox.pack()


        # Display until User 
        # exits themselves.
        top.mainloop()

test = ListBoxTest()
test.draw_listbox()