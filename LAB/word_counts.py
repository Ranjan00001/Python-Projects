def wordcount(filename):
	'''
	'''
	file = open(filename)
	text = file.read()
	file.close()
	dix = {}
	word = ''
	for x in text:
		if x.isalpha():
			word += x

		else:
			if word != '':
				add_word(dix, word)
			word = ''
	if word != '':
		add_word(dix, word)
	return dix

def add_word(dix, word):
	'''
	'''
	if word not in dix:
		dix[word] = 1
	else:
		dix[word] += 1

def loadfile(filename):
	'''
	'''
	res = wordcount(filename)
	print('Read a total of '+str(len(res)))


def wordcount1(filename):
	'''
	'''
	file = open(filename)
	text = file.read()
	file.close()
	dix = {}
	word = ''
	for pos in range(len(text)):
		if pos % (len(text)//10) == 0:
			yield round(100*pos/len(text))  # here % of work is yielded

		x = text[pos]
		if x.isalpha():
			word += x

		else:
			if word != '':
				add_word(dix, word)
			word = ''
	if word != '':
		add_word(dix, word)
	return dix

def loadfile1(filename):
	'''
	'''
	loader = wordcount1(filename)

	while not loader is None:
		try:
			a = next(loader)
			print('Loaded '+str(a)+'% of file')
		except StopIteration as e:
			res = e.args[0]
			loader = None
	print('Read a total of '+ str(len(res))+' words')


def loadfile2(filename1, filename2):
	'''
	'''
	loader1 = wordcount1(filename1)
	loader2 = wordcount1(filename2)

	res = {}
	while not loader1 is None and not loader2 is None:
		try:
			a = next(loader1)
			print('Loaded '+str(a)+'% of file1')
		except StopIteration as e:
			res = e.args[0]
			loader1 = None

		try:
			a = next(loader2)
			print('Loaded '+str(a)+'% of file2')
		except StopIteration as e:
			res = e.args[0]
			loader2 = None

	print('Read a total of '+ str(len(res))+' words')

if __name__ == '__main__':
	# print(wordcount('gandhi.txt') == wordcount1('gandhi.txt'))
	loadfile2('gandhi.txt', 'vivekanand.txt')