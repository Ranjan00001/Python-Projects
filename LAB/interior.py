# # it need to be revised
# # not correct
# import point
# def isinterior(p):
# 	'''

# 	'''

# 	x1=float(input('enter 1st x-coordinate: '))
# 	y1=float(input('enter 1st y-coordinate: '))
# 	z1=float(input('enter 1st z-coordinate: '))
# 	x2=float(input('enter 2nd x-coordinate: '))
# 	y2=float(input('enter 2nd y-coordinate: '))
# 	z2=float(input('enter 2nd z-coordinate: '))
# 	# d1=point.Point3(float(x1),float(y1),float(z1))
# 	# d2=point.Point3(float(x2),float(y2),float(z2))
# 	# dist=d1.distance(d2)
# 	# dist1=p.distance(d1)
# 	# dist2=p.distance(d2)
# 	A=(x1<=p.x<=x2 if x1<=x2 else x1>=p.x>=x2)
# 	B=(y1<=p.y<=x2 if y1<=y2 else y1>=p.y>=y2)
# 	C=(z1<=p.z<=z2 if z1<=z2 else z1>=p.z>=z2)
# 	if A and B and C:
# 		print('inside')
# 	else:
# 		print('outside')
# # p=point.Point3(2,2,2)
# # print(isinterior(p))
# if __name__ == '__main__':
# 	p=point.Point3(2,2,2)
# 	isinterior(p)



# print(len(str(130.59)))
# print(len(str(round(130.59,1))))
# print(round(130.59,1))


# 1. Levels of facts and truth may vary it depends on type of arguments.

# 2. In Maths we only concern about truth not facts.

# 3. This gives the one of definition of mathematics: imagination which can be written and presented formally.

def func():
	l = float(input())
	if l != -1:
		m = l
	else:
		return 'your first input is -1'

	while l!= -1:  #True:
		n = float(input())
		if n != -1:
			if n > m:
				m = n
		else:
			return m

print(func())

