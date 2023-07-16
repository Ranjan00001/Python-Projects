# write a function partition_list(arr, k) having two arguments: a list of distinct integers arr and an integers k 
# such that 0<= k <=len(arr). The function returns a tuple of two list: one containing the k largest elements of arr 
# and the others with the remaining elements of arr. Both these lists have elements in the same order as they appeared in arr
# [hint: write a helper function count_larger(arr, x) that returns the number of elements in arr that are larger than x]

def count_larger(arr, x):
	count = 0
	for i in arr:
		if i > x:
			count += 1
	return count	
arr=[1,2,3,4,5,6,7,8]
print(count_larger(arr, 5))

def partition_list(arr, k):
	'''
	0 <= k <= len(arr)
	'''
	lst1 = []
	lst2 = []
	for x in range(len(arr)):
		if arr[x] < k:           # and count_larger(arr, k) > len(lst1):
			lst1.append(arr[x])
		else:
			lst2.append(arr[x])
	return (lst1, lst2)	

a=[1,2,3,4,5,6,11,8,2]
print(partition_list(a, 4))
