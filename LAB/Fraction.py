class Fractions(object):
	'''
	instance is a fraction n/d
	'''
	# _num has type int
	# _denom is of type int

	def __init__(self, n, d):
		self._num = n
		self._denom = d

	# @property
	# def numerator(self):
	# 	return self._numerator
	
	def getNum(self):
		return self._num

	def setNum(self,value):
		assert type(value) == int, repr(value)+' is not an int'
		self._num = value

	def getDenom(self):
		return self._denom

	def setDenom(self,value):
		assert type(value) == int, repr(value)+' is not an int'
		assert value > 0, repr(value)+' is not positive'
		self._denom = value

	def __str__(self):
		return str(self._num)+'/'+str(self._denom)

	def __repr__(self):
		return str(self.__class__)+str(self._num)+'/'+str(self._denom)

	def __add__(self, other):
		assert isinstance(other, Fractions), repr(other)+' is not a Fractions'
		n = self._num*other._denom+other._num*self._denom
		d = self._denom*other._denom
		# assert type(n) == int, repr(n)+'is not an int'
		# assert type(d) == int, repr(d)+'is not an int'
		return Fractions(n,d)

# yad rakhe ki self._num ke jagah self.getNum() kare
	def __mul__(self, other):
		# assert isinstance(other, Fractions) or isinstance(other, int), repr(other)+' is not valid'

		if isinstance(other, Fractions):
			n = self._num*other._num
			d = self._denom*other._denom
		elif isinstance(other, int):
			n = self._num*other
			d = self._denom
		return Fractions(n,d)

	def __rmul__(self, other):
		assert isinstance(other, Fractions) or isinstance(other, int), repr(other)+' is not valid'
		if isinstance(other, Fractions):
			n = self._num*other._num
			d = self._denom*other._denom
		elif isinstance(other, int):
			n = self._num*other
			d = self._denom
		return Fractions(n,d)


	def __eq__(self, other):
		# assert type(other) == Fractions, repr(other)+' is not a Fractions'
		if not(hasattr(other,'_num') and hasattr(other,'_denom')):
			return False
		return self.getNum()*other.getDenom() == other.getNum()*self.getDenom()

	def __lt__(self, other):
		assert type(other) == Fractions, repr(other)+' is not a Fractions'
		return self.getNum()*other.getDenom() < other.getNum()*self.getDenom()

	def __le__(self, other):
		assert type(other) == Fractions, repr(other)+' is not a Fractions'
		return self.getNum()*other.getDenom() <= other.getNum()*self.getDenom()

	# def __gt__(self, other):
	# 	assert type(other) == Fractions, repr(other)+' is not a Fractions'
	# 	return self.getNum()*other.getDenom() > other.getNum()*self.getDenom()

	# def __ge__(self, other):
	# 	assert type(other) == Fractions, repr(other)+' is not a Fractions'
	# 	return self.getNum()*other.getDenom() >= other.getNum()*self.getDenom()

	# these overloaded operators need not to have same specifications, it may varies by different class

	# always use is operator if u are confused between compairing of folder name and operators overloading
# p = Fraction.Fractions(1,2)
# q = Fraction.Fractions(2,4)
# p.multiply

# prperty decorator is used for getter method