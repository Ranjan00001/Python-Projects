class A(object):
	"""docstring for A"""
	def __init__(self):
		self.a = 'old'
		self.change(self.a)

	def change(self,value):
		value='new'

class B(A):
	"""docstring for A"""
	def __init__(self):
		# super().__init__()
		A.__init__(self)
		self.y = 2

# o = B()
# print(o.x,o.y)

obj= A()
# print(obj.a) 

# new Question
class A:
	def __init__(self):
		self.a='a'

	def Display(self):
		print(self.a)

# class B(A):
# 	def __init__(self):
# 		self.b='b'

# obj= B()
# # print(obj.a)
# obj.Display()

class A(object):
	"""docstring for A"""
	def __init__(self):
		self.a = 5
		self._b = 10
		self.__c = 15

	def public_Display(self):
		print(self.a)
		print(self._b)
		print(self.__c)

	def _protected_Display(self):
		print(self.a)
		print(self._b)
		print(self.__c)

	def __private_Display(self):
		print(self.a)
		print(self._b)
		print(self.__c)

	def func(self):
		self.__private_Display()

class B(A):
	def func(self):
		self.__private_Display()

x = A()
y = B()

x.__c=1
print(x.__c)
# print(x.a)
# print(x._b)
# print(x.__c)

# print(y.a)
# print(y._b)
# print(x.__c)

# x.public_Display()
# y.public_Display()

# x.+_protected_Display()  # lawful
# y._protected_Display()   # unlawful

# x.__private_Display()   # error
# y.__private_Display()     # error

x.func()
# y.func()
