def vowels_alphabetical(s):
	'''
	returns True if the vowels in argument are in alphabetical order, and returns False otherwise

	it will return true if all vowels in a word are in alphabetical
	order and return false if these vowels are not in alphabetical order
 	In otherwords, the first occurrence of ‘a’ (if any) appears 
	before first e (if any) gives correct, first ‘e’ appears 
	before first ‘i’ if any etc.vowels are a,e,i,o,u .
	upper and lower case are taken same

	>>> vowels_alphabetical('a')
	True
	>>> vowels_alphabetical('ou')
	True
	>>> vowels_alphabetical('aie')
	False
	>>> vowels_alphabetical('')
	True
	>>> vowels_alphabetical('mny')
	True
	>>> vowels_alphabetical('ae')
	True
 
	parameter s:it is the word for which we have to find order of vowel
	precondition:it should be in string

	'''
	a1 = s.find('a')
	e = s.find('e')
	e1=e if e>=0 else a1
	i=s.find('i')
	i1=i if i>=0 else e1
	o=s.find('o')
	o1=o if o>=0 else i1
	u=s.find('u')
	u1=u if u>=0 else o1
	return a1<=e1<=i1<=o1<=u1
if __name__ =='__main__':
	import doctest
	doctest.testmod()



