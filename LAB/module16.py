def main1(s):
	try:
		x=float(s)
		return True
	except:
		return False		

	# try:
	# 	result = input('number: ')
	# 	x= float(result)
	# 	print('the next number is'+str(x+1))
	# except:
	# 	print('this is not a number')	
	
	# result = input('number: ')
	# x = float(result)
	# print('the next number is'+str(x+1))

if __name__ == '__main__':
	print(main1('e-2'))


def function1(x,y):
	try:
		return function2(x,y)
	except:
		return float('inf')	
def function2(x,y):
	try:
		return function3(x,y)
	except:
		return float('inf')
	# return function3(x,y)
def function3(x,y):
	return (x/y)

if __name__ == '__main__':
	function1(1,0)


def first(x):
	print('starting first.')
	try:
		second(x)
	except:
		print('caught at first')
	print('ending first')
	
def second(x):
	print('starting second')
	third(x)
	print('ending second')

def third(x):
	print('starting third')
	assert x<1
	print('ending third')	
first(2)

