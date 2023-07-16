def fibonacci(n):
	'''
	returns fibonacci sequence till n

	fibonacci seq is seq of numbers in which
	first two elements are 0 & 1 and next
	members are obtained by adding previous two

	parameter n: number of elements in fibonacci seq we want
	precondition: n is a int and n>1 

	examples:
	>>> fibonacci(3)
	[0, 1, 1]
	>>> fibonacci(10)
	[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
	>>> fibonacci(5)
	[0, 1, 1, 2, 3]
	'''
	series=[0,1]
	for x in range(n-2):
		for y in range(x+1,x+2):
			series=series+[series[x]+series[y]]
			# series.append(series[x]+series[y])
	return series
print(fibonacci(5))

def nth_fibonacci(n):
	'''
	returns nth number of fibonacci sequence
	'''
	lst=fibonacci(n)
	return lst[n-1]
print(nth_fibonacci(5))

