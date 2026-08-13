import sys
import re

"""
* Change "PASS" to "pass" in a new VCF file
For this question, you will be reading a VCF file and writing to a new VCF file. 
For a thorough explanation of VCF files, see Homework 6: Reading. 
We are looking for lines that have “PASS” in the 7th column. Remember that meta-data and header lines start with "#". 
All of the meta-data and header lines from the input file should be printed to the new file. 
After finding all the meta-data and header lines come the variant lines. 
Find all the variant lines that have the word "PASS" in the 7th column. 
Replace “PASS” with “pass”, using a regular expression, and then print those lines to the new file. 
The first command line argument will be the VCF file you are reading from, 
and the second command line argument will be the new file you are creating. 
You must use re.sub to change PASS to pass. 
The lines in the output file should appear in the same order they appear in the original file 
(minus the lines that shouldn't be included in the new file). 
"""

file1 = sys.argv[1]
file2 = sys.argv[2]

with open(file1, "r") as inf, open(file2, "w") as outf:
    for line in inf:
        line = line.strip()
        if line.startswith("#"):
            outf.write(f"{line}\n")
        else:
            columns = line.split("\t")
            if len(columns) > 6 and columns[6] == "PASS":
                columns[6] = re.sub("PASS", "pass", columns[6])
                outf.write(f"{"\t".join(columns)}\n")

"""
* Concatenate DNA sequences in new FASTA file
Recall that fasta files have a title line that starts with ">" followed by one or more sequence lines.
Write a program that opens input.fasta (given as sys.argv[1]) and creates a new file for output (given as sys.argv[2]). 
The output file should have the exact same title lines as input.fasta, 
but any sequences that appear on more than one line should be concatenated together and printed on one line, in uppercase.
So in your output, each sequence will have only one title line and only one uppercase sequence line.
Fasta records in the output file should appear in the same order as the input file.

For example, if you have the following input file:

>Animal1
Atat
ggggg
>AnimAl2
TtGT
cCcC

Your output should be:

>Animal1
ATATGGGGG
>AnimAl2
TTGTCCCC
"""

file_in = sys.argv[1]           # 1: input FASTA filename from command line
file_out = sys.argv[2]          # 2: output filename from command line

with open(file_in, "r") as inf, open(file_out, "w") as outf:  # 3: open input for read and output for write
    header = ""                 # 4: holds the current record's title line (e.g. ">seq1")
    sequence = ""               # 5: accumulates the current record's sequence (all lines concatenated)

    for line in inf:            # 6: iterate over every line in the input file
        line = line.strip()     # 7: remove leading/trailing whitespace and newline
        if line.startswith(">"):          # 8: this is a title/header line
            if header != "":              # 9: if we were already processing a record, flush it first
                outf.write(f"{header}\n{sequence}\n")  # 10: write previous record to output (title then concatenated seq)
            line = header                 # 11: start a new record: save this title line (keeps the '>' char)
            sequence = ""                 # 12: reset sequence accumulator for the new record
        else:                             # 13: this line is part of a sequence for the current header
            sequence += line.upper()      # 14: append the line (uppercased) to the sequence accumulator
    if header != "":                      # 15: after loop ends, if a record was in progress, write it out
        outf.write(f"{header}\n{sequence}\n")  # 16: write the final record
