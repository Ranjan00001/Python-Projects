# x1=float(input('enter 1st x-coordinate: '))
# y1=float(input('enter 1st y-coordinate: '))
# x2=float(input('enter 2nd x-coordinate: '))
# y2=float(input('enter 2nd y-coordinate: '))
# x3=float(input('enter 3rd x-coordinate: '))
# y3=float(input('enter 3rd y-coordinate: '))
# x4=float(input('enter 4th x-coordinate: '))
# y4=float(input('enter 4th y-coordinate: '))

def is_rectangle():
	slope_check=(y4-y3)/(x4-x3)*(y3-y2)/(x3-x2)==-1
	dist1=(x2-x1)**2+(y2-y1)**2==(x4-x3)**2+(y4-y3)**2
	dist2=(x2-x3)**2+(y2-y3)**2==(x4-x1)**2+(y4-y1)**2
	return slope_check and dist1 and dist2

def triangle_area(a,b,c):
	s=(a+b+c)/2
	return (s*(s-a)*(s-b)*(s-c))**0.5

# print(triangle_area(3,4,5))

def distance(a1,b1,a2,b2):
	return ((a1-a2)**2+(b1-b2)**2)**0.5


def inside_rectangle():
	x=float(input('enter x-coordinate: '))
	y=float(input('enter y-coordinate: '))
	a=distance(x,y,x1,y1)
	if is_rectangle():
		if triangle_area()
