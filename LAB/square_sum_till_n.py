def sum_squares(n):
	result=0
	for x in range(n+1):
		result+=x**2
	return result	

print(sum_squares(2))
