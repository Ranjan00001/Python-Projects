class RGB:
  def __init__(self,r,g,b):
    self.red = r
    self.green = g
    self.blue = b
  
  def __repr__(self):
        return "rgb.RGB(%s,%s,%s)"%(self.red,self.green,self.blue)
  
  @property
  def red(self):
    return self._red 

  @red.setter
  def red(self,value):
    if not isinstance(value,int):
      raise ValueError("attribute red must be an int.")
    if not (0<=value<=255):
      raise ValueError("attribute red can take values between 0 and 255.")

    self._red = value 

  @property
  def green(self):
    return self._green 

  @green.setter
  def green(self,value):
    if not isinstance(value,int):
      raise ValueError("attribute green must be an int.")
    if not (0<=value<=255):
      raise ValueError("attribute green can take values between 0 and 255.")

    self._green = value

  @property
  def blue(self):
    return self._blue 

  @blue.setter
  def blue(self,value):
    if not isinstance(value,int):
      raise ValueError("attribute blue must be an int.")
    if not (0<=value<=255):
      raise ValueError("attribute blue can take values between 0 and 255.")

    self._blue = value