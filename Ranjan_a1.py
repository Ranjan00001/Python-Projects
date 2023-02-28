"""
Module for currency exchange
This module provides several string parsing 
functions to implement a simple currency
exchange routine using an online currency
service.
The primary function in this module is exchange.
Author: RANJAN SINGH
Date: 29 Nov 2022
"""

# this gives the string before first space
def before_space(s):

	'''
	Returns a copy of s up to, but not including, the first space

	Parameter s: the string to slice
	Precondition: s is a string with at least one space

	# testing for string before first white space
	>>> before_space('rana ds')
	'rana'
	>>> before_space('rana  ds')
	'rana'
	>>> before_space(' rana ds')
	''

	'''
	first_space=s.find(' ')
	return s[:first_space]
# if __name__ == '__main__':
# 		import doctest
# 		doctest.testmod()
 

# this gives the string after first space
def after_space(s):
	'''
	Returns a copy of s after the first space

	Parameter s: the string to slice
	Precondition: s is a string with at least one space

	# testing for string after first white space
	>>> after_space('rana ds')
	'ds'
	>>> after_space('rana  ds')
	' ds'
	>>> after_space(' rana ds')
	'rana ds'
	>>> after_space('rana ds ')
	'ds '
	
	'''
	first_space=s.find(' ')
	return s[first_space+1:]

# if __name__ == '__main__':
# 		import doctest
# 		doctest.testmod()


# this is giving the string inside first quote
def first_inside_quotes(s):
	'''

	Returns the first substring of s between two (double) quotes

	A quote character is one that is inside a string, not one that
	delimits it. We typically use single quotes (') to delimit a
	string if we want to use a double quote character (") inside of it.
	
	Examples:

	first_inside_quotes('A "B C" D') returns 'B C'
	first_inside_quotes('A "B C" D "E F" G') returns 'B C',

	because it only picks the first such substring

	Parameter s: a string to search
	Precondition: s is a string containing at least two double quotes

	# testing for string between first double quote
	>>> first_inside_quotes('{ "lhs" : "2.5 United States Dollars", "rhs" : "64.375 Cuban Pesos", "err" : "" }')
	'lhs'
	>>> first_inside_quotes('A"B C"D "E F" G')
	'B C'
	>>> first_inside_quotes('A "B C" "E F" D')
	'B C'
	>>> first_inside_quotes('A " " "B C" D')
	' '

	'''
	first_double_quote= s.find('"')
	second_double_quote=s.find('"',first_double_quote+1)
	return s[first_double_quote+1:second_double_quote]

# if __name__ == '__main__':
# 		import doctest
# 		doctest.testmod()

# this is giving the string written after lhs in json string
def get_lhs(json):
	'''
	Returns the lhs value in the response to a currency query

	Given a JSON response to a currency query, this returns the
	string inside double quotes (") immediately following the keyword
	"lhs". For example, if the JSON is
	'{ "lhs" : "1 Bitcoin", "rhs" : "19995.85429186 Euros", "err" : "" }'
	then this function returns '1 Bitcoin' (not '"1 Bitcoin"').
	This function returns the empty string if
	the JSON response contains an error message.

	Parameter json: a json string to parse
	Precondition: json is the response to a currency query
	
	# testing for string written for lhs
	>>> get_lhs('{ "lhs" : "2.5 United States Dollars", "rhs" : "64.375 Cuban Pesos", "err" : "" }')
	'2.5 United States Dollars'
	>>> get_lhs('{ "lhs" : "2.5 Indian Rupees", "rhs" : "0.80682545635019 Cuban Pesos", "err" : "" }')
	'2.5 Indian Rupees'
	>>> get_lhs('{ "lhs" : "", "rhs" : "", "err" : "Source currency code is invalid." }')
	''

	'''
	substring_start = json.find(':')+3
	substring_end = json.find('"',substring_start)
	return json[substring_start:substring_end]

# if __name__ == '__main__':
# 	import doctest
# 	doctest.testmod()




