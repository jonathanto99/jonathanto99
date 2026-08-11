import sys

# Remove spaces from DNA sequences:
dna_seqs = sys.argv[1:]
new_list = []

for seq in dna_seqs:
    cleaned_seq = seq.replace(" ", "").upper()
    new_list.append(cleaned_seq)
new_list.sort()
print(new_list)

# Excise introns and recombine exons:
dna_seq = sys.argv[1]
positions = sys.argv[2]

pos1, pos2 = positions.split(",")
pos1 = int(pos1)
pos2 = int(pos2)

first_exon = dna_seq[:pos1]
second_exon = dna_seq[pos2-1:]

exons = first_exon + second_exon
print(exons)
