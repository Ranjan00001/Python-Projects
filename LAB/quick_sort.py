# def swap(lst, a, i):
# 	'''
# 	swaps ath elememnt with ith for lst
# 	'''
# 	temp = lst[i]
# 	lst[i] = lst[a]
# 	lst[a] = temp

# count = 0
# def partition(b, h, k):
# 	"""Partition list b[h..k] around a pivot x = b[h]"""
# 	global count
# 	i = h
# 	j = k+1
# 	x = b[h]
# 	while i < j-1:
# 		count += 1
# 		if b[i+1] >= x:
# 			swap(b,i+1,j-1)
# 			j = j - 1
# 		else: # b[i+1] < x
# 			swap(b,i+1, i)
# 			i = i + 1
# 	return i

# def quick_sort(b, h, k):
# 	if k-h < 1:
# 		return
# 	j = partition(b, h, k)
# 	quick_sort(b, h, j-1)
# 	quick_sort(b, j+1, k)

# # seq = [9,3,78,5,12,45,34,23,89,23,67]
# seq = [4,22,5,33,1,2]
# quick_sort(seq, 0, len(seq)-1)
# print(seq)
# print(count)

Sel_comp_count = 0
Sel_swap_count = 0

def Selection_sort(b):
  '''
  returns the sorted seq

  parameter b: mutable seq to be sorted
  precondition: seq(mutable)
  '''
  global Sel_swap_count
  i = 0
  length = len(b)
  while i < length:
    a = find_pos(b, i)
    swap(b, a, i)
    Sel_swap_count += 1
    i += 1
  return b

def find_pos(b, i):
  '''
  returns the pos of b[i] in current sorted seq
  it counts the element whivh are less than b[i]
  '''
  global Sel_comp_count
  for j in range(i, len(b)):
    if b[j] < b[i]:
      pos = j
    Sel_comp_count += 1
  return pos

# seq = [i for i in range(200)]
# import random
# random.shuffle(seq)
seq = [4,1, 7, 7, 1, 2, 3]
a = Insertion_sort(seq)
print(seq)
print(Sel_comp_count, Sel_swap_count)