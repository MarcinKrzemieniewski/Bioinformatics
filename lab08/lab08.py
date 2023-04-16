from pathlib import Path
import math

DIR = Path('data/blocks')

aminoacids = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'R', 'S', 'T', 'Q', 'W', 'Y', 'V']

def frequencies(amino):
	total = 0
	freq = 0
	for file in DIR.iterdir():
		fh = open(file)
		for line in fh:
			for char in line:
				total += 1
				if char == amino:
					freq += 1
		fh.close()
	frequency = freq/total
	return frequency

def expected_freq(A, B):
	expected = frequencies(A) * frequencies(B)
	return expected

def observed_nsubs(A, B):
	all_observed_nsubs = 0
	if A != B:
		for file in DIR.iterdir():
			protein_list = []
			obsubs = 0
			fh = open(file)
			for line in fh:
				protein_list.append(line.rstrip())
			fh.close()
			for i in range(len(protein_list[0])):
				asubs = 0
				bsubs = 0
				for protein in protein_list:
					if protein[i] == A:
						asubs += 1
					if protein[i] == B:
						bsubs += 1
				obsubs += asubs * bsubs
			all_observed_nsubs += obsubs
	else:
		for file in DIR.iterdir():
			protein_list = []
			obsubs = 0
			fh = open(file)
			for line in fh:
				protein_list.append(line.rstrip())
			fh.close()
			for i in range(len(protein_list[0])):
				asubs = 0
				bsubs = 0
				for protein in protein_list:
					if protein[i] == A:
						asubs += 1
				obsubs += (asubs *(asubs-1))/2
			all_observed_nsubs += obsubs
	return all_observed_nsubs

def observed_fsubs(A, B):
	lower = 0
	all_observed_fsubs = 0
	for file in DIR.iterdir():
		protein_list = []
		obsubs = 0
		fh = open(file)
		for line in fh:
			protein_list.append(line.rstrip())
		fh.close()
		lower += len(protein_list[0]) * (len(protein_list)*(len(protein_list)-1)/2)
	all_observed_fsubs = observed_nsubs(A, B) / lower
	return all_observed_fsubs

def matrix_scores(A, B):
	score = 2 * math.log(observed_fsubs(A, B)/expected_freq(A, B), 2)
	score = score // 1
	return int(score)

def matrix():
	print(4*' ', end='')
	for aminoacid1 in aminoacids:
		print(aminoacid1, end='   ')
	print('\n')
	for i in range(len(aminoacids)):
		print(aminoacids[i], end=' ')
		for j in range(len(aminoacids)):
			kasztany = matrix_scores(aminoacids[i], aminoacids[j])
			if kasztany < 0:
				print('', kasztany, end=' ')
			else:
				print(' ', kasztany, end=' ')
		print('\n')

matrix()