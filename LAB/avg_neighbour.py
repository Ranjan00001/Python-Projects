# Given a list of integers, replace each element with the average of its neighbours
# If any item is at the beginning or end, the average is the value of a single neighbour
# You may assume there at least 2 elements in the given list 
# Return the newly created list

def avg_replce(lst):
	result = []
	for x in range(len(lst)):
		if x == 0:
			result.append(lst[x+1])
		elif x == len(lst)-1:
			result.append(lst[x-1])
		else:
			result.append((lst[x-1]+lst[x+1])/2)
	return result		
a=[1,2,3,4]
print(avg_replce(a))
# need to use append

# def average(least):
# 	for x in range(len(least)):
# 		if x == 0:
# 			least[x] = least[x+1]
# 			# item = least[x+1]
# 			# least.insert(least[x], item)
# 		elif x == len(least)-1:
# 			least[x] = least[x-1]
# 			# item = least[x-1]
# 			# least.insert(least[x], item)
# 		else:
# 			least[x] = (least[x-1]+least[x+1])/2
# 			# item = (least[x-1]+least[x+1])/2
# 			# least.insert(least[x], item)	
# 	return least
# a=[1,2,3,4]
# print(average(a))


