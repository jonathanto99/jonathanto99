# Problem 3: Complementing a Strand of DNA

# Program:
dna_strand = open("rosalind_revc.txt").read() # Read the DNA strand from the file
dna_strand_reversed = dna_strand[::-1] # Reverse the DNA strand
dna_strand_complement = [] # Initialize an empty list to store the complement nucleotides

for nucleotide in dna_strand_reversed: # Iterate through each nucleotide in the reversed DNA strand
    if nucleotide == "A": 
        dna_strand_complement.append("T")
    elif nucleotide == "T":
        dna_strand_complement.append("A")
    elif nucleotide == "C":
        dna_strand_complement.append("G")
    elif nucleotide == "G":
        dna_strand_complement.append("C")

dna_strand_complement = "".join(dna_strand_complement) # Join the list into a string
print(dna_strand_complement) # Print the resulting complementary DNA strand
