

import Figure
import Edge
import Point
import numpy as np
import dead_kitten
import Cube
from Point import Point

# a = np.array([1,2,3])
# a = a.transpose()
# m = np.matrix(a).transpose()
# print(a)
# print(m)

# exit(1)
# edges = [
#     Edge.Edge(
#      Point.Point(2,3,4),
#      Point.Point(1,2,3)
#     )
# ]


a = Cube.Cube(
    Point(15, 15, 15),  # 1.
    Point(30, 15, 15),  # 2.
    Point(30, 30, 15),  # 3.
    Point(15, 30, 15),  # 4.
    Point(15, 15, 30),  # 5.
    Point(30, 15, 30),  # 6.
    Point(30, 30, 30),  # 7.
    Point(15, 30, 30)   # 8.
)
# a.add_vector

# one = np.array([1,1,1])
# two = np.array([1,2,3])
# three = np.add(one, two)
# print("One {0}".format(one))
# print("two {0}".format(two))
# print("three {0}".format(three))

# a.print_edges()
# a.add_vector([1, 1, 1, 0])
# a.print_edges()

#
# foo = Edge.Edge(
#      Point.Point(1,1,3),
#      Point.Point(1,1,1)
#     )
print("Before {0}".format(a))
# foo = foo + ([1, 2, 3])
# rot = dead_kitten.get_rotation_matrix(0, 0, 90)
rot = [1,1,1]
# print("Rot matrix: {0}".format(rot))
a.add_vector(rot)
# a.multiply_by_matrix(rot)
print("after: {0}".format(a))
# print(rot)




# a, b ,c = np.array([1,2,3])
# print("A: {0}".format(a))
# print("B: {0}".format(b))
# print("C: {0}".format(c))