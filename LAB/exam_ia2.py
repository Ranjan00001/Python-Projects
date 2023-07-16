# # tends to remove elements greater than or equal to 5

# def func(lst):
# 	for i in range(len(lst)):
# 		if lst[i] >= 5:
# 			lst.remove(lst[i])
# 	print(lst)
	
# a=[1,2,3,4,6]
# func(a)

# # ? iss question me list me jab do se jyada element remove karne honge to error ayega

import math
def find_composite(a,b):
	acc=[]
	for x in range(a,b+1):
		for y in range(1,math.ceil(b**0.5)):
			if x % y == 0:
				acc.append(x)
	return acc

print(find_composite(4,20))


def collapse(ragged):
	for x in ragged:
		ragged[ragged.index(x)] = math.fsum(x)/len(x)
	print(ragged)

b=[[1,2,3],[4,55,7],[1,7]]
collapse(b)


def countFrontBackMatches(s):
	count = 0
	for x in range(len(s)//2):
		if s[x] == s[-1-x]:
			count += 1
	return count
	
c='abcdcab'
print(countFrontBackMatches(c))

def sumfold(lst):
	for x in lst:                            # for x in range(len(lst)):
		if lst.index(x) != 0:                # if x != 0:
			lst[lst.index(x)] = lst[x]+lst[x-1]
	print(lst)

a=[1,2,3,4,6]
sumfold(a)			

