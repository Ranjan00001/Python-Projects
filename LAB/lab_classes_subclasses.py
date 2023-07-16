def isleapyear(y):
	"""
	Returns True if y is a leap year. False otherwise
	Precondition: y is an int >= 0
	"""
	if y % 4 == 0:
		if y % 100 == 0:
			if y % 400 == 0:
				return True
			return False
		return True

class Date(object):
	"""A class representing a month, day and year
	Attribute MONTHS: A CLASS ATTRIBUTE list of all month abbreviations in order
	Attribute DAYS: A CLASS ATTRIBUTE that is a dictionary. Keys are the strings from MONTHS; values are days in that month ('Feb' is 28 days)"""
	
	# Hidden Attributes
	# Attribute _year: The represented year. An int >= 2000 (IMMUTABLE)
	# Attribute _month: The month. A valid 3-letter string from MONTHS (IMMUTABLE)
	# Attribute _day: The day. An int representing a valid day of _month (MUTABLE)

	# CLASS ATTRIBU TES
	MONTHS = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
	
	DAYS = {'Jan':31,'Feb':28,'Mar':31,'Apr':30,'May':31,'Jun':30,'Jul':31,'Aug':31,'Sep':30,'Oct':31,'Nov':30,'Dec':31}

	# DEFINE GETTERS/SETTERS/HELPERS AS APPROPRIATE. SPECIFICATIONS NOT NEEDED.

	@property
	def year(self):
		"""Returns the year of this date"""
		return self._year

	@property
	def month(self):
		"""Returns the month of this date"""
		return self._month

	@property
	def day(self):
		"""Returns the day of this date"""
		return self._day
 
	@day.setter
	def day(self, value):
		"""Sets the day of this date
		Parameter value: The new day
		Precondition: value is a valid day in the month
		"""
		if not isinstance(value, int):
			raise ValueError(value, 'is not a float')

		if isleapyear(self.year) and self.month == 'Feb':
			assert 1 <= value <= 29

		else: 
			assert 1 <= value <= Date.DAYS[self.month]

		self._day = value


	def __init__(self, y, m, d):
		"""
		Initializes a new date for the given month, day, and year

		Precondition: y is an int >= 2000 for the year
		Precondition: m is a 3-letter string for a valid month
		Precondition: d is an int and a valid day for month m
		"""
		assert isinstance(y, int)
		assert y >= 2000
		assert m in Date.MONTHS
		self._year = y
		self._month = m
		self.day = d


	def __str__(self):
		"""
		Returns a string representation of this date.
		The representation is month day, year like this: 'Jan 2, 2002'
		"""
		return str(self.month)+' '+str(self.day)+', '+str(self.year)
		

	def __lt__(self, other):
		"""Returns True if this date happened before other (False otherwise)

		Precondition: other is a Date

		This method causes a TypeError if the precondition is violated."""

		# IMPORTANT: You are limited to 20 lines. Do NOT brute force this.
		if not isinstance(other, Date):
			raise TypeError('invalid type')
		# return self.year <= other.year and self.month < other.month or self.day < other.day
		if self.year < other.year:
			return True
		elif self.year == other.year and Date.MONTHS.index(self.month) < Date.MONTHS.index(other.month):
			return True
		elif self.month == other.month and self.day < other.day:
			return True
		else:
			return False


class DateTime(Date):

	"""A class representing a month, day and year, plus time of day (hours, minutes)"""

	# Hidden Attributes
	# Attribute _hour: The hour of the day. An int in range 0..23 (MUTABLE)
	# Attribute _minute: The minute of the hour. An int in range 0..59 (MUTABLE)

	# DEFINE GETTERS/SETTERS/HELPERS AS APPROPRIATE. SPECIFICATIONS NOT NEEDED.

	@property
	def hour(self):
		"""Returns the hour of the day"""
		return self._hour

	@hour.setter
	def hour(self, value):
		"""Sets the hour of the day
		Parameter value: The new hour
		Precondition: hour is an int in 0..23"""
		assert type(value) == int and 0 <= value <= 23, str(value)+'is invalid'
		self._hour = value

	@property
	def minute(self):
		"""Returns the minute of the minute"""
		return self._minute

	@minute.setter
	def minute(self, value):
		"""
		Sets the hour of the day
		Parameter value: The new minute
		Precondition: hour is an int in 0..23
		"""
		assert type(value) == int and 0 <= value <= 23, str(value)+'is invalid'
		self._minute = value 

	def __init__(self, y, m, d, hr, mn): # Fill in missing part
		"""
		Initializes a new datetime for the given month, day, year, hour and minute
		This method adds two additional (default) parameters to the initialize for
		Date. They are hr (for hour) and mn (for minute).
		Precondition: y is an int >= 2000 for the year
		Precondition: m is a 3-letter string for a valid month
		Precondition: d is an int and a valid day for month m
		Precondition: hr is an int in the range 0..23 (OPTIONAL; default 0)
		Precondition: mn is an int in the range 0..59 (OPTIONAL; default 0)
		"""
		super().__init__(y, m, d)
		self.hour = hr
		self.minute = mn


	def __str__(self):
		"""
		Returns a string representation of this DateTime object
		The representation is 'hh:mm on month day, year' like this: '9:45 on Jan 2, 2002'
		Single digit minutes should be padded with 0s. Hours do not need to be padded.
		"""
		return str(self.hour)+':'+str(self.minute)+' on '+super().__str__()

d = Date(2000,'Feb',19)
# print(str(d))
e = Date(2000, 'Jan', 20)
# print(d<e)
# print(isleapyear(2016))
f = DateTime(2000, 'Mar', 19, 6, 20)
# print(str(f))
# print(type(()))