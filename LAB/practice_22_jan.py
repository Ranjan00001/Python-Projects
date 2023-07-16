'''Finding the max in a list - Write a recursive function that receives a non-empty list of integers and returns the value of the maximum element in the list. Enforce the precondition that the list be non-empty. Count the number of recursive calls made by the function.
Palindrome - Write a recursive function that receives a string and returns True if it is a palindrome, and False otherwise. Enforce the precondition on the parameter. Count the number of recursive calls made by the function.
'''

def list_max(lst):
	assert type(lst) == list, 'a is not list'
	assert lst != [], 'a is empty list'
	if len(lst) == 1:
		return lst[0]

	else:
		return max(lst[1],list_max(lst[2:]))

a=[1,2,3,4,5]
print(list_max(a))
			

# def rec_reverse(s):
# 	if len(s) == 1:
# 		return s[0]
# 	else:
# 		return s[-1]+rec_reverse(s[:-1])

# b='abcde'
# print(rec_reverse(b))

# def is_palindrome(s):
# 	return s == rec_reverse(s)

# print(is_palindrome(b))

''' neeche wala palindrome ka dusra tarika hai'''
def is_palindrome1(s):
	if len(s)<=1:
		return True
	else:
		a=s[0] 
		b=s[-1]
		return a==b	and is_palindrome(s[1:-1])

print(is_palindrome('naman'))

# result = True
count_frames=0
def is_sorted(lst):
	global count_frames
	
	if len(lst) <=1:
		return True
	else:
		count_frames +=1
		return lst[0] <= lst[1] and is_sorted(lst[1:])

l=[1,2,3,4,5,6,7]
print(is_sorted(l))
print(count_frames)

''' isse ek trick banta hai ki jab bhi recursion ka output boolean ho to ye structure kam karega'''




def gcd(a,b):
	if a == 0:
		return b
	elif b== 0:
		return a	
	else:
		r=a%b
		gcd(b,r)

def gcd1(a,b):
	if a == 0:
		return b
	else:
		a,b=b%a,a
		return gcd(a,b)	