def find_chronology(time1, suffix1, time2, suffix2):
	'''
	shows us order of time

	Time in first two parameter is taken 1st event and 
	other two are taken as second events.
	if we give some input time in argument then it will 
	show us about that which of them will come previous 
	than other.

	>>> find_chronology(1,'pm',2,'pm')
	before
	>>> find_chronology(3,'am',2,'pm')
	before
	>>> find_chronology(2,'pm',2,'pm')
	same
	>>> find_chronology(3,'am',2,'am')
	after
	>>> find_chronology(2,'pm',2,'am')
	after

	parameter time1 :it requires time which i have to decide 
	precondition : it should be +ve int number


	parameter suffix1 :it requires suffix of time which i have to decide 
	precondition :it can be 'am' or 'pm'


	parameter time2 :it requires time which i have to decide 
	precondition : it should be +ve int number


	parameter time1 :it requires suffix of time which i have to decide 
	precondition :it can be 'am' or 'pm'

	'''
	if suffix1==suffix2:
		if time1>time2:
			print('after')
		if time1<time2:
			print('before')
		elif time1==time2:
			print('same')
	elif suffix1=='am':
		print('before')
	else:
		print('after')

if __name__ == '__main__':
	import doctest
	doctest.testmod()

 	
