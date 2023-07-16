def row_wise(lst):
	for i in lst:
		for j in i:
			print(j)		

a=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

row_wise(a)

def column_wise(lst):
	for i in range(len(lst[0])):         #range(len(lst[0])):
		for j in range(len(lst)):
			print(lst[j][i])

column_wise(a)

result=[]
def flatten(lst):
	global result
	for i in lst:
		if type(i) != list:
			result.append(i)
			# print(result)
		else:
			# print('else')
			flatten(i)                            #result.append(flatten(i))
	return result
b=[1,2,[3,4,[5,6]],7,8,[9,10]]
c=[3,4,[1,2]]
print(flatten(c))

