import ObjectList, objectCreator
from PIL import Image, ImageTk, ImageDraw
from numpy import ones, uint8
import Point
import numpy as np
from tkinter import Tk, Label, PhotoImage
from tkinter import ttk
focal_length = 50
image_width = 750
image_height = 750

window = Tk()
window.title("Third eye v3270.1")
window.configure(background='green')
window.geometry("{0}x{1}".format(image_width+25, image_height+25))
startImage = PhotoImage(file="Stage0.gif")
label = ttk.Label(window, image=startImage)
label.place(x=400, y=400)
label.pack()


right_move_vector = np.array([8, 0, 0])
left_move_vector = np.array([-8, 0, 0])
up_move_vector = np.array([0, 8, 0])
down_move_vector = np.array([0, -8, 0])

def castPoint( point_to_cast, focal_length, image_width, image_height):
    k = focal_length / point_to_cast.y
    x = ( k * point_to_cast.x ) + ( image_width / 2)
    y = ( image_height / 2) - k * point_to_cast.z
    return (x, y)

def leftKey(event):
    print("Left key pressed")

def rightKey(event):
    global right_move_vector
    global ol
    ol.sum_on_all_objects(right_move_vector)
    print("Right key pressed")

def upKey(event):
    print("Up key pressed")

def downKey(event):
    print("Down key pressed")

def qKey(event):
    print("Q key pressed")

def eKey(event):
    print("E key pressed")

def kKey(event):
    global focal_length
    if focal_length -5 < 0:
        focal_length = 0
    else:
        focal_length -= 5
    print("Decreased focal length to {0}".format(focal_length))
    redraw_image()

def lKey(event):
    global focal_length
    focal_length += 5
    print("Increased focal length to {0}".format(focal_length))
    redraw_image()



def draw_objects( object_list ):

    grey_image = ones([image_width, image_height], dtype=uint8) * 130
    grey_image = Image.fromarray(grey_image)

    draw = ImageDraw.Draw(grey_image)
    print("Redrawing with Focal_length: {0}".format(focal_length))
    for object_item in object_list.get_all_objects():
        print("Drawing object: {0}".format(object_item.__class__.__name__))
        object_lines = object_item.get_edges()
        for object_edge in object_lines:
            a = Point.Point(object_edge[0].x, object_edge[0].y, object_edge[0].z)
            b = Point.Point(object_edge[1].x, object_edge[1].y, object_edge[1].z)
            draw.line(
                [
                    castPoint(a, focal_length, image_width, image_height),
                    castPoint(b, focal_length, image_width, image_height)
                ]
                , fill=255
            )
    return ImageTk.PhotoImage(grey_image)

def redraw_image():
    global label
    global grey_image
    grey_image = draw_objects( ol )
    label.config(image=grey_image)
    print("Image was redrawn")


grey_image = ones([image_width, image_height], dtype=uint8)*130
grey_image = Image.fromarray(grey_image)
ol = ObjectList.MasterObjectList()

object_creator = objectCreator.objectCreator()
object_creator.case_two(ol) # case one has one line and one cube
redraw_image()

#
# panel = Label(window, image=draw_objects(ol))
# panel.config( image=PhotoImage(file="Stage1.gif"))
# panel = Label(window, image=PhotoImage(file="Stage1.gif"))
# panel.pack()


window.bind('<a>', leftKey)
window.bind('<d>', rightKey)
window.bind('<w>', upKey)
window.bind('<s>', downKey)
window.bind('<q>', qKey)
window.bind('<e>', eKey)

window.bind('<k>', kKey)
window.bind('<l>', lKey)



window.mainloop()


print("Hello world!")
