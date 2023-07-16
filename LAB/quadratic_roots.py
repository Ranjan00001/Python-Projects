def roots(a,b,c):

	'''it is used for finding roots of quadratic equation
	user need to give the value of different coefficient
	a,b,c are such that roots are real'''
	root_1 = (-b+(b**2-4*a*c)**1/2)/2*a  
	root_2 = (-b-(b**2-4*a*c)**1/2)/2*a
	print(roots_1,roots_2)
	 
roots(1,5,6)
