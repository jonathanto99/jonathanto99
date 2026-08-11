import sys

def problem_1():
    """
    * DNA Base Frequency Counter
    
    Read a DNA sequence from the command line. Use a dictionary to count how 
    many times each base (A, T, C, G) appears in the sequence (case-insensitive). 
    Print each base and its count on a separate line, in alphabetical order. 
    
    Constraints:
    - You may not use string methods like .count()
    - You must use a dictionary called `base_counts`
    
    Expected output format:
    A: 5
    C: 3
    G: 4
    T: 6
    """

    dna_seq = sys.argv[1]
    base_counts = {
        "a" : 0,
        "g" : 0,
        "c" : 0,
        "t" : 0,
    }

    for i in dna_seq:
        if i.casefold() == "a":
            base_counts["a"] += 1
        elif i.casefold() == "g":
            base_counts["g"] += 1
        elif i.casefold() == "c":
            base_counts["c"] += 1
        elif i.casefold() == "t":
            base_counts["t"] += 1
    
    for base, count in sorted(base_counts.items()):
        print(f"{base.upper()}: {count}")


def problem_2():
    """
    * Codon Translation Table
    
    Accept a DNA sequence and a codon from the command line. Count how many 
    times that specific codon appears in the sequence (overlapping allowed, no string.count() or regex).
    Print the sequence, the codon, and the count in tab-delimited format.
    
    Expected output format:
    ATGCTGAAATGA	ATG	1
    """

    dna_seq = sys.argv[1]
    codon = sys.argv[2]
    codon_count = 0

    for i in range(len(dna_seq) -2):
        if codon == dna_seq[i:i+3]:
            codon_count += 1
    
    print(f"{dna_seq}\t{codon}\t{codon_count}")
            

def problem_3():
    """
    * Species Genome Database

    Accept two command-line arguments:
    A file path to a tab-delimited file (species name, genome size)
    A species name to look up
    Build a genomes dictionary from the file. Look up the species and print its genome size in tab-delimited format.
    
    Example command: python quiz7_prep.py species.tsv "E.coli"
    Expected output: E.coli	4600000
    """
    
    file_path = sys.argv[1]
    species_name = sys.argv[2]
    genomes_dict = {}

    with open(file_path, "r") as inf:
        for raw in inf:
            line = raw.strip().split("\t")
            genomes_dict[line[0]] = line[1]
    if species_name in genomes_dict:
        print(f"{species_name}\t{genomes_dict[species_name]}")
    else:
        print("Species not found.")


def problem_4():
    """
    * Protein ID Lookup
    
    Read a tab-delimited file with protein IDs in column 1 and descriptions 
    in column 2. Build a dictionary mapping protein IDs to their descriptions.
    
    Accept a protein ID from the command line. If the ID exists, print its 
    description. If it doesn't exist, print "Protein not found."
    
    Constraints:
    - You must use a dictionary called `protein_db`
    
    Expected output format (found):
    TP53 tumor suppressor protein
    
    Expected output format (not found):
    Protein not found.
    """
    
    file_path = sys.argv[1]
    protein_id = sys.argv[2]
    protein_db = {}

    with open(file_path, "r") as inf:
        for raw in inf:
            line = raw.strip().split("\t")
            protein_db[line[0]] = line[1]
        
    if protein_id in protein_db:
        print(f"{protein_db[protein_id]}")
    else:
        print("Protein not found.")


def problem_5():
    """
    * Mutation Counter (Multi-file)
    
    Accept two input files and one output file from the command line. 
    Each file contains a DNA sequence on each line. For each line, compare 
    the sequences from file 1 and file 2 position-by-position.
    
    Use a dictionary to count how many positions differ between the two sequences.
    Write to the output file: sequence from file 1, tab, sequence from file 2, 
    tab, number of differences.
    
    Constraints:
    - You must use a dictionary called `diff_counts`
    - Preserve the order sequences appear in file 1
    
    Expected output format:
    ATGCTG	ATGCTA	1
    GAATGA	GAATGA	0
    """
    
    input1 = sys.argv[1]
    input2 = sys.argv[2]
    output = sys.argv[3]
    diff_counts = {}

    with open(input1, "r") as inf1, open(input2, "r") as inf2, open(output, "w") as outf:
        for line1, line2 in zip(inf1, inf2):
            diff_count = 0
            line1 = line1.strip()
            line2 = line2.strip()
            key = f"{line1}\t{line2}"
            for nuc1, nuc2 in zip(line1, line2):
                if nuc1 != nuc2:
                    diff_count += 1
            diff_counts[key] = diff_count
            outf.write(f"{line1}\t{line2}\t{diff_counts[key]}\n")
