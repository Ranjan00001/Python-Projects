# slicing is a method

def reverse_list(lst):
	# lst = lst[::-1]
	for x in range(len(lst)):
		# lst[x] = lst[-1-x]
		lst.insert(x, lst[-1-x])
	for y in range(-len(lst)//2, 0): 
		lst.pop(y)    #print
	# print(id(lst))	
	return lst

a=[1,2,3,4,5,6]	
print(reverse_list(a))	
	
# print(id(a))


