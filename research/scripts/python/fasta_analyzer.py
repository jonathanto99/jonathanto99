#! /usr/bin/env python

import sys
import argparse

# FASTA Sequence Analyzer

def exact_error():
    exact_error_message = (
    "Error: USAGE: python fasta_analyzer.py -i input.fasta -o output.tsv -m gc|composition"
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
    
    for flag in ["-i", "-o", "-m"]:
        arg_count = sum([1 for arg in sys.argv if arg == flag])
        if arg_count > 1:
            print(exact_error(), end="")
            sys.exit(1)
    
    parser.error = custom_error
    parser.add_argument("-i") # input file
    parser.add_argument("-o") # output file
    parser.add_argument("-m") # mode
    args, unknown = parser.parse_known_args()

    if unknown or not args.i or not args.o:
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


def calc_gc(header, sequence):
    header = header.strip()
    sequence = sequence.strip()

    if not sequence_valid(sequence):
        return f"{header}\tERROR\n"
    
    C_count = sequence.count("C")
    G_count = sequence.count("G")
    GC_count = G_count + C_count
    GC_percent = (GC_count / len(sequence)) * 100

    return f"{header}\t{GC_percent}%\n"


def count_composition(header, sequence):
    header = header.strip()
    sequence = sequence.strip()

    if not sequence_valid(sequence):
        return f"{header}\tERROR\n"

    A_count = sequence.count("A")
    C_count = sequence.count("C")
    G_count = sequence.count("G")
    T_count = sequence.count("T")

    A_percent = (A_count / len(sequence)) * 100
    C_percent = (C_count / len(sequence)) * 100
    G_percent = (G_count / len(sequence)) * 100
    T_percent = (T_count / len(sequence)) * 100

    return f"{header}\t{len(sequence)}\t{A_count}({A_percent}%)\t{T_count}({T_percent}%)\t{G_count}({G_percent}%)\t{C_count}({C_percent}%)\n"


def main():
    args = check_args(sys.argv)

    if args.m not in ["gc", "composition"]:
        print(exact_error(), end="")
        sys.exit(1)

    try:
        sequences = parse_fasta(args.i)
    except FileNotFoundError:
        print(exact_error(), end="")
        sys.exit(1)
    
    with open(args.o, "w") as f:
        if args.m == "gc":
            f.write("ID\tGC%\n")
        elif args.m == "composition":
            f.write("ID\tLength\tA(%A)\tT(%T)\tG(%G)\tC(%C)\n")
        
        for header, sequence in sequences.items():
            if args.m == "gc":
                f.write(calc_gc(header, sequence))
            elif args.m == "composition":
                f.write(count_composition(header, sequence))

if __name__ == "__main__":
    main()
