import numpy as np
import Point

class MasterObjectList():
    objectList = []

    def __init__(self):
        pass

    def get_all_objects(self):
        return self.objectList

    def add_new_object(self, object_to_add):
        self.objectList.append(object_to_add)

    def set_object_list(self, new_object_list):
        self.objectList = new_object_list

    def sum_on_all_objects(self, vector):
        print("Adding {0} on all objects".format(vector))
        # self.objectList = [np.add(x, vector) for x in self.objectList]

        for object_item in self.get_all_objects():
            for edge in object_item.get_edges():
                point_A = edge[0]
                point_B = edge[1]
