class Question(object): 		# Fill in missing part
	"""
	A class representing a question in the lab system
	
	Attribute USED_INDICES: A CLASS ATTRIBUTE list of all question indices.
	This list starts off empty, as there are no questions to start with.
	"""

	# ATTRIBUTE _index: The question index. An int > 0 (IMMUTABLE)
	# ATTRIBUTE _text: The question wording. A nonempty string (MUTABLE)

	# CLASS ATTRIBUTE. NO GETTERS OR SETTERS.
	USED_INDICES = []

	# DEFINE GETTERS/SETTERS/HELPERS AS APPROPRIATE. SPECIFICATIONS NOT NEEDED.
	
	@property 
	def index(self):
		return self._index
	
	@property
	def text(self):
		return self._text
	
	@text.setter
	def text(self, b):
		assert isinstance(b, str) and b != '', repr(b)+'is invalid'
		self._text = b


	def __init__(self, a, b):
		"""
		Initializes a new question for the given index and text.
		No question can share the same index as another. On creation, the question index is added to the class attribute USED_INDICES.

		Precondition: index is an int > 0, and not already in use.
		That is, index cannot be an element of USED_INDICES.
		Precondition: text is a non-empty string
		"""
		assert not a in Question.USED_INDICES, repr(a)+' is already in use'
		self._index = a
		self.text = b
		Question.USED_INDICES.append(a)

	def __str__(self):			# Fill in missing part
		"""
		Returns a string representation of this question.

		The format is '<index>. <text>'.

		Example: If index is 2 and the text is 'What is your quest?',
		this method will return '2. What is your quest?' 
		"""
		return "'" + str(self.index) + ". " + str(self.text) + "?'"

	def __eq__(self, other):		 # Fill in missing part
		"""
		Returns True if self and other are equal. False otherwise.

		An object is equal to this one (self) if it has the same type and the same index.
		You do not need to compare text, since indices are unique.
		Precondition: NONE. other can be ANYTHING
		"""
		return isinstance(other, Question) and self.index == other.index



class MCQ(Question):			# Fill in missing part
	"""A class representing a multiple choice question."""

	# ATTRIBUTE _choices: The options. A nonempty tuple of strings. (MUTABLE)
	# ATTRIBUTE _correct: The index of the correct answer. An int. (MUTABLE)
	# ADDITIONAL INVARIANT: _correct is a valid index of _choices at all times
	# HINT: This allows _correct to be negative as long as it is in bounds
	
	# DEFINE GETTERS/SETTERS/HELPERS AS APPROPRIATE. SPECIFICATIONS NOT NEEDED.
	
	@property
	def choices(self):
		return self._choices
	
	@property
	def correct(self):
		return self._correct
	
	# def correct_inv(a):
	# 	result = isinstance(a, tuple) and a != ()
	# 		# result = True
	# 	for i in a:
	# 		result = isinstance(i, str)
	# 	return result
		

	@choices.setter
	def choices(self, value):
		assert isinstance(value, tuple) and value != (), repr(value) + 'is invalid'
		self._choices = value

	@correct.setter
	def correct(self, value):
		assert isinstance(value, int), repr(value)+' is not an int'
		assert value, repr(value)+' is invalid'
		self._correct = value


	def __init__(self, a, b, c, d):
		"""
		Initializes a new multiple choice question with given choices.

		Precondition: index is an int > 0, and not already in use.
		That is, index cannot be an element of USED_INDICES in Question.
		Precondition: text is a non-empty string
		Precondition: choices is a nonempty tuple of strings
		Precondition: correct is an int and a valid index of choices
		(OPTIONAL ATTRIBUTE; correct is -1, the last choice, by default)
		"""
		super().__init__(a,b)
		self.choices = c
		self.correct = d


	def __str__(self):
		"""
		Returns a string representation of this multiple choice question.

		The format is '<index>. <text> <answer>'. 

		For example, suppose the question with index 2 and text 'What is your quest?' has choices ('To pass this exam.', 'To seek the Holy Grail.').
		If correct is 1, then the string is '2. What is your quest? To seek the Holy Grail.'
		"""
		return super().__str__()[:-1] + " " + str(self.choices[self.correct-1]) + ".'" 


b = Question(1, 'What is your name')
d = Question(1, 'which day is today')
c = MCQ(1, 'What is your name', ('ranjan', 'kirtan'), 1)
print(str(b))
print(str(c))
print(c == b)
print(b == d)

# print(b.index)
# print(c.index)
