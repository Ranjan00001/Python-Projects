def despace(s):
	'''
	returns the string after removing space from s

	parameter s : string to be operated
	precondition: string
	 
	'''
	empty_string=''
	for x in s:
		empty_string=empty_string+x if x!=' ' else empty_string
	return empty_string

print(despace('  hello  world '))		
