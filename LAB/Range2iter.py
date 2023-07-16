# class range2iter(object):

# 	"""docstring for range2iter"""

# 	@property
# 	def limit(self):
# 		return self._limit
# 	# @property
# 	# def pos(self):
# 	# 	return self._pos
	
# 	@limit.setter
# 	def limit(self, value):
# 		self._limit = value

# 	def __init__(self, a):
# 		self.limit = a
# 		self._pos = 0

# 	def __next__(self):
# 		if self.limit <= self._pos:
# 			raise StopIteration()

# 		else:
# 			value = self._pos**2
# 			self._pos += 1
# 		return value

# a = range2iter(4)    # iterator
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

def fibonacci(n):
    
	x = 0
	y = 1
	while x < n:
		yield x
		x, y = x + y, x

print(list(fibonacci(100)))

def combination(lst,k):
	'''
	Write a generator function in Python that generates all possible combinations of a given list of integers.
	Each combination should contain exactly k elements. For example, given the list [1, 2, 3, 4] and k = 2,
	the generator should yield the following combinations: (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4).
	Your task is to implement the generator function that generates these combinations.
	Hint: You may find it helpful to use recursion to generate the combinations.
	'''
	length = len(lst)
	for i in range(length):
		# print('hi')
		for j in range(i+1, length):
			yield [lst[i], lst[j]]

lst = [1,2,3,1]
print(list(combination(lst, 2)))