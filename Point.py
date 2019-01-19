import numpy as np

class Point:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        # self.j = 0

    def __str__(self):
        return "({0}, {1}, {2})".format(self.x, self.y, self.z)

    def __add__(self, vector_to_add):
        # print("[POINT]: Adding {0} to {1} = {2}".format(vector_to_add, self, np.add(self.get_coords_as_array(), vector_to_add)))
        foo = Point(0, 0, 0)
        foo.set_coords_from_array( np.add( self.get_coords_as_array(), vector_to_add ))
        # print("[POINT]: After adding vector {0}".format(foo))
        return foo

    def __mul__(self, other):
        foo = Point(0, 0, 0)
        foo.set_coords_from_array( np.multiply(self.get_coords_as_array(), other))
        # print("[POINT]: After adding vector {0}".format(foo))
        return foo

    def get_coords_as_array(self):
        return np.array( [self.x, self.y, self.z] )

    def set_coords_from_array(self, array):
        self.x, self.y, self.z = array

    def multiply(self, vector):
        self.set_coords_from_array( np.multiply( self.get_coords_as_array(), vector) )

    def add_vector(self, vector):
        self.set_coords_from_array( np.add( self.get_coords_as_array(), vector) )
