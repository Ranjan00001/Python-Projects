def verify_list(table):
	l=[]
	for i in table:
		if type(i) != list:
			l.append(i)
		else:
			l=[j for i in table for j in i ]
	# print(l)
	# result
	for i in range(1,10):
		# result= l.count(i)
		if l.count(i) != 1:
			# print(l.count(i))
			return False	
	return True

# table=[[2, 1, 9], [5, 4, 3], [8, 7, 6]]
# table = [[3,4,1],[5,2,6],[7,8,9]]
# print(verify_list(table))
table= [[i for i in range(1,10)] for j in range(9)]
# print(table)

def row_verify(table):
	'''
	verify a list for every row in table
	'''
	result=True
	for row in table:
		# print(row)
		if not verify_list(row):
			result = False
	return result
	
# print(row_verify(table))


def column_verify(table):
	
	result=True
	for j in range(9):
		column = [i[j] for i in table]
		if not verify_list(column):
			result = False
	return result

# print(column_verify(table))

def box_verify(table):
	result = True
	for i in range(3):
		# print('3i',table[3*i])
		# print('3i+1',table[3*i+1])
		# print('3i+2',table[3*i+2])
		for k in range(3):
			box = [table[3*i][3*k:3*(k+1)] ,table[3*i+1][3*k:3*(k+1)], table[3*i+2][3*k:3*(k+1)]]
			# print('box',box)
			# print(verify_list(box))
			if not verify_list(box):
				result = False	
	return result

# print(box_verify(table))


def sudoku_verify(table):
	return row_verify(table) and column_verify(table) and box_verify(table)


t= [[2, 1, 9, 5, 4, 3, 6, 7, 8], [5, 4, 3, 8, 7, 6, 9, 1, 2], [8, 7, 6, 2, 1, 9, 3, 4, 5], [4, 3, 2, 7, 6, 5, 8, 9, 1], [7, 6, 5, 1, 9, 8, 2, 3, 4], [1, 9, 8, 4, 3, 2, 5, 6, 7], [3, 2, 1, 6, 5, 4, 7, 8, 9], [6, 5, 4, 9, 8, 7, 1, 2, 3], [9, 8, 7, 3, 2, 1, 4, 5, 6]]
print(row_verify(t))
print(column_verify(t))
print(box_verify(t))
print(sudoku_verify(t))
