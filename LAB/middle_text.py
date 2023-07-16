# revise
# def middle(text):
# 	'''
# 	returns middle , starts at length divided by 3 (rounded down) 
# 	and continues until 2/3 of the string (rounded down)

# 	parameter text : the string to slice
# 	precondition : text is a string

# 	>>> middle('abc')
# 	'b'
# 	>>> middle('abcd')
# 	'b'
# 	>>> middle('abcde')
# 	'bc'
# 	>>> middle('ab')
# 	'a'

# 	'''
# 	size = len(text)
# 	start = size//3
# 	end = 2*size//3
# 	return = text[start:end] 

# if __name__ == '__main__':
# 	import doctest
# 	doctest.testmod()

import math
def sol_middle(text):
	start = math.floor(len(text)/3)
	end  = math.floor(2*len(text)/3)
	return text[start:end]

# print(sol_middle('abcde'))

# from hypothesis import given,strategies as st
# #@settings(max_examples=100)
# @given(st.text(min_size=3))
# def test_abc(word):
#  	assert middle(word)==sol_middle(word)

