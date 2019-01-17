import ObjectList
from Line import Line
from Cube import Cube
from Point import Point 


class objectCreator():


	def __init__(self):
		pass


	def case_one(self, objectListToAdd):
		# adds:
		#  one cube 
		#  one line

		# cube
		objectListToAdd.add_new_object(
			Cube(
				Point( 15,  15,  15 ),	    # 1.
 				Point( 100, 15,  15 ),	    # 2.	
				Point( 100, 100, 15 ),	    # 3.
				Point( 15,  100, 15 ), 		# 4.
				Point( 15,  15,  100),		# 5.
				Point( 100, 15,  100),	    # 6.
				Point( 100, 100, 100),	    # 7.
				Point( 15,  100, 100)		# 8.
				)
		)
  

		# line
		objectListToAdd.add_new_object(
			Line(
				Point( 200, 200, 5 ), 
				Point( 350, 350, 100 )
			)
		)


	def case_two(self, objectListToAdd):
			# adds:
			#  one cube
			#  one line
	
			# cube
			objectListToAdd.add_new_object(
				Cube(
					Point(15,  15,  15),	    # 1.
	 				Point(100, 15,  15),	    # 2.
					Point(100, 100, 15),	    # 3.
					Point(15,  100, 15), 		# 4.
					Point(30,  30,  100),		# 5.
					Point(115, 30,  100),	    # 6.
					Point(115, 115, 100),	    # 7.
					Point(30,  115, 100)		# 8.
	                        )
			)
	
			# line
			objectListToAdd.add_new_object(
				Line(
					Point(200, 200, 5),
					Point(350, 350, 100)
				)
			)
