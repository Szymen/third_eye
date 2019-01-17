from PIL import Image, ImageTk, ImageDraw
from numpy import ones, uint8
import Point
import global_window

def castPoint( point_to_cast, focal_length, image_width, image_height):
    k = focal_length / point_to_cast.y
    x = ( k * point_to_cast.x ) + ( image_width / 2)
    y = ( image_height / 2) - k * point_to_cast.z
    return (x, y)

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

def kKey(event):
    # global focal_length
    global_window.focal_length -= 5
    print("Decreased focal length to {0}".format(global_window.focal_length))
    redraw_image()

def lKey(event):
    global_window.focal_length += 5
    print("Increased focal length to {0}".format(global_window.focal_length))
    redraw_image()



def draw_objects( object_list ):

    grey_image = ones([global_window.image_width, global_window.image_height], dtype=uint8) * 130
    grey_image = Image.fromarray(grey_image)

    draw = ImageDraw.Draw(grey_image)
    print("Redrawing with Focal_length: {0}".format(global_window.focal_length))
    for object_item in object_list.get_all_objects():
        print("Drawing object: {0}".format(object_item.__class__.__name__))
        object_lines = object_item.get_edges()
        for object_edge in object_lines:
            a = Point.Point(object_edge[0].x, object_edge[0].y, object_edge[0].z)
            b = Point.Point(object_edge[1].x, object_edge[1].y, object_edge[1].z)


            draw.line(
                [
                    castPoint(a, global_window.focal_length, global_window.image_width, global_window.image_height),
                    castPoint(b, global_window.focal_length, global_window.image_width, global_window.image_height)
                ]
                , fill=255
            )

    tkimage = ImageTk.PhotoImage(grey_image)
    return tkimage

def redraw_image():
    global_window.panel.config(image=draw_objects( global_window.ol ))
    print("Image was redrawn")
