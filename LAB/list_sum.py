def sum(lst):
	'''
	returns the sum of all elements in lst

	parameter lst : list given to operate
	'''

	# crate variable to hold result(starts at 0)
	result=0
	# add each list variable to result
	for x in lst:
		result+=x
	# return the variable
	return result
print(sum([1,2,3]))

