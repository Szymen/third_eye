from tkinter import *

main = Tk()

def leftKey(event):
    print("Left key pressed")

def rightKey(event):
    print("Right key pressed")

def upKey(event):
    print("Up key pressed")

def downKey(event):
    print("Down key pressed")

def qKey(event):
    print("Q key pressed")

def eKey(event):
    print("E key pressed")

frame = Frame(main, width=100, height=100)
main.bind('<a>', leftKey)
main.bind('<d>', rightKey)
main.bind('<w>', upKey)
main.bind('<s>', downKey)
main.bind('<q>', qKey)
main.bind('<e>', eKey)
frame.pack()
main.mainloop()

print("Hello world!")