# Problem 2: Transcribing DNA into RNA

# Program:
dna_sequence = open("rosalind_rna.txt").read() # Read the DNA sequence from the file
rna_sequence = dna_sequence.replace("T", "U") # Replace all occurrences of 'T' with 'U' to transcribe DNA to RNA
print(rna_sequence) # Print the resulting RNA sequence