# this is giving the string written after rhs in json string
def get_rhs(json):
	'''

	Returns the rhs value in the response to a currency query

	Given a JSON response to a currency query, this returns the
	space tring inside double quotes (") 
	immediately following the keyword"rhs".
	For example, if the JSON is
	'{ "lhs" : "1 Bitcoin", "rhs" : "19995.85429186 Euros", "err" : "" }'
	then this function returns '19995.85429186 Euros' (not '"38781.518240835 Euros"').
	This function returns the empty string if the JSON response
	contains an error message.

	Parameter json: a json string to parse
	Precondition: json is the response to a currency query

	# testing for string written after rhs in double quote
	>>> get_rhs('{ "lhs" : "2.5 United States Dollars", "rhs" : "64.375 Cuban Pesos", "err" : "" }')	
	'64.375 Cuban Pesos'
	>>> get_rhs('{ "lhs" : "", "rhs" : "", "err" : "Source currency code is invalid." }')
	''

	'''
	substring_start = json.find(':',10)+3
	substring_end = json.find('"',substring_start)
	return json[substring_start:substring_end]

# if __name__ == '__main__':
# 		import doctest
# 		doctest.testmod()


# this is telling true if we got an error otherwise false
def has_error(json):
	'''
	Returns True if the query has an error; False otherwise.

	Given a JSON response to a currency query, this returns True if there
	is an error message. For example, if the JSON is
	'{ "lhs" : "", "rhs" : "", "err" : "Currency amount is invalid." }'
	then the query is not valid, so this function returns True ,
	(It does NOT return the message 'Currency amount is invalid.').
	
	Parameter json: a json string to parse
	Precondition: json is the response to a currency query
	
	# testing that function get_lhs(json) function is getting empty string or not
	>>> has_error('{ "lhs": "2 Namibian Dollars", "rhs": "2 Lesotho Maloti", "err": "" }')
	False
	>>> has_error('{ "lhs": "", "rhs": "", "err": "Source currency code is invalid." }')
	True
	'''
	return get_lhs(json)==''

# if __name__ == '__main__':
#  		import doctest
#  		doctest.testmod()


import requests
def query_website(old, new, amt):
	'''
	Returns a JSON string that is a response to a currency query.

	A currency query converts amt money in currency old to the currency new.
	The response should be a string of the form
	'{ "lhs":"<old-amt>", "rhs":"<new-amt>", "err":"" }'
	where the values old-amount and new-amount contain the value
	and name for the old and new currencies. If the query is
	invalid, both old-amount and new-amount will be empty, while
	"err" will have an error message.

	Parameter old: the currency on hand
	Precondition: old is a string with no spaces or non-letters

	Parameter new: the currency to convert to
	Precondition: new is a string with no spaces or non-letters

	Parameter amt: amount of currency to convert
	Precondition: amt is a float

	# there testing is done on manual level
	>>> query_website('USD','CUP',2.5)
	'{ "lhs" : "2.5 United States Dollars", "rhs" : "64.375 Cuban Pesos", "err" : "" }'
	>>> query_website('INR','USD',2.5)
	'{ "lhs" : "2.5 Indian Rupees", "rhs" : "0.031333027431075 United States Dollars", "err" : "" }'

	'''
	target_url = f'http://cs1110.cs.cornell.edu/2022fa/a1?old={old.upper()}&new={new.upper()}&amt={amt}'
	json = (requests.get(target_url)).text
	return json
	
# if __name__ == '__main__':
#  		import doctest
#  		doctest.testmod()


def is_currency(code):
	'''
	Returns: True if code is a valid (3 letter code for a) currency
	It returns False otherwise.
	
	Parameter code: the currency code to verify
	Precondition: code is a string with no spaces or non-letters. 
	# testing for validity of currency name
	>>> is_currency('USC')
	False
	>>> is_currency('INR')
	True
	

	'''
	amt=1
	return has_error(query_website(code,code,amt))==False

def exchange(old, new, amt):
	'''
	Returns the amount of currency received in the given exchange.

	In this exchange, the user is changing amt money in currency
	old to the currency new. The value returned represents the
	amount in currency new.
	
	The value returned has type float.

	Parameter old: the currency on hand
	Precondition: old is a string for a valid currency code
	
	Parameter new: the currency to convert to
	Precondition: new is a string for a valid currency code

	Parameter amt: amount of currency to convert
	Precondition: amt is a float
	>>> exchange('USD','CUP',2.5)
	64.375
	>>> exchange('INR','USD',2.5)
	0.031333027431075

	'''
	json=query_website(old,new,amt)
	# print(json)
	exchange_amt=get_rhs(json)
	# print(exchange_amt)
	# print(before_space(exchange_amt))
	return float(before_space(exchange_amt))

# print(first_inside_quotes('gchjvhd'))
if __name__ == '__main__':
 	import doctest
 	doctest.testmod()
