# we have to write only specification and doctest 

def unique_vowels_in_word(s, case_sensitive=False):
	'''
	returns the number of unique vowels in a given string s

	it counts the number of unique vowels (a,e,i,o,u) in a given 
	word, it can consider also the case sensitive vowels 
	if you want that will be taken in second argument

	>>>unique_vowels_in_word('abhay',true)
	1
	>>>unique_vowels_in_word('Abhay',true)
	2
	>>>unique_vowels_in_word('Abhay',false)
	1
	>>>unique_vowels_in_word('Abhay')
	1
	>>>unique_vowels_in_word('')
	-1

	parameter s: it is the word for which we have to count unique vowels
	precondition : it should be string

	parameter true/false:shows case sensitivity of word
	precondition:it should be bool

	in second parameter false will be taken as default


	'''


