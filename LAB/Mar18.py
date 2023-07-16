# def main():
# 	try:
# 		val = input()
# 		x = float(val)
# 		print('the next number is '+str(x+1))
# 		assert x<10, 'out of range'
# 	except ValueError:          # yaha type check karne ke liye isinstance ka use ho raha hai
# 		print('that"s not a number')
# 	except AssertionError:
# 		print('out of bound')

# if __name__ == '__main__':
# 	main()


# def foo(x):

# 	# assert type(x) == int, 'not an int'
# 	if type(x) != int:
# 		raise AssertionError('not an int')

# 	# assert x < 2, 'out of range'
# 	if x >= 2:
# 		raise AssertionError('not an int')
	
# 	return x+1

# foo(4)


class Student(object):
	"""docstring for Student"""

	__count = 0
	def __init__(self, arg):
		self.arg = arg
		Student.__count+=1

	def Display(self):
		print(Student.__count)

s= Student(123)
s.Display()