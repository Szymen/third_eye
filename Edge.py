import Point


class Edge:

    pointA = None
    pointB = None

    def __init__(self, pointA, pointB):
        self.pointA = pointA
        self.pointB = pointB


    def __str__(self):
        return "Edge {0} -- {1}".format(self.pointA, self.pointB)


    def __add__(self, vector_to_add):
        return Edge(
            self.pointA + vector_to_add,
            self.pointB + vector_to_add
        )

    def __mul__(self, vector_to_mult):
        return Edge(
            self.pointA * vector_to_mult,
            self.pointB * vector_to_mult
        )