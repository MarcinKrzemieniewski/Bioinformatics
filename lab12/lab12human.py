import pprint, heapq

genes = {}
trans = {}
exons = {}

f = open('new_data/lab12/Homo_sapiens.GRCh38.106.gtf')
for line in f:
	if line.startswith('#'):
		continue
	line = line.split()
	if line[2] == 'gene':
		length = int(line[4]) - int(line[3])
		geneid = line[9].rstrip(';').strip('\"') + ' ; ' + line[13].rstrip(';').strip('\"')
		genes[geneid] = length
	if line[2] == 'transcript':
		geneid = line[9].rstrip(';').strip('\"') + ' ; ' + line[17].rstrip(';').strip('\"')
		if geneid not in trans:
			trans[geneid] = 1
		else:
			trans[geneid] += 1
	if line[2] == 'exon':
		transid = line[13].rstrip(';').strip('\"') + ' ; ' + line[25].rstrip(';').strip('\"')
		if transid not in exons:
			exons[transid] = 1
		else:
			exons[transid] += 1
f.close()

longest_gene = heapq.nlargest(3, genes.values())
long_gene = {}
for key, value in genes.items():
	if value in longest_gene:
		long_gene[key] = value

largest_gene = heapq.nlargest(3, trans.values())
large_gene = {}
for key, value in trans.items():
	if value in largest_gene:
		large_gene[key] = value

largest_trans = heapq.nlargest(3, exons.values())
large_exon = {}
for key, value in exons.items():
	if value in largest_trans:
		large_exon[key] = value

print(f'#3 genes with longest genome sequence:')
pprint.pprint(long_gene)
print('#3 genes with the biggest amount of transcirpts:')
pprint.pprint(large_gene)
print('#3 transcripts with biggest amount of exons:')
pprint.pprint(large_exon)