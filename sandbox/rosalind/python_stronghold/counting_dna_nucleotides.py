# Problem 1: Counting DNA Nucleotides

# Bro I know what DNA and nucleotides are already

# Program:
raw_text = open("rosalind_dna.txt", "r").read() # This loads the file's content and makes it readable
A = raw_text.count("A") # Counting the number of A's in the string
C = raw_text.count("C") # Counting the number of C's in the string
G = raw_text.count("G") # Counting the number of G's in the string
T = raw_text.count("T") # Counting the number of T's in the string
print(A, C, G, T) # Printing out the counts of A, C, G, and T in that order
