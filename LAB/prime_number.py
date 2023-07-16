def is_prime0(n):
	for x in range(1,n,2):
		if n == 2 or n == 3 or 6*x+1 == n or 6*x-1 == n or n%5 !=0:
			# print(x)
			return True
	return False

# print(is_prime0(19))

import math 
def is_composite(n):
	for x in range(2, math.ceil(n**0.5)+1):
		if n%x == 0:
			return True 

# print(is_composite(4))

def is_prime(n):
	'''
	need to care about 1
	'''
	return n == 2 or not is_composite(n)

	# for x in range(1,n,2):
	# 	a=True if n%x != 0 else False
	# return a
a=10		
print(is_prime(a))

def is_prime1(n):
	if n == 2:
		return True
	for x in range(2, math.ceil(n**0.5)+1):
		if n%x == 0:
			return False
	return True

print(is_prime1(a))			

# from hypothesis import given,strategies as st
# #@settings(max_examples=100)
# @given(st.decimal)
# def test_prime(n):
#  	assert middle(n)==sol_middle(n)

