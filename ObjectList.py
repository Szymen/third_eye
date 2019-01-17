



class MasterObjectList():	
	objectList = []


	def __init__(self):
		pass

	def get_all_objects(self):
		return self.objectList

	def add_new_object(self, object_to_add):
		self.objectList.append(object_to_add)
	