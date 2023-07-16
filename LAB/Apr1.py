# # def linear_search(v, b):
# # 	'''
# # 	returns first occurence of v in b
# # 	'''
# # 	l = len(v)
# # 	for x in range(len(b)):
# # 		if b[x:x+l] == v:
# # 			return x

# # 	return -1

# # print(linear_search('xab', 'hshvxa'))


# # def linear_search(v, b):
# # 	x = 0
# # 	while x < len(b) and b[x] == v:
# # 		i += 1
# # 	if x == len(b):
# # 		return -1

# # 	return x


# # def reverse_linear_search(v, b):
# # 	for x in range(len(b)-1, -1, -1):
# # 		# print(x)
# # 		if b[x] == v:
# # 			return x

# # 	return -1

# # print(reverse_linear_search('a', 'ggdkyga'))


# def binary_search(v, b):
# 	'''
# 	returns first occurence of v in b
	
# 	b is a sorted sequence
# 	'''
# 	left  = 0
# 	right = len(b)
# 	guess = (left + right) //2
# 	loop  = 0

# 	while b[guess] != v:
# 		# print(guess)
# 		loop += 1
# 		if loop > len(b):
# 			return -1
# 		if b[guess] < v:
# 			left = guess
# 		elif b[guess] > v:
# 			right = guess
# 		guess = (left + right) // 2

# 	return guess

# lst = [4,5,12,23,89, 90, 456, 567,1000]
# print(binary_search(100, lst))


# # binary search using recursion  
# def binary_search(v, b):
# 	if not v in b:
# 		return -1
# 	left  = 0
# 	right = len(b)
# 	guess = (left + right) //2
# 	# print(guess)
# 	if b[guess] == v:
# 		print('if')
# 		# print(guess)
# 		return guess
# 	elif b[guess] < v:
# 		print('elif')
# 		return binary_search(v, b[guess:])

# 	# elif b[guess] > v:
# 	else:
# 		print('else')
# 		return binary_search(v, b[:guess])

# lst = [4,5,12,23,89, 90, 456, 567,1000]
# # a = binary_search(90, lst)
# # print(a)

# # Sorting
# # insertion sort

# lst = [4,10,23,50,90, 12, 36, 18]
# # print(push_down(5, lst))
# seq = [4,5,12,23,89, 90, 456, 567,1000, 23,1]
# # a = Sorting(seq)
# # print(a)


# # insertion sort using another method
# def Insertion_sort(seq):
# 	i = 1
# 	while i < len(seq):
# 		push_in(i, seq)
# 		# print(i, seq)
# 		i += 1
# 	return seq

# def push_in(x, seq):
# 	temp = seq[x]
# 	while x >= 0:
# 		# print('x', x)
# 		if temp < seq[x-1] and x != 0:
# 			# print('if', seq[x], x)
# 			seq[x] = seq[x-1]
# 			# seq[x-1] = temp
# 			x -= 1
# 		else:
# 			seq[x] = temp
# 			# print(seq[x], x)
# 			break

# seq = [9,3,78,69,5,12,45,34,23,89,23,67]
# # a = Insertion_sort(seq)
# # print(a)


# # t = (1,2)
# # a,b = t
# # print(a)

# # def partition(b,h,k):
# # 	'''
# # 	Returns the new position of pivot in partitioned list b[h..k]. 
# # 	Partition list b[h..k] around a pivot x = b[h]
# # 	'''
# # 	# we're starting assuming that there're 0 elements having value lesser than pivot and same for greater values also
# # 	i = h
# # 	j = k
# # 	while i < k and j > h:
# # 		# here doubt arises that how should i find the exact position of pivot
# # 		# here we can do that by counting how many numbers are less than or equal to pivot b[i]
# # 		a = min_count(b, i)
# # 		print(a, i, j)
# # 		# swap(b, a, i) if b[a] != b[i] else swap(b, a+1, i)
# # 		# this normal swap won't work bcz if b[a] is greater than b[i] then it will go to b[j] else it will go to b[i-1]
# # 		if b[a] > b[i]:
# # 			b[j] = b[a]
# # 			b[a] = b[i]
# # 		# elif b[a] < b[i]:
# # 		else:
# # 			b[i-1] = b[a]
# # 			b[a] = b[i]
# # 		print(seq)
# # 		i += 1
# # 		j -= 1
# # 	return b

# # def min_count(seq, x):
# # 	'''
# # 	returns the number of elements less than x in seq
# # 	'''
# # 	count = 0
# # 	for j in seq:
# # 		# print(seq[x])
# # 		if seq[x] > j:
# # 			# print('if')
# # 			count += 1

# # 	return count

# seq = [9,3,78,69,5,12,45,34,23,89,23,67]
# # q = min_count(seq, 5)
# # print(q)
# # r = partition(seq,0,11)
# # print(r)
my_list=[11,22,33,44,55]
my_iter = iter(my_list)
for i in my_iter:
	print(next(my_list))
	if i % 2 != 0:
		print(i)
