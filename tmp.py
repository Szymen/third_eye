
import Edge
import Point
import ObjectList
import objectCreator

import dead_kitten 
# e_list = [
#     Edge.Edge( Point.Point(1,1,1), Point.Point(3,1,1) ),
#     Edge.Edge( Point.Point(3,1,1), Point.Point(3,1,3) ),
#     Edge.Edge( Point.Point(3,1,3), Point.Point(1,1,3) ),
#     Edge.Edge( Point.Point(1,1,3), Point.Point(1,1,1) ),
#
#     Edge.Edge( Point.Point(1,1,1), Point.Point(3,1,1)  ),
#     Edge.Edge( Point.Point(3,1,1), Point.Point(3,3,1)  ),
#     Edge.Edge( Point.Point(3,3,1), Point.Point(1,3,1)  ),
#     Edge.Edge( Point.Point(1,3,1), Point.Point(1,1,1)  )
#     # Edge.Edge( Point.Point(), Point.Point()  ),
#     # Edge.Edge( Point.Point(), Point.Point()  ),
#     # Edge.Edge( Point.Point(), Point.Point()  ),
#     # Edge.Edge( Point.Point(), Point.Point()  ),
#     # Edge.Edge( Point.Point(), Point.Point()  ),
# ]
# wall_list = [
#         ( Point.Point(1, 3, 0),
#           Point.Point(3, 3, 0),
#           Point.Point(3, -1, 0),
#           Point.Point(1, -1, 0)
#         )
# ]

ol = ObjectList.MasterObjectList()

object_creator = objectCreator.objectCreator()
object_creator.case_one(ol) # case one has one line and one cube

wall_list = ol.get_all_objects()[0].get_walls()

wall_list = [wall_list[0]]


# print("Before({1}): {0} ".format(wall_list, len(wall_list)))
print("Before")
for x in wall_list:
    print("{0}, {1}, {2}, {3}".format(x[0], x[1], x[2], x[3]))

wall_list = dead_kitten.split_walls(wall_list)
# print("After({1}): {0}".format(wall_list, len(wall_list)))
print("After")
for x in wall_list:
    print("{0}, {1}, {2}, {3}".format(x[0], x[1], x[2], x[3]) )
