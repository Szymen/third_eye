
from global_window import *

from tkinter import Label
from PIL import Image
from dead_kitten import *
import ObjectList, objectCreator
from numpy import ones, uint8
import  global_window




global_window.window.geometry("{0}x{1}".format(image_width+25, image_height+25))
grey_image = ones([image_width, image_height], dtype=uint8)*130
grey_image = Image.fromarray(grey_image)

global_window.ol = ObjectList.MasterObjectList()

object_creator = objectCreator.objectCreator()
object_creator.case_two(global_window.ol) # case one has one line and one cube

global_window.panel = Label(global_window.window, image=draw_objects(global_window.ol))
global_window.panel.pack()


global_window.window.bind('<a>', leftKey)
global_window.window.bind('<d>', rightKey)
global_window.window.bind('<w>', upKey)
global_window.window.bind('<s>', downKey)
global_window.window.bind('<q>', qKey)
global_window.window.bind('<e>', eKey)

global_window.window.bind('<k>', kKey)
global_window.window.bind('<l>', lKey)



global_window.window.mainloop()

print("Hello world!")
