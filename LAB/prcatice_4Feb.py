# try:
# 	result=input('number: ')
# 	x=float(result)
# 	print('the next number is '+str(x+1))
# except:
# 	print('that is not a number! Try again')
# 	result=input('number:')
# 	x=float(result)
# 	print('the next number is '+str(x+1))


# loop=True
# while loop:
# 	try:
# 		result=input('number: ')
# 		x=float(result)
# 		print('the next number is '+str(x+1))
# 		loop= False
# 	except:
# 		print('that is not a number! Try again')


# def sum_square(n):
# 	total=0
# 	for i in range(n):
# 		total+=i*i

# def sum_square1(n):
# 	# print('before while')
# 	total=0
# 	i=0
# 	while i<n:
# 		# print('start loop '+str(x))
# 		total+=i*i
# 		i+=1
# 		# print('end loop')
# 	print('after loop')	
# 	return total

# print(sum_square1(5))

# def count_slash(s):
# 	count=0
# 	# for i in s:
# 	# 	if i == '/':
# 	# 		count+=1
# 	# for i in range(len(s)):
# 	# 	if s[i] == '/':
# 	# 		count+=1
# 	x=0
# 	while x < len(s):
# 		if s[x] == '/':
# 			count+=1
# 		x+=1
# 	x=s[0]
# 	while x == '':
# 		if x == '/':
# 			count+=1

# 	return count

# s='a/s/d/f'
# print(count_slash(s))


# def add_fracs(n):
# 	total = 0
# 	# for i in range(1,n+1):
# 	# 	total+=1/i
# 	i=1
# 	while i < n+1:
# 		total+=1/i
# 		i+=1
# 	return(total)

# print(add_fracs(4))	


# def prmpt(prompt,valid):
# 	while True:
# 		ans = input(prompt)
# 		if ans in valid:
# 			return ans
# 		else:
# 			print('enter valid ans')	
# prompt='enter choice: '
# valid=('a','b','c','d')
# print(prmpt(prompt,valid))

import random 
def roll_past(goal):
	score = 0
	while goal < score:
		die = random.randint(1,6)
		print(die)
		if die != 1:
			score+=die
		else:
			return 0
	# loop =True
	# while loop:
	# 	roll =random.randint(1,6)
	# 	if roll == 1:
	# 		score=0
	# 		loop=False
	# 	else:
	# 		score+=roll
	# 		loop=score<goal	
	return score

print(roll_past(15))


# def list_square(n):
# 	l=[]
# 	i=0
# 	while i < n:
# 		if i*i < n:
# 			l.append(i*i)
# 		i+=1	
# 	for i in range(int(n**0.5)+1):
# 		if i*i < n:
# 			l.append(i*i)
# 	return l

# print(list_square(15))	


# def rem3(lst):
# 	# for i in range(len(lst)):
# 	# 	if lst[i] == 3:

# 	i=0
# 	while i<len(lst):
# 		if lst[i]==3:
# 			del lst[i]
# 		else:
# 			i+=1
# 	print(lst)

# def sqrt1(c):
	
# 	x=c/2
# 	while abs(x*x-c)>1e-6:
# 		x=x/2+c/(2*x)
# 	return x	

# print(sqrt1(2))
# import math
# print(math.sqrt(2)==sqrt1(2))

