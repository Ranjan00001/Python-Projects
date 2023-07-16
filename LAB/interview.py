a = [1,2,3,4,4,4,5]
b = [0,4,4,4,4,5,7,9]
acc = []
for i in b:
	# print(i)
	try:
		q = a.index(i)
		# print('q',q)
		acc.append(i)
		a.pop(q)
	except:
		continue
print(acc)

# for x in b:
# 	for y in a:
# 		if x == y:
# 			acc.append(x)
# 			q = a.index(y)
# 			a.pop(q)
# 			break
# print(acc)