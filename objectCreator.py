import ObjectList
from Line import Line
from Cube import Cube
from Point import Point


class objectCreator():

    def __init__(self):
        pass

    def case_one(self, objectListToAdd):
        # adds:
        #  one cube
        #  one line

        # cube
        objectListToAdd.add_new_object(
            Cube(
                Point(15, 15, 15),  # 1.
                Point(30, 15, 15),  # 2.
                Point(30, 30, 15),  # 3.
                Point(15, 30, 15),  # 4.
                Point(15, 15, 30),  # 5.
                Point(30, 15, 30),  # 6.
                Point(30, 30, 30),  # 7.
                Point(15, 30, 30)  # 8.
            )
        )

        # # line
        # objectListToAdd.add_new_object(
        #     Line(
        #         Point(200, 200, 5),
        #         Point(350, 350, 100)
        #     )
        # )

    def case_two(self, objectListToAdd):
        # adds:
        #  one cube
        #  one line

        # cube
        objectListToAdd.add_new_object(
            Cube(  # x     y    z
                Point(15, 15, 15),  # 1.
                Point(30, 15, 15),  # 2.
                Point(30, 30, 15),  # 3.
                Point(15, 30, 15),  # 4.
                Point(15, 15, 30),  # 5.
                Point(30, 15, 30),  # 6.
                Point(30, 30, 30),  # 7.
                Point(15, 30, 30)   # 8.
            )
        )
        objectListToAdd.add_new_object(
            Cube(  # x     y    z
                Point(-15, 15, 15),  # 1.
                Point(-30, 15, 15),  # 2.
                Point(-30, 30, 15),  # 3.
                Point(-15, 30, 15),  # 4.
                Point(-15, 15, 30),  # 5.
                Point(-30, 15, 30),  # 6.
                Point(-30, 30, 30),  # 7.
                Point(-15, 30, 30)   # 8.
            )
        )
        objectListToAdd.add_new_object(
            Cube(  # x     y    z
                Point(89, 15, 15),  # 1.
                Point(74, 15, 15),  # 2.
                Point(74, 30, 15),  # 3.
                Point(89, 30, 15),  # 4.
                Point(89, 15, 30),  # 5.
                Point(74, 15, 30),  # 6.
                Point(74, 30, 30),  # 7.
                Point(89, 30, 30)   # 8.
            )
        )
        objectListToAdd.add_new_object(
            Line(
                Point(10, 100, 0),
                Point(-100, 100, 6)
            )

        )
