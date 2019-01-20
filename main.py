import ObjectList, objectCreator
from PIL import Image, ImageTk, ImageDraw
from numpy import ones, uint8
import Point
import numpy as np
from tkinter import Tk, Label, PhotoImage
from tkinter import ttk
import time
import dead_kitten
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


xp_rotate_matrix=dead_kitten.get_rotation_matrix(15,0,0)
xm_rotate_matrix=dead_kitten.get_rotation_matrix(-15,0,0)
yp_rotate_matrix=dead_kitten.get_rotation_matrix(0,15,0)
ym_rotate_matrix=dead_kitten.get_rotation_matrix(0,-15,0)
zp_rotate_matrix=dead_kitten.get_rotation_matrix(0,0,15)
zm_rotate_matrix=dead_kitten.get_rotation_matrix(0,0,-15)




forward_move_vector = np.array([0, 0, 8]) 
backward_move_vector = np.array([0, 0, -8])

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
    global left_move_vector
    move_all(left_move_vector)
    redraw_image()
    
def rightKey(event):
    print("Right key pressed")
    global right_move_vector
    move_all(right_move_vector)
    redraw_image()

def upKey(event):
    print("Up key pressed")
    global up_move_vector
    move_all(up_move_vector)
    redraw_image()

def downKey(event):
    print("Down key pressed")
    global down_move_vector
    move_all(down_move_vector)
    redraw_image()

def forwardKey(event):
    print("Forward key pressed")
    global forward_move_vector
    move_all(forward_move_vector)
    redraw_image()

def backwardKey(event):
    print("Backward key pressed")
    global backward_move_vector
    move_all(backward_move_vector)
    redraw_image()

def rot_xp_Key(event):
    global xp_rotate_matrix
    rotate_all(xp_rotate_matrix)
    redraw_image()
    
def rot_xm_Key(event):
    global xm_rotate_matrix
    rotate_all(xm_rotate_matrix)
    redraw_image()
    
def rot_yp_Key(event):
    global yp_rotate_matrix
    rotate_all(yp_rotate_matrix)
    redraw_image()
    
def rot_ym_Key(event):
    global ym_rotate_matrix
    rotate_all(ym_rotate_matrix)
    redraw_image()
    
def rot_zp_Key(event):
    global zp_rotate_matrix
    rotate_all(zp_rotate_matrix)
    redraw_image()
    
def rot_zm_Key(event):
    global zm_rotate_matrix
    rotate_all(zm_rotate_matrix)
    redraw_image()
    




def shrinkKey(event):
    global focal_length
    if focal_length -5 < 0:
        focal_length = 0
    else:
        focal_length -= 5
    print("Decreased focal length to {0}".format(focal_length))
    redraw_image()

def zoomKey(event):
    global focal_length
    focal_length += 5
    print("Increased focal length to {0}".format(focal_length))
    redraw_image()



def draw_objects( wiadro ):

    grey_image = ones([image_width, image_height], dtype=uint8) * 130
    grey_image = Image.fromarray(grey_image)

    draw = ImageDraw.Draw(grey_image)
    for object_item in wiadro:
        object_lines = object_item.get_edges()
        for object_edge in object_lines:
            draw.line(
                [
                    castPoint(object_edge.pointA, focal_length, image_width, image_height),
                    castPoint(object_edge.pointB, focal_length, image_width, image_height)
                ]
                , fill=255
            )
    return ImageTk.PhotoImage(grey_image)

def redraw_image():
    global label
    global grey_image
    global ol

    tmp_list = ol.get_all_objects()
    grey_image = draw_objects(tmp_list)

    label.config(image=grey_image)


def move_all( move_vector ):
    global ol
    for object_item in ol.get_all_objects():
        object_item.add_vector(move_vector)

def rotate_all( rot_vector ):
    global ol
    for object_item in ol.get_all_objects():
        object_item.multiply_by_matrix(rot_vector)



grey_image = ones([image_width, image_height], dtype=uint8)*130
grey_image = Image.fromarray(grey_image)
ol = ObjectList.MasterObjectList()

object_creator = objectCreator.objectCreator()
object_creator.case_two(ol) # case one has one line and one cube

redraw_image()



window.bind('<d>', leftKey)    
window.bind('<a>', rightKey)
window.bind('<r>', downKey)
window.bind('<f>', upKey)

window.bind('<w>', backwardKey) 
window.bind('<s>', forwardKey)

window.bind('<t>', zoomKey)
window.bind('<g>', shrinkKey)



window.bind('<i>', rot_xp_Key)
window.bind('<k>', rot_xm_Key)

window.bind('<j>', rot_yp_Key)
window.bind('<l>', rot_ym_Key)

window.bind('<u>', rot_zp_Key)
window.bind('<o>', rot_zm_Key)



window.mainloop()


print("Hello world!")
