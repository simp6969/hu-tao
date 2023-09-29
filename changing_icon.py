from tkinter import *
import ctypes
from PIL import Image,ImageTk

root = Tk()
root.geometry("300x330")
root.title("changing the icon")
canvas= Canvas(root, width= 300, height= 300)
canvas.pack()




img= (Image.open("C:\workspace\workspace\icon.png"))
resized_image= img.resize((300,300))
new_image= ImageTk.PhotoImage(resized_image)
canvas.create_image(10,10, anchor=NW, image=new_image)
Label(root, text="hellow").pack()

icon_path = 'C:\workspace\workspace\icon.ico'
myappid = 'mycompany.myproduct.subproduct.version'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
root.iconbitmap(icon_path)



root.mainloop()