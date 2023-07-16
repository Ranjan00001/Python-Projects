# mutable function
def add_one(lst):
	for x in range(len(lst)):
		lst[x]=lst[x]+1
	print(lst)
c=[1,2,3]
add_one(c)