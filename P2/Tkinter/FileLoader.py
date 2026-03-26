import tkinter as tk
from tkinter import filedialog as fd
from tkinter import scrolledtext

class FileLoader:
    
    root = tk.Tk()
    root.title("Text File Reader")
    root.geometry("600x400")

    text_area = tk.Text(root, height=2, width=4)
    text_area.pack(padx=20, pady=20)
    
    def open_file(self):
        """Open a text file and insert its content into the text widget."""
        filetypes = (
            ('Text files', '*.txt'),
            ('Text files', '*.json'),
            ('All files', '*.*')
        )

        # Open a file dialog to select a single file and return an open file handle
        file_handle = fd.askopenfile(
            title='Open a file',
            initialdir='/', # You can change the initial directory
            filetypes=filetypes
        )

        if file_handle:
            # Read the file's content
            content = file_handle.read()
            print(content)
            # Clear previous content in the Text widget
            
            
            # Insert the content into the Text widget
            self.text_area.insert(tk.END, content)
            
            # Close the file handle
            file_handle.close()

    def draw_app(self):

        # Create a Button to open the file dialog
        open_button = tk.Button(
            self.root,
            text='Open Text File',
            command=self.open_file
        )
        open_button.pack(pady=10)

        # Create a ScrolledText widget (includes built-in scrollbars)
        self.text_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, padx=1, pady=1)
        self.text_area.pack(expand=True, fill='both')

        # Run the Tkinter event loop
        self.root.mainloop()

test = FileLoader()
test.draw_app()