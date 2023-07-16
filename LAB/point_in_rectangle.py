import point
x=float(input('enter  x-coordinate: '))
y=float(input('enter  y-coordinate: '))
def interior(x,y):
	'''
	'''
	x1=float(input('enter 1st x-coordinate: '))
	y1=float(input('enter 1st y-coordinate: '))
	x2=float(input('enter 2nd x-coordinate: '))
	y2=float(input('enter 2nd y-coordinate: '))
	x3=float(input('enter 3rd x-coordinate: '))
	y3=float(input('enter 3rd y-coordinate: '))
	x4=float(input('enter 4th x-coordinate: '))
	y4=float(input('enter 4th y-coordinate: '))
	
	# if y2-y1==(y4-y3)/(x4-x3)*(x2-x1) and y4-y3==(y2-y1)/(x2-x1)*(x4-x3) and x2-x1==x4-x3 and y2-y1==y4-y3:
	# x4-x3=(x4-x3) if (x4-x3)!=0 else 1 
	if (y4-y3)/(x4-x3)*(y3-y2)/(x3-x2)==-1 and (x2-x1)**2+(y2-y1)**2==(x4-x3)**2+(y4-y3)**2 and (x2-x3)**2+(y2-y3)**2==(x4-x1)**2+(y4-y1)**2:
		if (((y-y1)-((y4-y3)/(x4-x3)*(x-x1)))*((y-y2)-((y4-y1)/(x4-x1)*(x-x2))))<=0 and ((y-y3)-((y2-y1)/(x2-x1)*(x-x3)))*((y-y4)-((y2-y3)/(x2-x3)*(x-x4)))<=0:
			print('Inside')
		else:
			print('outside')
	else:
		print('Rect not forming')
# 	if x2>x1:
# 			return x2>=x>=x1
# 		if x1>x2:
# 			return x1>=x>=x2
# 		if x4>x3:
# 			return x4>=x>=x3
# 		if x3>x4:
# 			return x3>=x>=x4		
# 	coord_1=point.Point3(x1,y1,0)
# 	coord_2=point.Point3(x2,y2,0)
# 	coord_3=point.Point3(x3,y3,0)
# 	coord_4=point.Point3(x4,y4,0)
# if __name__ == '__main__':
# 	x1=5
# 	y1=0
# 	x2=0
# 	y2=5
# 	x3=-5
# 	y3=0
	# x4=0
	# y4=-5
	# print(interior(0,0))
	# print(interior(1,2))
	# print(interior(3,0))
	# print(interior(-2,0))
	# print(interior(0,-2))

interior(x,y)