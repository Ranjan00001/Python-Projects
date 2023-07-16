#this is simple addition of two variables and their rounding off to two decimal digit

x=78.2346
y=67.23

print('The value of x is {0} and that of y is  {1} and the sum is {2}'.format(x,y,'%0.2f'%(x+y)))

# above result can also be achieved by f-string
print(f"The value of x is {x} and that of y is  {y} and the sum is {'%0.2f'%(x+y)}")

# again '%0.2f'%<expression> is similar to round(expression,2)
