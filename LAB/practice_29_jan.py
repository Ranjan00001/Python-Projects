
# def helper(table):
# 	'''
# 	'''

# 	result = []
# 	for i in table:
# 		for j in i:
# 			if type(j) in [int,float]:
# 				result.append(True)
# 			else:
# 				result.append(False)
# 	return result		

# a=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
# print(helper(a))				
# # print(result)
# def all_nums1(table):
# 	if False in helper(a):
# 		return False
# 	else:
# 		return True

# print(all_nums1(a))			


# def all_nums(table):
# 	                                            # result=True
# 	for i in table:
# 		for j in i:
# 			if not type(j) in [int,float]:
# 				return False                    #result = False
# 	return True                                 #return result

# print(all_nums(a))


# def transpose1(table):
# 	for i in table:
# 		for j in i:
# 			table[i][j] = table[j][i]

def transpose(table):
	'''
	returns copy of table with rows and columns swapped

	precondition: table is a non-ragged list
	parameter table: table given to transpose
	'''
	p=[]
	#q=[]
	for i in range(len(table[0])):
		q=[]
		for j in range(len(table)):
			q.append(table[j][i])
		p.append(q)
		#q=[]	
	return p

a=[[1,2,3],[4,5,6],[7,8,9],[10,11,13]]
print(transpose(a))

# def add_ones(table):
# 	for i in range(len(table)):
# 		for j in table[i]:
# 			i[j] = j+1
# 			print(j)
# 	print(table)
	
# add_ones(a)


# def strip(table,col):
# 	for i in transpose(table):
# 		table[i].remove(i[col])
# 	print(table)
	
# strip(a,1)

# d1={'a':1,'b':2}
# d2={'b':2}
# # d1+d2
# print(d1.values())
# print(d1)
# print(type(d1.values()))


# def max_grades(grades):
# 	l=0
# 	for i in grades:
# 		if grades[i]>l:
# 			 l=grades[i]
# 	return l
	
# def roll_no_above_cutoff(grades,cutoff):
# 	l=[]
# 	for i in grades:
# 		if grades[i]>=cutoff:
# 			l.append(i)

# 	return l
# d1={'a':0,'b':2}
# print(roll_no_above_cutoff(d1,1))

# def give_extra_credit(grades,rolls,bonus):
# 	for i in grades:
# 		if i in rolls:
# 			grades[i]+=bonus
# 	print(grades)
	
# 			


# def falt(lst):

# 	lst=[lst[i][j] for i in range(len(lst)) for j in range(len(lst[i])) if len(lst[i][j])<=6]
# 	return lst

# print(falt([['mercury','venus','earth'],['mars','kirtanCa']]))
# acc = 0

# def list_sum1(lst) :
# 	# global acc
# 	acc = 0
# 	for i in range(len(lst)):
# 		# print(i)
# 		if type(lst[i]) != list :
# 			# print('after1',i,acc)
# 			acc += lst[i]
# 			# print('after', i, acc)

# 		else :
# 			# print('before',i,acc)
# 			acc += list_sum1(lst[i])
# 			# print('after',i,acc)
# 	return acc

# print(list_sum1([1, 2, 3, [4, 5, [7, [8]]], 6]))
# print(acc)


acc = 0
def list_sum(lst) :
	global acc
	for i in lst:
		# print(i)
		if type(i) != list :
			acc += i
		else :
			list_sum(i)
	return acc

print(list_sum([1, 2, 3, [4, 5, 6, [7, 8]]]))
# print(acc)


# lst = [1, 2, 3, [4],[6, 7]]
# result = []
# def flatten(lst):
# 	# global result
# 	for i in lst :
# 		if type(i) == list :
# 			flatten(i)
# 		else:
# 			result.append(i)	
# 	return result

# print(flatten(lst))


def power(a,b):
	if b == 0:
		return 1
	if b%2 == 0:
		return power(a*a,b//2)
	else:
		return 	a*power(a*a,(b-1)//2)	

print(power(2,4))

def power1(a,b):
	if b ==0:
		return 1
	return a*power1(a,b-1)

print(power1(2,4))

# def func():
# 	return [[i for i in range(4)] for i in range(4)]
# print(func())	