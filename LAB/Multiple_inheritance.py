class Length(object):
	"""docstring for Length"""

	@property
	def lent(self):
		return self._lent
	
	@lent.setter
	def lent(self, value):
		assert isinstance(value, float) or isinstance(value, int), repr(value) + 'is not valid'
		self._lent = value

	def __init__(self, a):
		self.lent = a
		# super().__init__()

class Breadth(object):
	"""docstring for Breadth"""

	@property
	def bread(self):
		return self._bread
	
	@bread.setter
	def bread(self, value):
		assert isinstance(value, float) or isinstance(value, int), repr(value) + 'is not valid'
		assert value >= 0, repr(value)+ ' is invalid'
		self._bread = value

	def __init__(self, a):
		self.bread = a
		
class Rectangle(Length, Breadth):
	"""docstring for Rect_area"""

	def __init__(self, l, b):
		# Length.__init__(self, l)
		# Breadth.__init__(self, b)
		super().__init__(l)
		super(Length, self).__init__(b)

	def r_area(self):
		return self.lent * self.bread

a = Rectangle(2,3)
print(a.r_area())

# print(Length.mro())
