def function(n,k):
	'''
	returns a list of combination of k numbers in range(1,n)
	'''
	l = []
	for i in range(1,n):
		for j in range(1,k+1):
			m = [i,i+j]
			l.append(m)


	# value = float(value)
 #    while len(str(value)) > 5:
 #        # if len(str(value)) > 5:
 #        value = round(value, len(str(value))-1)
 #    while len(str(value)) < 5:
 #       value = float(str(value)+'0')   
 #    return str(value)
    a = str(value).find('.')+1
    l = len(str(value))
    if l > 5:
        value = round(value,l-5)
    1.3546    
    elif l == 4:
        value = round(value+)
        1
    # value = float(value)
    # a = str(value).find('.')+2
    # l = len(str(value))
    # if l != 5:
    #     value = round(value,l-a)
    # if len(str(value)) == 5:
    #     return str(value)
    # else:
    #     str5(value)
    # pass
# '%0.2f'(4/3)  
# print()
# print(str5(130.59))			
		