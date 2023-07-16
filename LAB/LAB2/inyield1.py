"""
A module to demonstrate a yield expression (not a statement)

A yield expression receives data instead of sending it as output
You write the word yield in parenthesis and assign it to a value
"""

def receive(n):
	"""
	Receives n values as input and prints them each out.

	This function is a coroutine and the data is sent via a
	send method on the generator object.

	Parameter n: The number of messages to receive
	Precondition: n is an int >=0
	"""
	for a in range(n):
		# receive the value sent
		value = (yield)
		print("Coroutine received value "+repr(value))