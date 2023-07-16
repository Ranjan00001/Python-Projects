

def is_valid_brackets(s):
	'''
	this function is used for checking that brackets are in right position i.e. balanced or not
	'''
	t = 0

	for i in s:
		if i == '(':
			t+=1
		elif i == ')':
			t = t-1

		if t != 0:
			return False
	return True

# import math
# class Point3(object):
# 	"""Class for points in 3d space
# 	Invariant: x is a float
# 	Invariant y is a float
# 	Invariant z is a float """

# 	def __init__(self,x,y,z):
# 		self.x = x
# 		self.y = y
# 		self.z = z

# 	def distance(self,q):
# 		"""Returns dist from self to q
# 		Precondition: q a Point3"""
# 		assert type(q) == Point3
# 		sqrdst = ((self.x-q.x)**2 +
# (self.y-q.y)**2 +
# 			(self.z-q.z)**2)
# 		return math.sqrt(sqrdst)

# p = Point3(1,1,1)
# q = Point3(1,3,0)
# print(p.distance(q))
# print(q.distance(p))