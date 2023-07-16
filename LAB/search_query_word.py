

def search(s1,s2):
	lst1 = s1.split()
	lst2 = s2.split()
	count1 = 0
	count2 = 0
	for i in lst1:
		if i.strip(',./!@#') == query_word:   # stripped some common special characters 
			count1 +=1
	for i in lst2:
		if i.strip(',./!@#') == query_word:
			count2 +=1
	if count1 > count2:
		return 'First' 
	elif count1 < count2:
		return 'Second'
	else:
		return 'both'

s1 = input('enter first string: ')
s2 = input('enter Second string: ')
query_word = input('enter query word: ')
if __name__ == '__main__':
	print(search(s1,s2))



				