# this is a imutable function
def copy_add_one(lst):
	result=[]
	# print(result)
	for x in lst:
		x=1+x
		print(id(x))
		result.append(x)
	 	# # print(id(result))
		# result=result+[x]
		# # print(id(result))
		# # print(result)
	return result
a=[1, 2, 3]
print(copy_add_one(a))		
# print(a)