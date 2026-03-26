

import tkinter as tk

class LabelTest:

    def draw_label(self):
        root = tk.Tk()
        root.title("Label Demo")
        root.geometry('500x400')
        lbl = tk.Label(root, text="Hello World")
        lbl.pack()

        root.mainloop()

test = LabelTest()
test.draw_label()