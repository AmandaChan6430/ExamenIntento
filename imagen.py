from tkinter import *

from PIL import ImageTk, Image

ventana = Tk()
ventana.title("Imagen en tkinter")
ventana.iconbitmap(r"C:\Users\CHANIS\Downloads\istockphoto-1126396789-170667a.ico")

imagen = ImageTk.PhotoImage(Image.open(r"C:\Users\CHANIS\Downloads\istockphoto-1064117208-612x612.jpg"))
Label = Label(image=imagen)
Label.pack()

ventana.mainloop()
