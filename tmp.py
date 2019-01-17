from tkinter import *
from tkinter import ttk


def TestLogic():
    print("Test logic!")
    global stgImg
    stgImg = PhotoImage(file="Stage1.gif")
    label.config(image=stgImg)
    label.place(x=400, y=400)
    print(stgImg)



root = Tk()

root.geometry('1010x740+200+200')

stgImg = PhotoImage(file="Stage0.gif")
label = ttk.Label(root, image=stgImg)
label.place(x=400, y=400)
label.pack()

testBtn = ttk.Button(root, text="TEST", command=TestLogic)
testBtn.place(x=400, y=200)

# root.after(1000, TestLogic())
root.mainloop()