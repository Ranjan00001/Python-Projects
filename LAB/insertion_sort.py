def swap(lst, a, i):
	'''
	swaps ath elememnt with ith for lst
	'''
	temp = lst[i]
	lst[i] = lst[a]
	lst[a] = temp

def Sorting(seq):
	n = len(seq)
	i = 1
	while i < n:
		push_down(i, seq)
		# print('outer loop: ',i)
		i += 1

	return seq

def push_down(x, seq):
	'''
	pueshes down seq[x] to it's sorted order in seq

	x is index
	'''
	# seq.append(a)
	# print(len(seq))
	# for x in range(len(seq)-1, -1, -1):
	# 	# print(x)
	# 	if seq[x] > seq[a]:
	# 		# seq[x]  = seq[x-1]
	# 		seq[x-1], seq[a], seq[x] = seq[a], seq[x], seq[x-1] 
	# 		print(seq)
	# return seq
	# x = a
	while x > 0 and seq[x-1] > seq[x] :
		# if seq[x-1] > seq[x]:
		swap(seq, x-1, x)
		# print(x)
		x -= 1

seq = [i for i in range(200)]
import random
random.shuffle(seq)
# print(seq)
a = Sorting(seq)
# print(count)

