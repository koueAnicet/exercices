from distutils import command
from email.mime import image
from struct import pack
from tkinter import*
#from PIL import ImageTk,Image
from tkinter import filedialog

root = Tk()
#aller sur une autre fenetre
"""top = Toplevel()
lbl = Label(top, text="hello", width=30, height=12).pack()
"""
#aller chercher un fichier dans le directories
"""def open():

    root.filename = filedialog.askopenfilename(initialdir="Documents/python", title="select a file", filetypes=(("png files","*.png"),("alll files","*.*")))
    my_label =Label(root, text=root.filname).pack()
    my_image= ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()
my_btn =Button(root, text="open File",command=open).pack()"""

root.mainloop()