# # # # linear search

# # # def linear_search(v,b):
# # # 	"""
# # # 	Returns: first occurrence of v in b; -1 if not found

# # # 	Parameter v: The value to search for
# # # 	Precondition: None (v can be any value)

# # # 	Parameter b: The sequence to search for
# # # 	Precond: b is a sequence
# # # 	"""
# # # 	i = 0
# # # 	while i < len(b):
# # # 		if b[i] == v:
# # # 			return i
# # # 		i += 1
# # # 	return -1

# # # b = [i for i in range(10)]
# # # print(linear_search(3, b))



# # # binary search

# # def binary_search(v,b):
# # 	"""
# # 	Returns: an occurrence of v in b

# # 	Parameter v: The value to search for
# # 	Precondition: None (v can be any value)

# # 	Parameter b: The sequence to search for
# # 	Precond: b is a sorted sequence
# # 	"""
# # 	left  = 0
# # 	right = len(b)
# # 	guess = (left + right) // 2
# # 	i = left
# # 	while b[guess] != v:
# # 		if b[guess] < v:
# # 			left  = guess
# # 		else:
# # 			right = guess
# # 		# i += 1
# # 		# print(i)
# # 		guess = (left + right) // 2
# # 	return guess

# # b = [i for i in range(100)]
# # print(binary_search(50,b))



# # Sorting

# # Insertion sort
# def Insertion_sort(b):
# 	'''
# 	returns the sorted seq

# 	precondition: b is a sequence
# 	'''
# 	length = len(b)
# 	i = 1                # i is pos of element to which we're gonna move
# 	while i < length:
# 		move_in(i, b)
# 		i += 1
# 	return b

# def move_in(i, b):
# 	'''
# 	shifts this b[i] so that it will stay at right pos in this current sorted seq

# 	basically it compares i-1, i-2, and so on then moves
# 	this b[i] to i-r+1 when this b[i-r] < b[i]
	
# 	parameter i: pos of element in b which is to be moved to it's pos in current sorted seq
# 	precondiition: int

# 	parameter b: seq on which we have to work on
# 	precondition: a seq
# 	'''
# 	r = 1
# 	pivot = b[i]
# 	while b[i-r] > pivot and r <= i:
# 		swap(b, i-r, i-r+1)
# 		print(b, i, r)
# 		r += 1

# def swap(b, h, k):
# 	'''
# 	swaps the element at k with h for seq b
# 	'''
# 	temp = b[h]
# 	b[h] = b[k]
# 	b[k] = temp

# b = [76, 23, 1, 2, 6]
# print(Insertion_sort(b))

# selection sort

def selection_sort(b):
	i = 1
	length = len(b)
	while i < length:
		a = find_pos(i, b)
		print(a)
		swap(b, i, a)
		print(b, i, a)
		i += 1
	return b

def find_pos(i, b):
	'''
	returns the pos for b[i] in the current sorted seq

	parameter i: pos of element in b for which we have to find it's correct pos in current sorted seq
	precondiition: int

	parameter b: seq on which we have to work on
	precondition: a seq
	'''
	pos = 1
	while pos > 0:
		if b[i-pos] > b[i]:
			pos -= 1
		else:
			break

	return pos

def swap(b, h, k):
	'''
	swaps the element at k with h for seq b
	'''
	temp = b[h]
	b[h] = b[k]
	b[k] = temp

b = [76, 23, 1, 2, 6]
# print(selection_sort(b))

# quick sort
def partition(b, h, k):
	'''
	returns the partitioned list where pivot would be at its original pos in partitioned sorted list
	'''
	# here we're chosing pivot as b[h], we can vary it also
	pivot = b[h]
	c = count_min(b, h)


def count_min(b, h):
	'''
	returns count of the number less than b[h]
	'''
	for i in range()