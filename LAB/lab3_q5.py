# gives viualisation about function call frame
def func1(): 
	x=5 
	print("Inside func1, before calling func2: ",x) 
	func2() 
	print("Inside func1, after calling func2: ",x) 


def func2(): 
	global x 
	x=x*2 

x=10 
print("Initial: ",x) 
func1() 
print("After func1: ",x) 
func2() 
print("After func2: ",x) 

