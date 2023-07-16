def grade(m):
	'''
	CONVERTS score to grade

	score given should be less than 100.at the difference of 10 marks grades
	are being changed. here 'F' stands for fail.

	>>> grade(90)
	B
	>>> grade(91)
	A
	>>> grade(50)
	E
	>>> grade(39)
	F
	
	'''
	if m > 90 :
		print('A')
	elif m >= 80 :
		print('B')	
	elif m >= 70 :
		print('C')
	elif m >= 60 :
		print('D')
	elif m >= 50 :
		print('E')
	elif m >= 40 :
		print('E-')
	else:
		print('F')

grade(39)				