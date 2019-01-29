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
            Edge.Edge(self.one, self.two),            # 0
            Edge.Edge(self.two ,self.three ),         # 1
            Edge.Edge(self.three, self.four),         # 2 
            Edge.Edge(self.four, self.one),           # 3
            Edge.Edge(self.four, self.eight),         # 4 
            Edge.Edge(self.three, self.seven),        # 5 
            Edge.Edge(self.two, self.six),            # 6
            Edge.Edge(self.one, self.five),           # 7
            Edge.Edge(self.five, self.six),           # 8
            Edge.Edge(self.six, self.seven),          # 9 
            Edge.Edge(self.seven, self.eight),        # 10 
            Edge.Edge(self.eight, self.five)          # 11 
        ]
        self.walls = [
            (self.one, self.two, self.three, self.four),
            (self.four, self.eight, self.seven, self.three),
            (self.eight, self.seven, self.six, self.five),
            (self.five, self.six, self.two, self.one),
            (self.one, self.five, self.eight, self.four),
            (self.two, self.six, self.seven, self.three)
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


    def get_walls(self):
        one  =  self.edges[0].pointA
        two  =  self.edges[0].pointB
        three=  self.edges[1].pointB
        four =  self.edges[3].pointA
        five =  self.edges[11].pointB
        six  =  self.edges[9].pointA
        seven=  self.edges[10].pointA
        eight=  self.edges[10].pointB
        return [
            (one, two, three, four),
            (two, six, seven, three),
            (six, five, eight, seven),
            (five, one, four, eight),
            (five, six, two, one),
            (four, three, seven, eight)
        ]
#     8._______.7
#     /|      / |
#  4./_|_____/.3|
#   |5.|_____|__|. 6
#   |  /     | /
#   | /      |/
# 1.|________|.2