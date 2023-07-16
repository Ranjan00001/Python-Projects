def triangle_star(n):
	for x in range(n):
		print(' '*(n-x)+'*'*(2*x+1)+' '*(n-x))

def trapezium_star(n):
	for x in range(n):
		print(' '*(n-x)+'*'*(2*x+2*n-1)+' '*(n-x))

def rectangle_star(n):
	for x in range(6):
		print(' '*n+'*'*3)

def christmas_tree(b):
	a=2*b-1
	triangle_star(a)
	trapezium_star(b)
	trapezium_star(b)
	rectangle_star(a)

christmas_tree(5)
