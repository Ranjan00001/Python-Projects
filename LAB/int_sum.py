def sum_double(a,b):
	'''
	returns sum for differrent int and double of sum for same int

	parameter a : number to be added
	precondition: it should be int
	
	parameter b : number to be added
	precondition: it should be int
	
	>>> sum_double(1,2)
	3
	>>> sum_double(1,3)
	4
	>>> sum_double(3,3)
	12
	'''

	if a != b :
		return a+b
	else :
		return (a+b)*2	

print(sum_double(3,3))
