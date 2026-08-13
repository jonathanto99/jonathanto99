"""
# Lab 1: User Inputs and Conditional Statements
* Pseudocode
1. Validate user inputs and make sure that there are no empty strings and/or invalid characters. 
Output errors if for either of these conditions is met. Separate error message for each condition. 
2. Calculate and output the length of each sequence. There will be 3 sequences. Only count A, G, C, and T (and lowercase). 
White spaces (spaces, tabs) are considered valid characters, they are just not calculated as a part of the sequence length. 
3. Concatenate the three processed sequences and display them in one string all in uppercase. 
Check for white spaces. Remove them if found. 
4. Calculate the percentage of GC content in the concatenated sequence and display the percentage. 
There is no need for rounding. Just print out whatever Python gets from the calculation. 
"""

# * Program:
#! /usr/bin/env python

import sys

valid_chars = "AGCTagct \t"

def is_sequence_valid(seq):
    # Check if sequence is empty or contains only whitespace 
    # Also check each character in the sequence for invalid characters
    if seq.strip() == "":
        print("ERROR: You must enter a DNA sequence")
        return False
    for nuc in seq:
        if nuc not in valid_chars:
            print("ERROR: Invalid DNA sequence")
            return False
    return True


def get_args():
    # If the script is run without 3 args (e.g. from the editor), use these defaults for quick testing.
    # When you run from terminal with three args, those will be used instead.
    if len(sys.argv) < 4:
        # change these defaults to test other cases quickly
        return ["ACGT", "gg cc", " t t a a "]
    return sys.argv[1:4]


def gc_calc(seq):
    # Calculate the GC percentage of a sequence.
    if not seq:
        return 0.0 
    gc_count = 0
    for nuc in seq:
        if nuc in ["G", "C"]:
            gc_count += 1
    return gc_count / len(seq) * 100


def main():
    seqs = get_args()
    full_seq = ""
    
    for i, seq in enumerate(seqs):
        if not is_sequence_valid(seq):
            sys.exit(1)
        # Find and output the length of each string, only counting nucleotides
        # Concatenate the three sequences and print them in one string
        seq = seq.replace("\\t", "\t").replace("\\n", "\n")
        clean_seq = seq.replace(" ", "").replace("\t", "")
        full_seq += clean_seq.upper()
        print(f"Sequence {i + 1}: {len(clean_seq)}")
    print(f"\nConcatenated Sequence: {full_seq}")
    print(f"GC Content: {gc_calc(full_seq)}%")

if __name__ == "__main__":
    main()
