"""
A module with a simple 2x2 matrix

This module contains both a 2D point and a 
2x2 matrix that we can multiply with a point
"""
import math

class Point2(object):
    
    """
    An instance is a point in 2D space.
    """
    
    def getX(self):
	    """
		Gets x coordinate
		"""
	    return self._x

    def setX(self, value):
    	"""
    	Sets x coordinate.

    	Parameter value: the value to assign to x
    	Precondition: value is an int or float
    	"""
    	assert type(value) in [int,float], repr(value)+' is neither an int nor float'
    	self._x = float(value)

    def getY(self):
    	"""
    	Gets y coordinate
    	"""
    	return self._y

    def setY(self, value):
    	"""
    	Sets y coordinate.

    	Parameter value: the value to assign to y
    	Precondition: value is an int or float
    	"""
    	assert type(value) in [int,float], repr(value)+' is neither an int nor float'
    	self._y = float(value)


    # BUILT_IN METHODS
    def __init__(self, x=0, y=0):
        """
        All attribute values are 0.0 by default.
        
        :param x: initial x value
        :type x:  ``int`` or ``float``
            
        :param y: initial y value
        :type y:  ``int`` or ``float``
        """
        self.setX(x)
        self.setY(y)
    
    def __add__(self, other):
        """
        Returns a new point that is the sum of this and other

        This method should not alter the contents of either self or other

        Parameter other: point to be added
        Precondition: other is a Point2 object
        """
        assert (type(other) == Point2), "Illegal addition"
        return Point2(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        """
        Returns True if other is a Point2 with same 
        contents as this one; False otherwise

        Parameter other: the point to compare
        Precondition: other can be anything
        """
        return (type(other) == Point2 and 
        	self._x == other._x and 
        	self._y == other._y)

    def __str__(self):
    	"""
    	Returns a string representation of this point
    	"""
    	return '('+str(self.getX())+', '+str(self.getY())+')'
    
    def __repr__(self):
    	"""
    	Returns a string representation of this point
    	"""
    	return self.__str__()


class Matrix(object):
	"""
	Class representing 2x2 matrices

	The matrix has 4 attributes: a,b,c,d
	It represents matrix of the form
	   a   b
	   c   d

	It is a immutable object
	"""
	def getA(self):
		"""
		The top left value of the matrix

		Invariant: the value is a float. This is
		immutable and may not be altered.
		"""
		return self._a

	def getB(self):
		"""
		The top right value of the matrix

		Invariant: the value is a float. This is
		immutable and may not be altered.
		"""
		return self._b

	def getC(self):
		"""
		The bottom left value of the matrix

		Invariant: the value is a float. This is
		immutable and may not be altered.
		"""
		return self._c

	def getD(self):
		"""
		The bottom right value of the matrix

		Invariant: the value is a float. This is
		immutable and may not be altered.
		"""
		return self._d

	def __init__(self,a=1,b=0,c=0,d=1):
		"""
		Initializes a new Matrix [[a,b],[c,d]]

		Parameter a: initial a value, defaults to 1
		Precondition: a is a number (int/float)

		Parameter b: initial a value, defaults to 0
		Precondition: b is a number (int/float)
    
    	Parameter c: initial a value, defaults to 0
		Precondition: c is a number (int/float)

		Parameter d: initial a value, defaults to 1
		Precondition: d is a number (int/float)
 		"""
		self._a = float(a)
		self._b = float(b)
		self._c = float(c)
		self._d = float(d)

	@classmethod
	def createRotation(clas,angle=0):
		"""
		Creates a new matrix for rotation

		A rotation matrix will rotate space about
		the origin

		Parameter angle: The rotation angle in degrees
		Precondition: angle is a number (int or float)
		"""
		radians = math.pi*angle/180.0
		c = math.cos(radians)
		s = math.sin(radians)
		# return Matrix(c,-s,s,c)
		return clas(c,-s,s,c)

	def __str__(self):
		"""
		Returns a string representation of this matrix
		"""
		return '|'+str(self.getA())+' '+str(self.getB())+'|'+"\n"+'|'+str(self.getC())+' '+str(self.getD())+'|'
    
	def __repr__(self):
		"""
		Returns a string representation of this point
		"""
		return self.__str__()
a = Matrix.createRotation(60)
print(a)