import Point
import Figure
import Edge

class Line(Figure.Figure):


    def __init__(self, pointA, pointB):
        self.pointA = pointA
        self.pointB = pointB
        self.edges = [Edge.Edge(self.pointA, self.pointB)]

    def __str__(self):
        return self.edges[0].__str__()

