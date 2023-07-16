def palindrome(word):
	# word = input('enter the string word :')
	'''
	it decides that word is palindrome or not
	
	>>> palindrome('gagagag')
	True
	>>> palindrome('gagdf')
	False
	>>> palindrome('')
	True

	parameter word :it should be the word for which we have to decide 
	precondition: it should be string
	# can ignore the case of string
	
	'''
	# size=len(word)
	result=word[::-1]
	return word==result
	
if __name__ == '__main__':
	import doctest
	doctest.testmod()
