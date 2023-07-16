class employee(object):
	"""
	represents information for salaried employee in a company

	has attribute for name, start, salary
	
	"""
	# HIDDEN INSTANCE ATTRIBUTES
	# Attribute _name:name of employee
	# Invariant : not a empty string 

	# Attribute _start: year when employee was hired
	# Invariant: int, year>1970, -1(undefined)

	# Attribute _salary: annual salary the employee is getting
	# Invariant: int, >0

	def getName(self):
		'''
		returns the employee's name
		name is non-empty string
		'''
		# gives access to read the attribute _name of object of class employee

		return self._name

	def setName(self,a):
		'''
		sets the new name to

		parameter a: the new name of employee 
		precondition: non-empty string
		'''
		# gives access to re-write the attribute _name of object of class employee
	
		assert type(a) == str, repr(a)+'is not a string'
		assert a != '', repr(a)+'is an empty string'
		self._name = a

	def getStart(self):
		'''
		returns the employee's year of joining
		'''
		# gives access to read the attribute _start of object of class employee
		
		return self._start

	def setStart(self,b):
		'''
		sets the start year to b

		parameter b: the new year of joining
		precondition: b is an int, >1970 or -1 if undefined
		'''
		# gives access to re-write the attribute _start of object of class employee

		assert type(b) == int, repr(b)+'is not an int'
		assert b >= 1970 or b == -1, repr(a)+'joining year is an invalid year'
		self._start = b

	def getSalary(self):
		'''
		returns the employee's annual salary
		'''
		# gives access to read the attribute _salary of object of class employee

		return self._salary

	def setSalary(self,c):
		'''
		sets salary to c

		parameter c: the new salary given to employee
		precondition: c is an positive int
		'''
		# gives access to re-write the attribute _salary of object of class employee

		assert type(c) == int, repr(c)+'is not an int'
		assert c >= 0, repr(c)+'is below 0'
		self._salary = c


	def __init__(self, a, b = -1, c = 50000):
		'''
		forms an instance of type Employee

		parameter a: name of employee
		precondition: non-empty string

		parameter b: joining year of employee, default value is -1(in case of undefined)
		precondition: year >= 1970, and should be of int type

		parameter c: salary of employee that he/she is getting, default value is 50000
		precondition: int type data 

		'''
		self.setName(a)
		self.setStart(b)
		self.setSalary(c)

	def __repr__(self):
		'''
		returns string unambigous representation of attribute content along with its type(class) details
		'''
		return str(self.__class__)+'('+self._name+', '+str(self._start)+', '+str(self._salary)+')'

	def __str__(self):
		'''
		returns string representation of attribute content
		'''
		return self._name+', '+str(self._start)+', '+str(self._salary)

	def get_compensation(self):
		'''
		returns compensation amount of employee's annual salary

		parameter amount: amount, which employee is getting as compensation
		precondition: int type, amount > 0
		'''
		return self._salary

class Executive(Employee):
	'''
	represents information for executive in a company
	'''
	# Attribute _bonus: bonus that executive is getting
	# Invariant: it's a positive float number 
	
	def getBonus(self):
		'''
		returns the executive's bonus
		'''
		return self._bonus

	def setBonus(self,d):
		'''
		sets bonus to d

		paremeter d:
		precondition:
		'''
		assert type(d) in (float,int), repr(d)+'is not number'
		assert d >= 0, repr(d)+'can"t be negative'
		self._bonus = d

	def __init__(self, a, b, d = 0.0): # yha salary nahi hai
		'''
		forms an instance of type Executive
		
		parameter a: name of employee
		precondition: non-empty string

		parameter b: joining year of employee, default value is -1(in case of undefined)
		precondition: year >= 1970, and should be of int type

		parameter c: salary of employee that he/she is getting, default value is 50000
		precondition: int type data 

		parameter d: bonus of the executive, default value is 0.0 
		precondition: a positive float 

		'''
		# super().__init__(a,b,50000)  # default salary 50000 liya
		super().__init__(a,b)
		self.setBonus(d)

	def get_compensation(self):
		'''
		returns compensation amount of executive's annual salary

		'''
		return self._salary+self._bonus

	def __repr__(self):
		'''
		returns unambigous representation of class executive
		'''
		# return str(self.__class__)+'('+self._name+', '+str(self._start)+', '+str(self._salary)+', '+str(self._bonus)+')'
		return str(self.__class__)+super().__str__()+', '+str(self._bonus)

	def __str__(self):
		'''
		returns str representation of executive class
		'''
		return super().__str__()+', '+str(self._bonus)

a = Employee('anjali',2017,90000)
b = Executive('shrianjali',2019,100000)