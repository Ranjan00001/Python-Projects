import math

class Point3:
  def __init__(self,x,y,z):
    self.x = x
    self.y = y
    self.z = z
   
  def __repr__(self):
        return "point.Point3(%s,%s,%s)"%(self.x,self.y,self.z)
  
  @property
  def x(self):
    return self._x 

  @x.setter
  def x(self,value):
    if not isinstance(value,int) and not isinstance(value,float):
        raise ValueError("attribute x must be an int or float.")
    self._x = float(value) 

  @property
  def y(self):
    return self._y

  @y.setter
  def y(self,value):
    if not isinstance(value,int) and not isinstance(value,float):
        raise ValueError("attribute y must be an int or float.")
    self._y = float(value) 

  @property
  def z(self):
    return self._z

  @z.setter
  def z(self,value):
    if not isinstance(value,int) and not isinstance(value,float):
        raise ValueError("attribute z must be an int or float.")
    self._z = float(value) 

  def distance(self, other):
    dx = self.x - other.x
    dy = self.y - other.y
    dz = self.z - other.z
    return math.sqrt(dx**2 + dy**2 + dz**2)

  def clamp(self,low, high):
    if self.x >= high:
      self.x = high
    elif self.x <= low:
      self.x = low

    if self.y >= high:
      self.y = high
    elif self.y <= low:
      self.y = low

    if self.z >= high:
      self.z = high
    elif self.z <= low:
      self.z = low

p = Point3(1,1,1)
# q = Point3(1,2,3)
# print(p.distance(q))
print(p.__dict__)
print(p.__class__)
# class Point3(object):
#   """Class for points in 3d space
#   Invariant: x is a float
#   Invariant y is a float
#   Invariant z is a float """

#   def __init__(self,x=0,y=0,z=0):
#     """Initializes a new Point3
#     Precond: x,y,z are numbers"""
#     self.x = x
#     self.y = y
#     self.z = z

# a = Point3(1,2,3)