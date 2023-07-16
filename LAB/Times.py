class time:
	"""
	hour and minute are attribute
	"""
	def getHour(self):
		return self._hour

	def setHour(self, h):
		assert type(h) == int
		assert 0 <= h and h < 24
		self._hour = h

	def __init__(self, hour, minute):
		assert type(hour) == int
		assert 0 <= hour < 24
		assert type(minute) == int
		assert 0 <= minute < 60

		self._hour = hour
		self._minute = minute

	def increment(self, hours, mins):
		assert type(hours) == int
		assert type(mins) == int
		assert hours >= 0
		assert 0 <= mins < 60

		self.minute+= mins
		self.hour += hours + self.minute//60
		# if self.hour > 23:
		self.hour = self.hour%24
		# if self.minute > 23:
		self.minute = self.minute%60

	# def increment1(self, other):
	# 	self.minute+= other.minute
	# 	self.hour += other.hour + self.minute//60
	# 	# if self.hour > 23:
	# 	self.hour = self.hour%24
	# 	# if self.minute > 23:
	# 	self.minute = self.minute%60

	# def increment2(self, others):
		# others.hour += 24

	def __repr__(self):
		return str(self.__class__)+'('+str(self.hour)+', '+str(self.minute)+')'

	def _is_minute(self,m):
		return (type(m) == int and m >= 0 and m < 60)


# a = time(12,30)
# # a.increment(2,308)
# b = a
# # print(b == a)
# # print(a.hour, b.hour,a.minute, b.minute)

# c = time(13,40)
# a.increment1(c)
# print(a.hour,a.minute)

# # a.increment2(c)
# # print(c.hour)