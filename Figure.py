import Edge
import numpy as np


class Figure:

    edges = []
    walls = []

    def __init__(self, edges):
        self.edges = edges

    def __str__(self):
        tmp = "{0}\n".format(self.__class__.__name__)
        for x in self.edges:
            tmp += x.__str__()+"\n"
        return tmp

    def get_edges(self):
        return self.edges

    def add_vector(self, vector):
        vector = np.array(vector)
        self.edges = [ edge_item + vector for edge_item in self.edges] 

    def multiply_by_matrix(self, matrix):
        self.edges = [ edge_item * matrix for edge_item in self.edges]


    def print_edges(self):
        for edge_item in self.edges:
            print("[FIGURE]_print_edges: {0}".format(edge_item))


    def get_walls(self):
        return self.walls

