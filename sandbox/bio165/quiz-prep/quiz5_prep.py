import sys
import re

# Problem 1 — File Reading
# Write a program that accepts a file path from the command line.
# The file contains one word per line. Print the total number of words,
# the number of unique words, and the number of words that start with
# a vowel (a, e, i, o, u — case insensitive).

file1 = sys.argv[1]
total_count = 0
vowel_count = 0
vowels = "aeiouAEIOU"
seen_words = set()

with open(file1, "r") as infile:
    for word in infile:
        word = word.strip()
        total_count += 1
        seen_words.add(word)
        if word.startswith(vowels):
            vowel_count += 1
unique_count = len(seen_words)

print(f"""
Total word count is: {total_count}!
Unique word count is: {unique_count}!
Vowel word count is: {vowel_count}!
""")

# Problem 2 — File Writing
# Write a program that accepts an input and output file from the command line.
# Each line in the input file contains a DNA sequence (only A, T, C, G characters).
# Write to the output file only the sequences that are longer than 10 characters,
# with the sequence reversed and in lowercase.

file1 = sys.argv[1]
file2 = sys.argv[2]

with open(file1, "r") as inf, open(file2, "w") as outf:
    for line in inf:
        line = line.strip()
        if len(line) > 10:
            line = line[::-1].lower()
            outf.write(f"{line}\n")

# Problem 3 — FASTA
# Write a program that accepts an input FASTA file and an output file from
# the command line. Write only the records where the sequence contains no
# ambiguous bases (i.e., only A, T, C, G — no N or other characters,
# case insensitive) to the output file. Title lines and sequence structure
# should be preserved exactly.

infile = sys.argv[1]
outfile = sys.argv[2]
valid_bases = set("atcgATCG")

with open(infile, "r") as inf, open(outfile, "w") as outf:
    current_header = None
    current_seq = ""

    for line in inf:
        line = line.strip()
        if line.startswith(">"):
            if current_header and all(base in valid_bases for base in current_seq):
                outf.write(f"{current_header}\n{current_seq}\n")
            current_header = line
            current_seq = ""
        else:
            current_seq += line
    if current_header and all(base in valid_bases for base in current_seq):
        outf.write(f"{current_header}\n{current_seq}\n")

# Problem 4 — VCF
# Write a program that accepts a VCF file from the command line. Print to
# the screen the total number of variant lines, and the number of variant
# lines where the quality score (column 6) is greater than 30.
# Do not use regular expressions.

vcf_file = sys.argv[1]
variant_count = 0
good_quality = 0

with open(vcf_file, "r") as inf:
    for line in inf:
        line = line.strip()
        if line.startswith("#"):
            continue
        columns = line.split("\t")
        if len(columns) > 5:
            variant_count += 1
            if int(columns[5]) > 30:
                good_quality += 1

print(f"The number of variant line is: {variant_count}. The number of good quality reads is: {good_quality}.")

# Problem 5 — VCF Writing with re.sub
# Write a program that accepts an input and output VCF file from the command line.
# Copy all metadata and header lines to the output file unchanged. For variant lines,
# use re.sub to replace any chromosome number in column 1 that starts with `chr`
# (e.g. `chr1`, `chr12`) with just the number (e.g. `1`, `12`). Write all variant
# lines (modified or not) to the output file.

infile = sys.argv[1]
outfile = sys.argv[2]
regex = r"^chr"
replace = r""

with open(infile, "r") as inf, open(outfile, "w") as outf:
    for line in inf:
        line = line.strip()
        if line.startswith("#"):
            outf.write(f"{line}\n")
            continue
        columns = line.split("\t")
        columns[0] = re.sub(regex, replace, columns[0])
        outf.write(f"{"\t".join(columns)}\n")

