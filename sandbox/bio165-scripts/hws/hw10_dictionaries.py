import sys

"""
# * Capitalizing DNA Sequences 
Write a small python program that takes in one system argument: a DNA sequence. 
You will convert that sequence to uppercase and print out the changed sequence. 
In this example you can assume the user will enter a valid DNA sequence that can consist of both upper or lowercase letters. 
You should use a dictionary to do the conversion. 
The dictionary should have four keys, each one a lowercase letter, and store the uppercase version of the letter as the value.
You may not use string.upper(), string.replace(), or regular expressions anywhere in your program.
You must call your dictionary “caps”.
"""

dna_seq = sys.argv[1]
caps = {}

for nuc in dna_seq:
    if nuc == "a":
        caps["a"] = "A"
        print(caps["a"], end="")
    elif nuc == "g":
        caps["g"] = "G"
        print(caps["g"], end="")
    elif nuc == "c":
        caps["c"] = "C"
        print(caps["c"], end="")
    elif nuc == "t":
        caps["t"] = "T"
        print(caps["t"], end="")
    else:
        print(nuc, end="")

print()

"""
# * Printing Genome Name & Size
For this practice, your program will take two system arguments: a genomes file, and a genome name. 
This a file that has genomes with their genome size, separated by a tab. 
You should open the genomes file and programmatically create a dictionary with keys that are the genome names
and the value is the genome size. Using the system argument of the genome name, 
retrieve the genome size from the dictionary and print it to the screen. 
You must use a dictionary called "genomes" for this exercise. 
"""

genome_file = sys.argv[1]
genome_name = sys.argv[2]
genomes = {}

with open(genome_file) as inf:
    for line in inf:
        line = line.strip().split("\t")
        genomes[line[0]] = line[1]

if genome_name in genomes:
    print(genomes[genome_name])

"""
Your program should accept three system arguments: the paths to two fasta files and the path to the output fasta file. 
Each of these files have sequences with the same header lines. For each sequence, convert it to uppercase, 
take the sequence from the second file and concatenate it to the sequence from file one. 
Next, print out the resulting header lines and uppercase sequence to a file. 
The sequence should all be written on the same line, and the header lines should not be changed 
(i.e., do not convert the header lines to uppercase).
You must use a dictionary called "headers" for this exercise and you must keep the sequences 
in the same order as they appear in the first fasta file 
(remember, you cannot assume that key:value pairs in a dictionary remain in the same order as inserted).
"""

infile1 = sys.argv[1]
infile2 = sys.argv[2]
outfile = sys.argv[3]

headers = {} # Dictionary to store concatenated sequences, keyed by header
order = [] # List to remember the order headers appeared in file1

with open(infile1) as inf1, open(infile2) as inf2, open(outfile, "w") as outf: # Open all three files at once
    for line1, line2 in zip(inf1, inf2): # Read both input files line by line at the same time
        if line1.startswith(">"): # If the line is a header, record it
            header = line1.strip()
            order.append(header) # remember the order
            headers[header] = "" # create an empty entry for this header
        else: # If the line is a sequence, concatenate and convert to uppercase
            seq1 = line1.strip()
            seq2 = line2.strip()
            combined = seq1 + seq2
            headers[header] = combined.upper()

    # Write to the output file in the original order
    for header in order:
        outf.write(f"{header}\n")
        outf.write(f"{headers[header]}\n")
