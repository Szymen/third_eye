import Edge
import numpy as np


class Figure:

    edges = []

    def __init__(self, edges):
        self.edges = edges

    def add_vector(self, vector):
        vector = np.array(vector)
        return Figure( [ np.add(edge_item, vector) for edge_item in self.edges] )

    def multiply_by_vector(self, vector):
        vector = np.array(vector)
        self.edges = [ np.multiply(edge_item, vector) for edge_item in self.edges]

    def print_edges(self):
        for edge_item in self.edges:
            print("[FIGURE]_print_edges: {0}".format(edge_item))