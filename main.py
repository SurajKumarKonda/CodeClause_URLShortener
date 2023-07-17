import pyshorteners
from tkinter import *

win = Tk()
win.geometry("500x300")
win.configure(bg="pink")
#Button Function
def short():
    url = entry1.get()
    s = pyshorteners.Shortener().tinyurl.short(url)

    entry2.insert(END, s)
#Label for entering user url
Label(win,text="Please Enter Your Url Link", font="helvetica 18 bold", bg="purple", fg="white").pack(fill="x")
#Entry Box
entry1 = Entry(win, font="10", bd=3, width=40)
entry1.pack(pady=30)
#Button
Button(win, text="Click Me", font="helvetica 16", bg="green", fg="white", width="14", command=short).pack()
#Entry
entry2 = Entry(win,font="impack 16 bold", bg="pink", width=24, bd=0)
entry2.pack(pady=30)
mainloop()