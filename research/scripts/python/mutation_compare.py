#! /usr/bin/env python

import sys
import argparse

# Mutation Comparison Tool 

def exact_error():
    exact_error_message = (
    "Error: USAGE: python mutation_compare.py -i1 reference.fasta -i2 sample.fasta -o output.tsv"
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
    
    for flag in ["-i1", "-i2", "-o"]:
        arg_count = sum([1 for arg in sys.argv if arg == flag])
        if arg_count > 1:
            print(exact_error(), end="")
            sys.exit(1)
    
    parser.error = custom_error
    parser.add_argument("-i1") # input file
    parser.add_argument("-i2") # output file
    parser.add_argument("-o") # mode
    args, unknown = parser.parse_known_args()

    if unknown or not args.i1 or not args.i2 or not args.o:
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


def count_mutations(seq1, seq2):
    snp_count = 0
    for nuc1, nuc2 in zip(seq1, seq2):
        if nuc1 != nuc2:
            snp_count += 1
    return snp_count


def get_mutation_positions(seq1, seq2):
    snp_positions = []
    for i, (nuc1, nuc2) in enumerate(zip(seq1, seq2)):
        if nuc1 != nuc2:
            snp_position = i
            snp_positions.append(snp_position + 1)
    return snp_positions
        

def main():
    args = check_args(sys.argv)
    mutation_report = {}

    try:
        ref_sequences = parse_fasta(args.i1)
        sample_sequences = parse_fasta(args.i2)
    except FileNotFoundError:
        print(exact_error(), end="")
        sys.exit(1)

    for header, ref_seq in ref_sequences.items():
        if header in sample_sequences:
            sample_seq = sample_sequences[header]
            snp_count = count_mutations(ref_seq, sample_seq)
            snp_positions = get_mutation_positions(ref_seq, sample_seq)
            mutation_report[header] = (ref_seq, sample_seq, snp_count, snp_positions)

    with open(args.o, "w") as f:
        f.write("ID\tReference\tSample\tMutations\tPositions\n")
        
        for header, (ref_seq, sample_seq, snp_count, snp_positions) in mutation_report.items():
            if len(snp_positions) == 0: 
                positions_str = "none"
            else: 
                positions_str = ",".join(str(p) for p in snp_positions)
        
        f.write(f"{header}\t{ref_seq}\t{sample_seq}\t{snp_count}\t{positions_str}\n")

if __name__ == "__main__":
    main()
