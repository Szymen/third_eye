import Point
import Figure
import Edge

#     8._______.7
#     /|      / |
#  4./_|_____/.3|
#   |5.|_____|__|. 6
#   |  /     | /
#   | /      |/
# 1.|________|.2


class Cube(Figure.Figure):

    def __init__(self, pointA, pointB, pointC, pointD, pointE, pointF, pointG, pointH):
        self.one   = pointA
        self.two   = pointB
        self.three = pointC
        self.four  = pointD
        self.five  = pointE
        self.six   = pointF
        self.seven = pointG
        self.eight = pointH
        self.edges =  [
            Edge.Edge(self.one, self.two),
            Edge.Edge(self.two ,self.three ),
            Edge.Edge(self.three, self.four),
            Edge.Edge(self.four, self.one),
            Edge.Edge(self.four, self.eight),
            Edge.Edge(self.three, self.seven),
            Edge.Edge(self.two, self.six),
            Edge.Edge(self.one, self.five),
            Edge.Edge(self.five, self.six),
            Edge.Edge(self.six, self.seven),
            Edge.Edge(self.seven, self.eight),
            Edge.Edge(self.eight, self.five)
        ]

    def get_points(self):
        return [
            self.one  ,
            self.two  ,
            self.three,
            self.four ,
            self.five ,
            self.six  ,
            self.seven,
            self.eight
            ]

    def set_points(self, pointArray):
        self.one, self.two, self.three, self.four, self.five, self.six, self.seven, self.eight = pointArray