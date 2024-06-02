import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

filename = filedialog.askopenfilename( title='open', filetypes=(('Text Files', '*.txt'),('Excel Files', '*.csv'), ('All Files', '*.*')))
#print (filename)
myfile = open(filename)

print()

print(myfile)


