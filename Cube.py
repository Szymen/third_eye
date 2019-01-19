import Point


#     8._______.7
#     /|      / |
#  4./_|_____/.3|
#   |5.|_____|__|. 6
#   |  /     | /
#   | /      |/
# 1.|________|.2


class Cube:

    def __init__(self, pointA, pointB, pointC, pointD, pointE, pointF, pointG, pointH):
        self.one   = pointA
        self.two   = pointB
        self.three = pointC
        self.four  = pointD
        self.five  = pointE
        self.six   = pointF
        self.seven = pointG
        self.eight = pointH

    # def __init__(self, xa, ya, za, xb, yb, zb, xc, yc, zc, xd, yd, zd, xe, ye, ze, xf, yf, zf, xg , yg, zg, xh, yh, zh):
    #     self.one   = Point.Point(xa, ya, za)
    #     self.two   = Point.Point(xb, yb, zb)
    #     self.three = Point.Point(xc, yc, zc)
    #     self.four  = Point.Point(xd, yd, zd)
    #     self.five  = Point.Point(xe, ye, ze)
    #     self.six   = Point.Point(xf, yf, zf)
    #     self.seven = Point.Point(xg, yg, zg)
    #     self.eight = Point.Point(xh, yh, zh)

    def get_edges(self):
        return [
            (self.one, self.two),
            (self.two ,self.three ),
            (self.three, self.four),
            (self.four, self.one),
            (self.four, self.eight),
            (self.three, self.seven),
            (self.two, self.six),
            (self.one, self.five),
            (self.five, self.six),
            (self.six, self.seven),
            (self.seven, self.eight),
            (self.eight, self.five)
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