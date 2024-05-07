from tkinter import *
import qrcode

root = Tk()
root.title("QR CODE GENERATOR")
root.geometry("1000x550")
root.config(bg="#D2DADC")
root.resizable(False,False)


def generate():
    name= title.get()
    text= entry.get()
    qr=qrcode.make(text)
    qr.save("Qrcode/"+ str(name)+".png")

Label(root, text="Welcome to the QRCODE Generator", fg="black", bg="#D2DADC", font=15).place(x=50,y=170)

title=Entry(root, text="Insert here the file name", fg="black", width=13, font="arial 15")
title.place(x=50, y=200)

entry = Entry(root,width=28, text="Insert here the URL link", fg="black", font="arial 15")
entry.place(x=50, y=250)

Button(root,text="Generate QrCode", width=20, height=2, bg="green", fg="white", command=generate).place(x=50, y=300)
root.mainloop()