import numpy as np
import hashlib
class Point:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        # self.j = 0

    def __str__(self):
        return "({0}, {1}, {2})".format(self.x, self.y, self.z)

    def __add__(self, vector_to_add):
        foo = Point(0, 0, 0)
        foo.set_coords_from_array( np.add( self.get_coords_as_array(), vector_to_add ))
        return foo

    def __mul__(self, other):
        foo = Point(0, 0, 0)
        coords = np.matrix( self.get_coords_as_array() )
        coords.transpose()
        mat = other
        res = np.matmul(self.get_coords_as_array(), other)
        foo.set_coords_from_array( res )
        return foo

    def __hash__(self):
        string = "({0},{1},{2})".format(self.x, self.y, self.z)
        m = hashlib.sha256()
        m.update(str.encode(string))
        val = int.from_bytes(m.digest(), 'big')
        print("Hash: {0}".format(val))
        return val

    def get_coords_as_array(self):
        return np.array( [self.x, self.y, self.z] )

    def set_coords_from_array(self, array):
        self.x, self.y, self.z = array

    def add_vector(self, vector):
        self.set_coords_from_array( np.add( self.get_coords_as_array(), vector) )
