import tkinter as tk
from tkinter import ttk

class TreeViewTest:

    def draw_treeview(self):
        root = tk.Tk()
        root.title("Treeview App")
        data = [("R1C1", "R1C2", "R1C3"), ("R2C1", "R2C2", "R2C3")]
        columns = ("Column #1", "Column #2", "Column #3")

        # Create Treeview
        tree = ttk.Treeview(root, columns=columns, show="headings")
        tree.pack(fill="both", expand=True)

        # Set headings
        for col in columns:
            tree.heading(col, text=col)

        # Insert data
        for item in data:
            tree.insert("", tk.END, values=item)

        root.mainloop()

test = TreeViewTest()
test.draw_treeview()