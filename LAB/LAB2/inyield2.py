def give_receive(n):
	"""
	Receives n values as input and prints them each out.

	This function is a coroutine and the data is sent via a 
	send method on the generator object.

	Parameter n: The number of messages to receive
	Precondition: n is an int >= 0
	"""
	for x in range(n):
		# Give x to the parent function, receive the value sent by the parent
		value = (yield x)
		print("Coroutine received value "+repr(value))