class Person:
	def __init__(self, a, b, c, d):
		self.name = a
		self.age = b
		self.gender = c
		self.adhar = d

	def __str__(self):
		return '('+str(self.name)+','+str(self.age)+','+str(self.gender)+','+str(self.adhar)+','+')'

	def __repr__(self):
		return str(self.__class__)+str(self)


class Vehicle:
	def __init__(self, a, b, c):
		self.brand = a
		self.model = b
		self.type = c

	def __str__(self):
		return '('+str(self.brand)+','+str(self.model)+','+str(self.type)+','+')'

	def __repr__(self):
		return str(self.__class__)+str(self)


class Dog:
	def __init__(self, a, b, c, d):
		self.name = a
		self.breed = b
		self.age = c
		self.color = d

	def __str__(self):
		return '('+str(self.name)+','+str(self.breed)+','+str(self.age)+','+str(self.color)+','+')'

	def __repr__(self):
		return str(self.__class__)+str(self)

