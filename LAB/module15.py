def last_name_first(name):
	'''
	returns copy of <name> is in the form <last name>,<first name>
	
	parameter name : name to reverse
	precondition : name is in the form <first name>,<last name>
	               name has only one space, separating first and last

	>>> last_name_first('sitare foundation')
	'foundation,sitare'
	>>> last_name_first('foundation  sitare')
	'sitare,foundation'

	'''
	assert type(name) == str ,'Precondition violation'
	assert name.count(' ') == 1, 'Precondition violation'
	first_end = name.find(' ')
	first = name[:first_end]
	last = name[first_end+1:].strip()
	return last +','+first


def last_name_first1(name):
	'''
	returns copy of <name> is in the form <last name>,<first name>
	
	parameter name : name to reverse
	precondition : name is in the form <first name>,<last name>
	               name has only one space, separating first and last

	>>> last_name_first('sitare foundation')
	'foundation,sitare'
	>>> last_name_first('foundation  sitare')
	'sitare,foundation'

	'''
	assert type(name) == str ,str(name)+'is not a string'
	assert ' ' in name, name+'is missing a space'
	assert name.count(name,' ') == 1, name+'has too many spaces'
	first_end = name.find(' ')
	first = name[:first_end]
	last = name[first_end+1:].strip()
	return last +','+first


def is_two_words(w):
	first_space = w.find(' ')
	first_name = w[:first_space]
	last_name = w[first_space:].strip(' ')
	if first_name == '':
		return False
	elif last_name == '':
		return False	
	# elif ' ' in first_name:
	# 	return False
	elif ' ' in last_name:
		return False
	elif not ' ' in w:
		return False		
	else:
		return True	 

# a='ab'		
# print(is_two_words(a))		 	
