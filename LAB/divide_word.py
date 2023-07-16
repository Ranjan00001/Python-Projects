def partition(s):

	# set accumulator even and odd
	# for each index in s
	# see is it 0
	# see is it even
	# see is it odd
	acc_even=''
	acc_odd=''
	for x in range(len(s)):		
		if x%2==0:
			acc_even+=s[x]
		else:
			acc_odd+=s[x]
	return [acc_even,acc_odd]		
print(partition('aabb'))
