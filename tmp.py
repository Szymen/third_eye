

import Figure
import Edge
import Point
import numpy as np
import dead_kitten

edges = [
    Edge.Edge(
     Point.Point(2,3,4),
     Point.Point(1,2,3)
    )
]


a = Figure.Figure(edges)
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
foo = Edge.Edge(
     Point.Point(1,1,3),
     Point.Point(1,1,1)
    )
print("Before {0}".format(foo))
# foo = foo + ([1, 2, 3])
rot = dead_kitten.get_rotation_matrix(0,90,0)
foo = foo * rot
print("after: {0}".format(foo))
print(rot)



# a, b ,c = np.array([1,2,3])
# print("A: {0}".format(a))
# print("B: {0}".format(b))
# print("C: {0}".format(c))