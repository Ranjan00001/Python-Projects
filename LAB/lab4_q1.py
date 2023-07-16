# gives idea about defult parameter
def func(n=10):
	print('here is the nymber 1 received :',n)

func(5)
func()
'''in first function call we gave them argument so it didn't taken the default value
but during second function call we didn't gave any function signature so it taken the default value '''
 
# also remember that default parameter should come after non-deault
