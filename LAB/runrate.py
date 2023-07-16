def runrate(r,o):
	'''
	calculates required run rate

	parameter r : runs remaining
	precondition: it should be int
	
	parameter o : overs remaining
	precondition: it should be float
	
	>>> runrate(12,2)
	6.0
	>>> runrate(15,2.3)
	6.000000000000002

	'''

	balls_remain = int(o)*6+(o-int(o))*10  # o*6
	runrate_per_ball = r/balls_remain
	runrate_per_over = runrate_per_ball*6
	return runrate_per_over
# if __name__ == '__main__':
# 	r=int(input('enter required runs: '))
# 	o=float(input('enter remaining overs: '))

print(runrate(12,2))

