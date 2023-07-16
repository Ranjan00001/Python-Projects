def anglicize1to19(n):
	'''
	0<n<20

	'''
	if n==1:
		return 'one'
	elif n==2:
		return 'two'	
	elif n==3:
		return 'three'	
	elif n==4:
		return 'four'	
	elif n==5:
		return 'five'	
	elif n==6:
		return 'six'	
	elif n==7:
		return 'seven'	
	elif n==8:
		return 'eight'	
	elif n==9:
		return 'nine'	
	elif n==10:
		return 'ten'	
	elif n==11:
		return 'eleven'	
	elif n==12:
		return 'tweleve'	
	elif n==13:
		return 'thirteen'	
	elif n==14:
		return 'fourteen'	
	elif n==15:
		return 'fifteen'	
	elif n==16:
		return 'sixteen'	
	elif n==17:
		return 'seventeen'	
	elif n==18:
		return 'eighteen'	
	else:
	return 'nineteen'
	
def tens(n):
	'''
	0<n<10

	'''
	if n==1:
		return 'ten'
	elif n==2:
		return 'twenty'	
	elif n==3:
		return 'thirty'	
	elif n==4:
		return 'fourty'	
	elif n==5:
		return 'fifty'	
	elif n==6:
		return 'sixty'	
	elif n==7:
		return 'seventy'	
	elif n==8:
		return 'eighty'	
	return 'ninety'	

def anglicize20to99(n):
	'''
	19<n<100

	'''
	if n%10==0:
		return tens(n//10)
	else:
		return tens(n//10)+' '+anglicize1to19(n%10)

def anglicize100to999(n):
	'''
	99<n<1000
	'''
	if n%100==0:
		return anglicize1to19(n//100)+' '+'hundred'
	else:
		return anglicize1to19(n//100)+' '+'hundred'+' '+anglicize20to99(n%100)
def anglicize1000to9999(n):
	'''
	999<n<10000
	'''
	if n%1000==0:
		return anglicize1to19(n//1000)+' '+'thousand'
	else:
		return anglicize1to19(n//1000)+' '+'thousand'+' '+anglicize100to999(n%1000)

def anglicize(n):
	'''
	0<n<10000
	'''
	if n>0 and n<20:
		return anglicize1to19(n)
	elif n>19 and n<100:
		return anglicize20to99(n)
	elif n>99 and n<1000:
		return anglicize100to999(n)
	elif n>999 and n<10000:
		return anglicize1000to9999(n)

print(anglicize(7567))				