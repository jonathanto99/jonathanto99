# ============================================================
# BIO 165 — Functions Practice
# Practice problems for mastering Python functions.
# Each problem uses def, parameters, return values, and
# bioinformatics-themed content from BIO 165.
# ============================================================

import sys

"""
# Problem 1: GC Content Calculator (Function + Return Value)

Define a function called `calc_gc_content` that accepts a single DNA
sequence string as a parameter and RETURNS the GC content as a float
(percentage, rounded to 2 decimal places).

In the main body of your program, accept a DNA sequence from the command
line, call `calc_gc_content`, and print the result.

! Constraints:
- You must define and call a function named `calc_gc_content`
- The function must use a return statement (not print)
- You may not use string.count()
- The function must be case-insensitive

* Example command: 
python functions_practice.py ATGCGCTTAA

* Expected output: 
GC Content: 40.00%
"""

def calc_gc_content(dna_seq):
    seq_upper = dna_seq.upper()
    if len(seq_upper) == 0:
        return 0.0
    gc_count = 0
    for nuc in seq_upper:
        if nuc in ("G", "C"):
            gc_count += 1  
    return round((gc_count / len(seq_upper)) * 100, 2)

if __name__ == "__main__":
    seq = sys.argv[1] if len(sys.argv) > 1 else ""
    gc = calc_gc_content(seq)
    print(f"GC Content: {gc:.2f}%")

"""
# Transcription Function (Default Parameters)

Define a function called `transcribe` that accepts:
- A DNA sequence string (required parameter)
- A boolean `uppercase` with a default value of True

The function should return the RNA transcript (replace T with U).
If `uppercase` is True, return the result in uppercase.
If `uppercase` is False, return the result in lowercase.

In the main body, accept a DNA sequence from the command line.
Call `transcribe` twice — once with the default parameter and once
with `uppercase=False` — and print both results.

! Constraints:
- You must define a function named `transcribe` with a default parameter
- You must call the function at least twice with different argument values
- Do not use str.replace() — use a loop instead

* Example command:
python functions_practice.py ATGCTA

* Expected output: 
AUGCUA
augcua
"""

def transcribe(dna_seq, uppercase=True):
    if len(dna_seq) == 0:
        return ""
    else:
        rna_list = ["U" if nuc.upper() == "T" else nuc for nuc in dna_seq]
        rna_seq = "".join(rna_list)
        return rna_seq.upper() if uppercase else rna_seq.lower()

if __name__ == "__main__":
    dna_seq = sys.argv[1] if len(sys.argv) > 1 else ""
    upper = transcribe(dna_seq)
    lower = transcribe(dna_seq, uppercase=False)
    print(upper)
    print(lower)

"""
# Reverse Complement (Function Calling Function)

Define two functions:

1. `complement(sequence)` — returns the complement of a DNA sequence
   (A↔T, G↔C), preserving case.

2. `reverse_complement(sequence)` — calls `complement()` internally,
   then reverses the result and returns it.

In the main body, accept a DNA sequence from the command line.
Print the original sequence, its complement, and its reverse complement,
each on a separate line with a label.

! Constraints:
- `reverse_complement` must call `complement` internally
- You may not use slicing (e.g., seq[::-1]) to reverse — use a loop
- Both functions must use a return statement

* Example command:
python functions_practice.py ATGCTT

* Expected output:
Original:    ATGCTT
Complement:    TACGAA
Reverse Complement:    AAGCAT
"""

def complement(dna_seq):
    if len(dna_seq) == 0:
        return ""
    pairs = {
        "A": "T", "T": "A", "G": "C", "C": "G",
        "a": "t", "t": "a", "g": "c", "c": "g"
    }
    comp = [pairs.get(nuc, nuc) for nuc in dna_seq]
    return "".join(comp)
                

def reverse_complement(dna_seq):
    comp = complement(dna_seq)
    rev_comp = []
    for i in comp:
        rev_comp.insert(0, i)
    return "".join(rev_comp)

if __name__ == "__main__":
    dna_seq = sys.argv[1] if len(sys.argv) > 1 else ""
    if dna_seq:
        print(f"Original:\t{dna_seq}")
        print(f"Complement:\t{complement(dna_seq)}")
        print(f"Reverse Complement:\t{reverse_complement(dna_seq)}")

"""
# FASTA Sequence Lookup (Function + Dictionary + File I/O)

Define a function called `parse_fasta` that accepts a filepath as a
parameter and returns a dictionary mapping each sequence header (without
the ">") to its full sequence string.

In the main body, accept a FASTA file path and a sequence header string
from the command line. Call `parse_fasta` to build the dictionary, then
look up the given header. Print the header and sequence length if found,
or "Header not found." if it does not exist.

! Constraints:
- You must define and call a function named `parse_fasta`
- The function must return a dictionary (do not print inside the function)
- Assume sequences may span multiple lines in the FASTA file
- Strip the ">" from header keys stored in the dictionary

* Example command:
python functions_practice.py sequences.fasta "Homo_sapiens_BRCA1"

* Expected output (found):
Homo_sapiens_BRCA1: 1234 bp

* Expected output (not found):
Header not found.
"""

def parse_fasta(file_path):
    fasta_dict = {}
    current_header = None
    with open (file_path, "r") as inf:
        for line in inf:
            line = line.strip()
            if line.startswith(">"):
                current_header = line[1:]
                fasta_dict[current_header] = ""
            elif current_header:
                fasta_dict[current_header] += line
    return fasta_dict

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        file_path = sys.argv[1]
        seq_header = sys.argv[2]
        fasta_data = parse_fasta(file_path)

        if seq_header in fasta_data:
            dna_seq = fasta_data[seq_header]
            print(f"{seq_header}: {len(dna_seq)} bp")
        else:
            print("Header not found.")
    else:
        print("Usage: python quiz8_prep.py <file_path> <header>")

"""
# Word Frequency from Multiple Files (Functions + Dictionaries + File I/O)

Define a function called `count_words` that accepts a filepath and an
existing dictionary as parameters. The function should read the file and
update the dictionary with word counts (case-insensitive; ignore periods
and commas only). The function should NOT return anything — it modifies
the dictionary in place.

In the main body, accept two input file paths from the command line.
Create an empty dictionary called `word_freq`, then call `count_words`
once for each file. Write every unique word and its total count to a
file called `output.txt` (do not print anything to the screen).

! Constraints:
- You must define and call a function named `count_words`
- You must use a dictionary called `word_freq`
- Do not print anything to the screen; write all results to `output.txt`
- The function modifies the dictionary in place (no return statement needed)

* Expected output file format:
the: 12
dog: 8
cat: 5
"""

def count_words(file_path, word_dict):
    try:
        with open (file_path, "r") as inf:
            for line in inf:
                clean_line = line.lower().replace(".", "").replace(",", "")
                words = clean_line.split()
                for word in words:
                    word_dict[word] = word_dict.get(word, 0) + 1
    except FileNotFoundError:
        pass

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        file1, file2 = sys.argv[1], sys.argv[2]
        word_freq = {}

        count_words(file1, word_freq)
        count_words(file2, word_freq)

        with open("output.txt", "w") as outf:
            for word, count in word_freq.items():
                outf.write(f"{word}: {count}\n")
    else:
        print("Usage: python quiz8_prep.py <file1> <file2>")
