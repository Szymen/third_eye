import Point
import numpy as np

def get_rotation_matrix(angle_x, angle_y, angle_z ):
    sin_x = np.sin(angle_x * (np.pi / 180))
    cos_x = np.cos(angle_x * (np.pi / 180))

    sin_y = np.sin(angle_y * (np.pi / 180))
    cos_y = np.cos(angle_y * (np.pi / 180))

    sin_z = np.sin(angle_z * (np.pi / 180))
    cos_z = np.cos(angle_z * (np.pi / 180))

    rx = np.array([
        [1.0, 0.0, 0.0],
        [0.0, cos_x, -sin_x],
        [0.0, sin_x, cos_x],
    ])

    ry = np.array([
        [cos_y, 0.0, sin_y],
        [0.0, 1.0, 0.0],
        [-sin_y, 0.0, cos_y],
        ])

    rz = np.array([
        [cos_z, -sin_z, 0.0],
        [sin_z, cos_z, 0.0],
        [0.0, 0.0, 1.0],
    ])
    return np.matmul(np.matmul(rx, ry), rz)


def split_walls( wall_list ):

    new_wall_list = []
    
    for wall_item in wall_list:
        pointA = wall_item[0]
        pointB = wall_item[1]
        pointC = wall_item[2]
        pointD = wall_item[3]

        point_one = Point.Point(
            (pointA.x + pointB.x) / 2,
            (pointA.y + pointB.y) / 2,
            (pointA.z + pointB.z) / 2
        )

        point_two = Point.Point(
            (pointB.x + pointC.x) / 2,
            (pointB.y + pointC.y) / 2,
            (pointB.z + pointC.z) / 2
        )

        point_three = Point.Point(
            (pointD.x + pointC.x) / 2,
            (pointD.y + pointC.y) / 2,
            (pointD.z + pointC.z) / 2
        )

        point_four = Point.Point(
            (pointD.x + pointA.x) / 2,
            (pointD.y + pointA.y) / 2,
            (pointD.z + pointA.z) / 2
        )

        point_five = Point.Point(
            (pointA.x + pointB.x + pointC.x + pointD.x) / 4,
            (pointA.y + pointB.y + pointC.y + pointD.y) / 4,
            (pointA.z + pointB.z + pointC.z + pointD.z) / 4
        )
        print("pointA: {0}".format(pointA))
        print("pointB: {0}".format(pointB))
        print("pointC: {0}".format(pointC))
        print("pointD: {0}".format(pointD))
        print("point_one: {0}".format(point_one))
        print("point_two: {0}".format(point_two))
        print("point_three:{0}".format(point_three))
        print("point_four: {0}".format(point_four))
        print("point_five: {0}".format(point_five))
        # tmp = 
        new_wall_list.append( (pointA,        point_one,  point_five,     point_four  )) # I
        new_wall_list.append( (point_one,     pointB,     point_two,      point_five  )) # II
        new_wall_list.append( (point_two,     pointC,     point_three,    point_five )) # III
        new_wall_list.append( (point_three,   pointD,     point_four,     point_five  )) # IV
        

    # print("in function")
    # for x in new_wall_list:
    #     print("{0}".format(x))

    
    return new_wall_list.copy()
