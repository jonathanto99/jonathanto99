"""
# Lab 3: Translation
* Pseudocode:
1. Process and store the codon information:
    Open the codon file for reading.
    Recommendation only: Store the data in a dictionary with the codons as keys and the amino acids as values. 
    (While this is only a recommendation, you can be confident you will have to be able to use dictionaries on the exams.)
    Close the codon file.
2. Open the input and output FASTA files:
    Open the input FASTA file for reading.
    Open the output FASTA file for writing.
3. Read the input FASTA file one record at a time:
    You may read the input FASTA file any way you want, 
    but you will need to be able to differentiate between header and sequence lines.
4. Check the sequence for errors:
    Error checking is exactly the same as Lab 1.
    Spaces and uppercase/lowercase nucleotides are not errors:
    Whitespace (spaces and tabs) should be removed.
    If invalid characters (not A, C, G, T, space, or tab) appear anywhere in the DNA sequence (even after the stop codon), 
    then the header line should still be written to the output file, but the protein sequence should be ERROR.
    If there is an error, do not attempt to translate the sequence. Just go to the next record in the input FASTA file.
5. Transcribe the DNA sequence to RNA (Lab 2).
6. Translate the RNA sequence to protein:
    Iterate through the RNA sequence three characters at a time to extract a codon.
    You are guaranteed that the first codon in a properly formatted (non-error) RNA sequence will be the start codon AUG.
6.1. This is a recommendation only (and the most intuitive and easiest approach): 
    Use the dictionary to find the amino acid associated with each codon.
    Concatenate the amino acid translated from the codon to the protein sequence.
    When you find a stop codon (UAA, UAG, UGA) stop translating and continue to the next step. 
    Do not include an asterisk (“*”) in the protein sequence.
7. Write the header and translated protein sequence to the output file:
    The headers must be in the same order as the input file
    and the case in the output file should match the case in the input file.
    The protein sequence or error message must be written on a new line immediately following the header, in all uppercase.
8. Repeat Steps 3 through 7 for all sequences in the input file.
9. Close the input and output FASTA files:
    This step is completed automatically if you used with to open the files.

"""

# * Program:
#! /usr/bin/env python

import sys

input_file_name = sys.argv[1]
codon_file_name = sys.argv[2]
output_file_name = sys.argv[3]


def codonDictionary(codon_file_name):
    codon_dict = {}
    with open(codon_file_name, "r") as inf:
        for raw in inf:
            line = raw.strip().split("\t")
            codon_dict[line[0]] = line[1]
    return codon_dict


def isValidSequence(seq):
    valid_chars = set("ATGCatgc \t")
    return all(char in valid_chars for char in seq)


def errorChecker(seq):
    if not seq.strip():
        return False
    if not isValidSequence(seq):
        return False
    return True


def transcribe(seq):
    if not errorChecker(seq):
        return "ERROR"
    clean_seq = seq.replace(" ", "").replace("\t", "")
    rna_seq = clean_seq.replace("t", "u").replace("T", "U").upper()
    return rna_seq


def translate(rna_seq, codon_dict):
    protein = ""
    for i in range(0, len(rna_seq), 3):
        codon = rna_seq[i:i+3]
        if len(codon) == 3:
            amino_acid = codon_dict[codon]
            if amino_acid == "*":
                break
            protein += amino_acid
        elif len(codon) < 3:
            break
    return protein


def main(input_file_name, codon_file_name, output_file_name):
    codon_dict = codonDictionary(codon_file_name)
    with open(input_file_name, "r") as inf, open(output_file_name, "w") as outf:
        expect_sequence = False
        for raw in inf:
            line = raw.strip()
            if line.startswith(">") and not expect_sequence:
                header = line
                expect_sequence = True
            else:
                if not errorChecker(line):
                    outf.write(header + "\n")
                    outf.write("ERROR\n")
                else:
                    rna_seq = transcribe(line)
                    protein = translate(rna_seq, codon_dict)
                    outf.write(f"{header}\n")
                    outf.write(f"{protein}\n")
                expect_sequence = False

if __name__ == "__main__":
    main(input_file_name, codon_file_name, output_file_name)
