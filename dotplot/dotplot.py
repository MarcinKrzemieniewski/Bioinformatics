fasx = open('data/a.fasta')
fasy = open('data/b.fasta')

def sequence(file):
	chars = ''
	for line in file:
		if line.startswith('>') == False:
			for char in line:
				if char != '\n':
					chars += char.upper()
	return chars

def compare(seqx, y):
	same = []
	for char in seqx:
		if char == y:
			same.append('X')
		else:
			same.append('.')
	return same

def dotplot(x, y):
	print(' ', end = ' ')
	for char in x:
		print(char, end = ' ')
	print('')
	for char in y:
		print(char, end = ' ')
		compared = compare(seqx, char)
		for element in compared:
			print(element, end = ' ')
		print('')



seqx = sequence(fasx)
seqy = sequence(fasy)

dotplot(seqx, seqy)