def swap(lst, a, i):
	'''
	swaps ath elememnt with ith for lst
	'''
	temp = lst[i]
	lst[i] = lst[a]
	lst[a] = temp		

def selection_sort(lst):

	i = 0
	length = len(lst)
	while i < length:
		# print(i)
		a = min_pos(lst, i)
		# print(a)
		swap(lst, a, i)
		i += 1
	return lst

count = 0
def min_pos(lst, i):
	'''
	returns pos of min number in list lst after ith position
	'''
	global count
	result = lst[i]
	for x in range(i, len(lst)):
		# print(x, result)
		count += 1
		if lst[x] <= result:
			result = lst[x]
			pos = x
			
	return pos

seq = [i for i in range(200)]
import random
random.shuffle(seq)
# print(seq)
a = selection_sort(seq)
print(a)