import json
import xml.etree.ElementTree as ET

from FileManager import FileManager
from Student import Student
from tkinter import *

class Main:
    def hola_mundo(self):
        print("hola mundo")

    def first_gui(self):
        root = Tk()
        root.title("Bienvenidos")
        root.geometry('500x400')
        
        lbl = Label(root, text = "Esta es mi primer etiqueta")
        lbl.grid()
        root.mainloop()
    
main = Main()
main.first_gui()