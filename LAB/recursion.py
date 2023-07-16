# def factorial(n):
# 	try:
# 		if n < 0:
# 			return 1/0
# 		elif n == 0:
# 			return 1		
# 		return n*factorial(n-1)
# 	except:
# 		return repr(n)+' is not a positive integer'

# print(factorial(1))

# def reverse(s):
# 	try:
# 		if len(s) == 0:
# 			return ''
# 		return s[-1] + reverse(s[:-1])
# 	except:
# 		return repr(s) +' is not a string'

# print(reverse('dasveb'))

# count = 0
# def find_substring(string,sub_str):
# 	global count
# 	try:
# 		if not (sub_str in string):
# 			return -1
# 		elif string[:len(sub_str)] == sub_str :
# 			print('elif')
# 			return count
# 		# else:
# 		print('else')
# 		count += 1
# 		find_substring(string[1:],sub_str)
# 		return count
# 	except:
# 		return -1

# s = 'qwewqwrty'
# print(find_substring(s,'ty'))


count = 0
def occurence(string,character):
	global count
	try:
		if not (character in string):
			return count
		else:
			a = string.find(character)
			# print(a)
			count += 1
			occurence(string[a+1:],character)
			return count
	except:
		return repr(character)+' is not a string'

s = 'qwewqwrty'
print(occurence(s,'qw'))

def long_comm_prefix(lst):
	n = list(map(len,lst))
	print(n)
	m = min(n)
	o = [i for i in lst if len(i) == 2]
	print(o)

lst = ['df', 'ghdfg', 'dsfg']
long_comm_prefix(lst)