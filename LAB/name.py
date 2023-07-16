def last_name_first(name):
	'''
	returns copy of <name> is in the form <last name>,<first name>
	
	parameter name : name to reverse
	precondition : name is in the form <first name>,<last name>

	>>> last_name_first('sitare foundation')
	'foundation,sitare'
	>>> last_name_first('foundation  sitare')
	'sitare,foundation'

	'''
	first_end = name.find(' ')
	first = name[:first_end]
	last = name[first_end+1:].strip()
	return last +','+first

# if __name__=='__main__':
# 	import doctest
# 	doctest.testmod()

#print(last_name_first('ranjan singh'))
#print(last_name_first('ranjan  singh'))
