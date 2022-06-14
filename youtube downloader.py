from tkinter import *
import tkinter as tk
from pytube import *

root = Tk()

root.geometry('540x300')
root.resizable(0, 0)

root.title("Youtube video downloader")

border_effects = {
    "groove" : tk.GROOVE ,
}

for relief_name, relief in border_effects.items():
    frame1 = tk.Frame(master=root, relief=relief, borderwidth=10 , bg ="dark blue" )
    frame1.pack()    

bottomframe1 = Frame(root)
bottomframe1.place(x = 270 , y = 130)

label1 = Label(master = frame1, text="Youtube downloader!", font='arial 20 bold', fg="purple", bg="black" ).pack()

effect = Frame(root , relief=relief , bg = "dark blue" , borderwidth= 5)
label2 = Label(effect, text="Paste the Url here! :", font='arial 15 bold' , bg = "sky blue" , fg = "black",).pack()
effect.place(x = 8 , y = 88)

link = StringVar()
entry_url = Entry(master = root,width=40 ,textvariable=link).place(x=170, y=90)


def downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    video.get_file_path()
      
    Label(root,Button.config(root,text = "DOWNLOADED"), height=30, font='arial 15').place(x=280, y=130)

frame2 = tk.Frame(master=root, relief=relief, borderwidth=5 , bg ="dark blue" )
frame2.place(x = 300 , y = 150)
Button(master = frame2, text="EXIT", width=10, font="arial 15 bold", fg = "red", bg="red", command=root.quit).pack()


frame3 = tk.Frame(master=root, relief=relief, borderwidth=5 , bg ="dark blue" )
frame3.place(x=110, y=150)
Button(master = frame3, text= "DOWNLOAD ", width=10, font="arial 15 bold", fg = "green",bg='pale violet red', padx=2, command=downloader).pack()

root.mainloop()