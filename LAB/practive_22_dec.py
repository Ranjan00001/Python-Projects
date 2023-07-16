for x in range(1,4):
	for y in range(5,8):
		print([x,y])
# above is similar as
l=[[x,y] for x in range(1,4) for y in range(5,8)]# here we can also have if statement
print(l)
# this is called as list comprehension
 