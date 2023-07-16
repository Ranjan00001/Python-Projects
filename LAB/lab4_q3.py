
# def sump(a=2,b):
# 	print(a+b)

# sump(3)
# # non-default argument follows default argument


# see these below two functions, it will give u idea about global variable
def funcl(n):
	x=n+1
	n=n+2
	return n
# here it has already carried global variables bcz it has parameter

n=3
print(funcl(n))
print(n)

def func():
	# global n
	x=n+1
	n=n+2
	print(n)
	print(x)
# here it is not identifying(carrying) global variables bcz it has no parameter
# so we need to use term global
n=3
func()