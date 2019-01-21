# from PIL import Image, ImageDraw

# # PIL.Image
# im = Image.open("Stage0.gif")
# draw = ImageDraw.Draw(im)
# draw.polygon(((0,100),(15,120),(120,130),(100,50),(75,10)), fill=(130,255,255))


# im.save("proba.gif", format='png' )

import Edge
import Point

e_list = [
    Edge.Edge( Point.Point(1,1,1), Point.Point(3,1,1) ),
    Edge.Edge( Point.Point(3,1,1), Point.Point(3,1,3) ),
    Edge.Edge( Point.Point(3,1,3), Point.Point(1,1,3) ),
    Edge.Edge( Point.Point(1,1,3), Point.Point(1,1,1) ),
    
    Edge.Edge( Point.Point(1,1,1), Point.Point(3,1,1)  ),
    Edge.Edge( Point.Point(3,1,1), Point.Point(3,3,1)  ),
    Edge.Edge( Point.Point(3,3,1), Point.Point(1,3,1)  ),
    Edge.Edge( Point.Point(1,3,1), Point.Point(1,1,1)  )
    # Edge.Edge( Point.Point(), Point.Point()  ),
    # Edge.Edge( Point.Point(), Point.Point()  ),
    # Edge.Edge( Point.Point(), Point.Point()  ),
    # Edge.Edge( Point.Point(), Point.Point()  ),
    # Edge.Edge( Point.Point(), Point.Point()  ),
]



def check_presence(needle, haystack):
    for iter in haystack:
        if needle.x == iter.x and needle.y == iter.y and needle.z == iter.z:
            return True
    return False



def create_walls_from_edges(edges):
    print(edges)
    print("Przyszlo:")
    walls_list = []
    all_points = []


    for edge_item in edges:
        # print(edge_item)
        a = edge_item.pointA
        b = edge_item.pointB
        print("Processing {0}".format(a))
        if check_presence(a, all_points):
            print("WAS: There was already point {0} in all_points".format(a))
            for i in range(len (walls_list) ):
                if check_presence(a, walls_list[i]):
                    walls_list[i].append(b)
        else:
            print("ADD: There was no point {0} in all_points, adding".format(a))
            all_points.append(a)
            walls_list.append([a, b])
            print("Added new wall, added ")
            # print(all_points)

        print("Processing {0}".format(a))
        if check_presence(b, all_points):
            print("WAS: There was already point {0} in all_points".format(b))
            for i in range(len (walls_list) ):
                if check_presence(b, walls_list[i]):
                    walls_list[i].append(a)
        else:
            print("ADD: There was no point {0} in all_points, adding".format(b))
            all_points.append(b)
            walls_list.append([b, a])
            print("Added new wall, added ")
            # print(all_points)

    return walls_list


foo = create_walls_from_edges(e_list)

master_set = []

for wall in foo:
    # print("New wall:")
    tmp = set()
    for pnt in wall:
        tmp.add(pnt)
        # print(">>{0}".format(pnt))
    master_set.append(tmp)


for wall in master_set:
    print("New wall:")
    for pnt in wall:
        print(">>{0}".format(pnt))
    
