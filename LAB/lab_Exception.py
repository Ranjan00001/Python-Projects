# Question 1

def fun(a):
    if a < 4:
        b = a/(a-3)  
    print("Value of b = ", b)

try:
    fun(3)
except NameError:
    print('b does not exist')
except ZeroDivisionError:
    print('Zero divison')
    
 
# Question 2
class Error(Exception):
    """docstring for Error"""

    pass

class ZError(Error):
    '''raises error when value entered is 0
    '''
    pass

class RError(Error):
    """raises error when value entered is negative
    """
    pass

if __name__ == '__main__':
    try:
        num = int(input("Enter a number: "))
    except ValueError:
        print('enter int convertible values, using num = 1')
        num = 1
    if num == 0:
        raise ZError(' is zero', num)
    elif num < 0:
        raise RError(' is negative', num)

# Question 3

class MyError(Exception):
 
    # Constructor or Initializer
    def __init__(self, value):
        # self.value = value
        pass
 
    # __str__ is to print() the value
    def __str__(self):
        return (repr(self.value))
 

try:
    raise(MyError(3*2))
except MyError as error:
    # print('A New Exception occurred: ', error.value)
    print(error.args[0])
