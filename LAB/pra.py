my_list=[11,22,33,44,55]
my_iter = iter(my_list)
for i in my_iter:
	
	if i % 2 != 0:
		print(next(my_iter))
	print(i)
