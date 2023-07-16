import point
def copy2d(p):
	'''
	returns a 2d copy of the point



	'''
	q=point.Point3(p.x,p.y,0)
	return q
q=point.Point3(1,2,3)
r=copy2d(q)
print(r)
print(r.x)
print(r.y)
print(r.z)

