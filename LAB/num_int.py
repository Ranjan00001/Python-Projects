def num_ints(lst):
	'''
	returns the number of all integers in lst

	parameter lst: list given to operate
	precondition : lst is list 
	'''
	count=0
	for x in lst:
		count=count+1 if type(x)==int else count
	return count
	
print(num_ints([1,2,3,1.2,'ae']))		


