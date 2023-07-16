# def unique_vowels_in_word(s, case_sensitive=False):
# 	'''
# 	returns the number of unique vowels in a given string s

# 	it counts the number of unique vowels (a,e,i,o,u) in a given 
# 	word, it can consider also the case sensitive vowels 
# 	if you want that will be taken in second argument.
# 	in second parameter false will be taken as default.
# 	it should return -1 if string is non alphabetical.

# 	>>> unique_vowels_in_word('abhay',True)
# 	1
# 	>>> unique_vowels_in_word('Abhay',True)
# 	2
# 	>>> unique_vowels_in_word('Abhay',False)
# 	1
# 	>>> unique_vowels_in_word('A',True)
# 	1
# 	>>> unique_vowels_in_word('Ee',True)
# 	2
# 	>>> unique_vowels_in_word('')
# 	-1

# 	parameter s: it is the word for which we have to count unique vowels
# 	precondition : it should be string

# 	parameter true/false:shows case sensitivity of word
# 	precondition:it should be bool

# 	'''
# 	if not s.isalpha():
# 		return -1
# 	elif case_sensitive:
# 		A=s.count('A')
# 		A1 =1 if A>=1 else 0
# 		E=s.count('E')
# 		E1=1 if E>=1 else 0
# 		I=s.count('I')
# 		I1=1 if I>=1 else 0
# 		O=s.count('O')
# 		O1=1 if O>=1 else 0
# 		U=s.count('U')
# 		U1=1 if U>=1 else 0
# 		a=s.count('a')
# 		a1=1 if a>=1 else 0
# 		e=s.count('e')
# 		e1=1 if e>=1 else 0
# 		i=s.count('i')
# 		i1=1 if i>=1 else 0
# 		o=s.count('o')
# 		o1=1 if o>=1 else 0
# 		u=s.count('u')
# 		u1=1 if u>=1 else 0
# 		return a1+e1+i1+o1+u1+A1+E1+I1+O1+U1
# 	# elif not case_sensitive:
# 	else:
# 		r=s.lower()
# 		a=r.count('a')
# 		a1=1 if a>=1 else 0
# 		e=r.count('e')
# 		e1=1 if e>=1 else 0
# 		i=r.count('i')
# 		i1=1 if i>=1 else 0
# 		o=r.count('o')
# 		o1=1 if o>=1 else 0
# 		u=r.count('u')
# 		u1=1 if u>=1 else 0
# 		return a1+e1+i1+o1+u1

# # if __name__ == '__main__':
# # 			import doctest
# # 			doctest.testmod()

# def sol_unique_vowels_in_word(s,case_sensitive=False):
# 	if not s.isalpha():
# 		return -1
# 	vowels = 'aeiouAEIOU'
# 	if not case_sensitive:
# 		s = s.lower()
# 	return len(set(s).intersection(vowels))

# # def test_1_arg():
# # 	assert unique_vowels_in_word('abhay')==sol_unique_vowels_in_word('abhay')
# # 	assert unique_vowels_in_word('Abhay')==sol_unique_vowels_in_word('Abhay')
# # 	assert unique_vowels_in_word('')==sol_unique_vowels_in_word('') 

# # def test_2_arg(s, case_sensitive=False):
# # 	assert unique_vowels_in_word('abhay',True) == sol_unique_vowels_in_word('abhay',True)
# # 	assert unique_vowels_in_word('Abhay',True) == sol_unique_vowels_in_word('Abhay',True)
# # 	assert unique_vowels_in_word('abhay',False) == sol_unique_vowels_in_word('abhay',False)
# # 	assert unique_vowels_in_word('abhay') == sol_unique_vowels_in_word('abhay')
# # 	assert unique_vowels_in_word('') == sol_unique_vowels_in_word('')

# from hypothesis import given, strategies as st, settings
# @settings(max_examples=1000)
# @given(st.text())
# def test_1_arg(s):
# 	assert unique_vowels_in_word(s) == sol_unique_vowels_in_word(s)
# # Test with two arguments
# @given(st.text(), st.booleans())
# def test_2_arg(s, b):
# 	assert unique_vowels_in_word(s, b) == sol_unique_vowels_in_word(s, b)
# # Run the Hypothesis
# if __name__ == '__main__':
# 	test_1_arg()
# 	test_2_arg()
# 	



def incr(x):
	return x+1
def decr(x):
	return x-1
if __name__ == '__main__':
	print(incr(5))
	print(decr(5))
	