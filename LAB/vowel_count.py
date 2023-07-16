# important,please revise
# print(in place of return) doctest me kam karega and compare wale me kam nahi karega
# compare wale me do type hai 
# 1st is that ham ek standard function lekar apne given argument se compare kar le
# 2nd is that ham ek standard function lekar hypothesis se argument le and compare kare
# remember that hypothesis can't give u 100 percent correctness


def num_vowels(word):
	'''
	Returns: number of vowels in string word.
 	Vowels are defined to be 'a','e','i','o', and 'u'. 
 	Repeated vowels are counted separately. Both upper case and 
 	lower case vowels are counted.
 	
	>>> num_vowels('hat')
	1
	>>> num_vowels('ate')
	2
	>>> num_vowels('but')
	1
	>>> num_vowels('Eet')
	2
	>>> num_vowels('put')
	1
	
 	Parameter word: The text to check for vowels
 	Precondition: word string w/ at least one letter and only letters
	'''
	a= word.count('a')+word.count('A')
	e= word.count('e')+word.count('E')
	i= word.count('i')+word.count('I')
	o= word.count('o')+word.count('O')
	u= word.count('u')+word.count('U')
	return (a+e+i+o+u)

# if __name__=='__main__':
# 	import doctest
# 	doctest.testmod()

def sol_num_vowels(word):
	a = word.count('a')+word.count('A')
	e = word.count('e')+word.count('E')
	i = word.count('i')+word.count('I')
	o = word.count('o')+word.count('O')
	u = word.count('U')+word.count('U')

	return (a+e+i+o+u)


def test_abc():
	assert num_vowels('hat')==sol_num_vowels('hat')
	assert num_vowels('hate')==sol_num_vowels('hate')
	assert num_vowels('beet')==sol_num_vowels('beet')
	assert num_vowels('sky')==sol_num_vowels('sky')
	assert num_vowels('year')==sol_num_vowels('year')
	assert num_vowels('put')==sol_num_vowels('put')

# from hypothesis import given,strategies as st,settings
# @settings(max_examples=100)
# @given(st.text(min_size=3))
# def test_num_vowels(word):
#  	assert num_vowels(word)==sol_num_vowels(word)

if __name__ == '__main__':
	test_abc()