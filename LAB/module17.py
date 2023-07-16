import sys
sys.setrecursionlimit(100)
def factorial(n):
	assert type(n) == int ,str(n)+'is not an integer'
	assert n >= 0 ,sr(n)+'is a negative'
	# if n==0:
	# 	return 1
	return n*factorial(n-1)

print(factorial(1))


def fibonacci(n):
	if n<=1:
		return 1
	return fibonacci(n-1)+fibonacci(n-2)
	
		
def num_es(s):
	assert type(s) == str, repr(s)+'is not str'
	if s == '':
		return 0
	elif len(s) == 1:
		return 1 if s == 'e' else 0

	left = num_es(s[0])
	right = num_es(s[1:])
	return left+right


def deblank(s):
	if s == '':
		return s      # yaha kuch galat ho sakta hai please be careful
	elif len(s) == 1:
		return '' if s == ' ' else s

	left = deblank(s[0])
	right = deblank(s[1:])
	return left+right
	

print(deblank('sag b'))



def commafy(s):
	if s == '':
		return s
	if len(s) == 3:
		return ','+'s'

	right = commafy(s[-1:-4:-1])
	left = commafy(s[-4::-1])
	return left+','+right



def commafy1(s):
	if len(s) < 3:
		return s

	left = commafy(s[:-3])
	right = s[-3:]
	return left+','+right

