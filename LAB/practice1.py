def head(l):
	if len(l)%2 == 0:
		for i in range(len(l)):
			if i%2 != 0:
				# print(i)
				l[i-1],l[i]=l[i],l[i-1]
	else:
		a=l[len(l)//2]
		l.remove(l[len(l)//2])			
		head(l)
  		l.insert(len(l)//2, a)
	return l
	
a=[1,2,3,4,5]
print(head(a))

''' yaha ek danger hai ki jab bhi loop me range ka use kare to element uthate vaqt dhyan rakhe'''
