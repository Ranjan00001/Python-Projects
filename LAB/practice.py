def celcius_to_fahrent(n):
	'''
	changes and prints input temp (in celcius) to fahrenheit

	parameter n: temp in celcius given to check
	precondition: n should be float

	>>> celcius_to_fahret(0.0)
	32.0 ; weather is cold
	>>> celcius_to_fahret(-40.0)
	-40.0 ; weather is cold
	>>> celcius_to_fahret(100.0)
	212.0 ; weather is hot
	>>> celcius_to_fahret(25.0)
	77.0 ; weather is nice

	'''
	n=float(input('enter temp in celcius: '))
	result = (9*n)/5+32  # formula used is (9c/5=f-32)

	if result < 60:      # case when result is less than 60
		print( result,'; weather is cold')	
	elif result <= 85:   # case when result is between 60 and 85
		print( result,'; weather is nice')	
	else:                # case when result is greater than 85
		print( result,'; weather is hot')	

if __name__ == '__main__':
	import doctest
	doctest.testmod()
	celcius_to_fahrent(5)
