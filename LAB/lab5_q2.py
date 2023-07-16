#we have to write only specification and doctest 

def vowels_alphabetical(s):
	'''
	returns True if the vowels in argument are in alphabetical order, and returns False otherwise

	it will return true if all vowels in a word are in alphabetical
	order and return false if these vowels are not in alphabetical order
 	In otherwords, the first occurrence of ‘a’ (if any) appears 
	before first e (if any) gives correct, first ‘e’ appears 
	before first ‘i’ if any etc.vowels are a,e,i,o,u .
	upper and lower case are taken same

	>>>vowels_alphabetical('a')
	true
	>>>vowels_alphabetical('ou')
	true
	>>>vowels_alphabetical('aie')
	false
	>>>vowels_alphabetical('')
	-1
	>>>vowels_alphabetical('mny')
	false

	parameter s:it is the word for which we have to find order of vowel
	precondition:it should be in string

	'''
