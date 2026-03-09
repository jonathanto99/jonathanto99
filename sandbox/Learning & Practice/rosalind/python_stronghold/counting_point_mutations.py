# Problem 5: Counting and comparing point mutations in a homologous sequence of DNA

# Pseudocode:
'''
1. Open the file, read the lines for the two homologous DNA sequences and store the nucleotides of each DNA sequence 
2. Compare the nucleotides of each DNA sequence to mark any difference between them
3. Count the number of different nucleotides between the DNA sequences and store it as Hamming distance
4. Print the Hamming distance
''' 
# Program: 
dna_seq = [] # Empty list for dna sequence
hamming_distance = 0 # Hamming distance set to 0 to be added to

with open("rosalind_hamm.txt") as point_mutations: # opens the file
    for line in point_mutations: # Reads it line by line
        dna_seq.append(line.strip()) # Adds the lines to the list individually

seq1 = dna_seq[0] # The first DNA sequence is at the 0 index
seq2 = dna_seq[1] # The next DNA sequence is at the 1 index
    
for n1, n2 in zip(seq1, seq2): # Loops through and compare the nucleotides in each sequence
    if n1 != n2: # If each nucleotide in seq1 is not the same as its homologous nucleotide in seq2
        hamming_distance += 1 # Hamming distance increases by 1

print(hamming_distance) # Print the hamming distance