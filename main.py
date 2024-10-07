from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.title("Pic in widgets for tkinter")
window.geometry("400x400")


upload = Image.open("images.jpeg")
image = ImageTk.PhotoImage(upload)

label = Label(window, image=image, height=350, width=300)
label.place(x=50, y=0)

label2 = Label(window, text="This is a forest")
label2.place(x=40, y=30)

window.mainloop()