import Point


class Line:


    def __init__(self, pointA, pointB):
        self.pointA = pointA
        self.pointB = pointB

    # def __init__(self, xa, ya, za, xb, yb, zb):
    #     self.pointA = Point.Point(xa, ya, za)
    #     self.pointB = Point.Point(xb, yb, zb)

    def get_edges(self):
        return [(self.pointA, self.pointB)]