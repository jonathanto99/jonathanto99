"""
# Lab 2: Reverse Complement
* Pseudocode:
1. Open the input FASTA file for reading. (See the 'Input" section for more information about the input FASTA file.)
2. Open the output FASTA file for writing.
3. Read the input FASTA file one record at a time. 
4. Find the complementary bases by iterating through the sequence one character at a time.  
5. Then build a new string with the complementary bases. 
6. Then reversing the order of the new string so that it now reads 5' to 3'.
7. Write the FASTA record with the transformed sequence to the output FASTA file.
8. The headers must appear unmodified and in the same order as the input FASTA file.
9. The transformed sequence is written to the line below the header, and must be in uppercase.

# Lab 2: Transcription
* Pseudocode:
1. Open the input FASTA file for reading. (See the 'Input" section for more information about the input FASTA file.)
2. Open the output FASTA file for writing.
3. Read the input FASTA file one record at a time. 
4. You must use the re module for your regular expression. 
5. In the dna sequences, look for and replace each thymine with uracil using regular expression.
6. Remember that the syntax for regular expression in this case is rna = re.sub(search, replace, dna)
7. Write the FASTA record with the transformed sequence to the output FASTA file.
8. The headers must appear unmodified and in the same order as the input FASTA file.
9. The transformed sequence is written to the line below the header, and must be in uppercase.
"""

# * Program:
#! /usr/bin/env python

import sys
import re

def rev_comp(input_file, output_file):
    # Reverse complement logic
    trans_table = str.maketrans("ACGTacgt", "TGCAtgca")
    with open(input_file, "r") as inf, open(output_file, "w") as outf:
        for line in inf:
            line = line.strip()
            if line.startswith(">"):
                outf.write(f"{line}\n")
            else:
                outf.write(f"{line.translate(trans_table)[::-1]}\n")


def transcription(input_file, output_file):
    # Transcription logic
    with open(input_file, "r") as inf, open(output_file, "w") as outf:
        for line in inf:
            line = line.strip()
            if line.startswith(">"):
                outf.write(f"{line}\n")
            else:
                rna_seq = re.sub(r"[Tt]", r"U", line)
                outf.write(f"{rna_seq.upper()}\n")


def main():
    # Check sys.argv length
    if len(sys.argv) < 3:
        print("Usage: Usage: python script.py <input.fasta> <output.fasta>")
        sys.exit(1)

    input_file = sys.argv[1]
    out_rev = "revcomp_" + sys.argv[2]
    out_trans = "transcribed_" + sys.argv[2]

    rev_comp(input_file, out_rev)
    transcription(input_file, out_trans)
    print("Processing complete.")

if __name__ == "__main__":
    main()
