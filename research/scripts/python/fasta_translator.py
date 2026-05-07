#! /usr/bin/env python

import sys
import re
import argparse

# FASTA Translator - Final Exam: Extra Credit Problem (see .md file for more instructions)

def exact_error():
    exact_error_message = (
    "Error: USAGE: python fasta_translator.py -i input.fasta -o output.tsv -c codons.tsv"
    )
    return exact_error_message


def sequence_valid(sequence):
    sequence = sequence.strip()

    if len(sequence) == 0:
        return False

    for nuc in sequence:
        if nuc.upper() not in "ATGC":
            return False

    return True


def check_args(args):
    parser = argparse.ArgumentParser()

    def custom_error():
        print(exact_error(), end="")
        sys.exit(1)
    
    for flag in ["-i", "-o", "-c"]:
        arg_count = sum([1 for arg in sys.argv if arg == flag])
        if arg_count > 1:
            print(exact_error(), end="")
            sys.exit(1)
    
    parser.error = custom_error
    parser.add_argument("-i") # input file
    parser.add_argument("-o") # output file
    parser.add_argument("-c") # mode
    args, unknown = parser.parse_known_args()

    if unknown or not args.i or not args.o or not args.c:
        print(exact_error(), end="")
        sys.exit(1)
    
    return args


def parse_fasta(filepath):
    sequences = {}
    current_id = None
    current_seq = []

    with open(filepath, "r") as f:
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                if current_id:
                    sequences[current_id] = "".join(current_seq)
                
                current_id = line[1:]
                current_seq = []
            else:
                current_seq.append(line)
        
        if current_id:
            sequences[current_id] = "".join(current_seq)
    
    return sequences


def load_codons(codon_filepath):
    codon_dict = {}

    with open(codon_filepath, "r") as f:
        for line in f:
            line = line.strip().split("\t")
            codon_dict[line[0]] = line[1]
    
    return codon_dict


def translate(header, sequence, codon_dict):
    header = header.strip()
    sequence = sequence.strip()
    protein = ""

    if not sequence_valid(sequence):
        return f">{header}\nERROR\n"

    rna_sequence = re.sub(r"T", r"U", sequence)

    for i in range(0, len(rna_sequence), 3):
        codon = rna_sequence[i:i+3]
        if len(codon) == 3:
            amino_acid = codon_dict.get(codon)
            if amino_acid == "*":
                break
            protein += amino_acid
        elif len(codon) < 3:
            break
    
    return f">{header}\n{protein}\n"


def main():
    args = check_args(sys.argv)

    try:
        sequences = parse_fasta(args.i)
    except FileNotFoundError:
        print(exact_error(), end="")
        sys.exit(1)

    codon_dict = load_codons(args.c)

    with open(args.o, "w") as f:
        for header, sequence in sequences.items():
            f.write(translate(header, sequence, codon_dict))

if __name__ == "__main__":
    main()
