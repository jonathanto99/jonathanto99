#! /usr/bin/env python

"""
# Lab 5: DNA Toolbox
* Pseudocode:
List of Options
Description of command-line options and their dependencies Options Parameter after the Option Expected Functionality Other Options Required to be Included
-g 	N/A 	Calculate GC percent 	-i, -o
-r 	N/A 	Reverse complement 	-i, -o
-s 	N/A 	Transcription 	-i, -o
-l (lowercase L) 	N/A 	Translation 	-i, -o, -c
-n 	N/A 	Count Nucleotides 	-i, -o
-i 	Path to the input file 	Store path to input file 	N/A
-o 	Path to the output file 	Store path to output file 	N/A
-c 	Path to the codons file 	Store path to codons file 	N/A
Check if the command line options are valid.

If the options are invalid, the following exact error message must be printed to the screen:
Error: USAGE: python myprogram.py: option -i input.fasta -o output.txt
Available options:
-g GC percent   
-r reverse complement
-s transcription
-l translation
-n count nucleotides
For clarity, that error message contains the following characters (where a space is indicated, it is exactly one space):
Error: USAGE: python myprogram.py: option -i input.fasta -o output.txt\n
Available options:\n
-g GC percent\n
-r reverse complement\n
-s transcription\n
-l translation\n
-n count nucleotides\n
Note: The error message is exactly the same regardless of what the user inputs. If an error is found in the system arguments, that error message should be printed to the screen and your program should exit immediately.

Call the correct function associated with the user-specified option.

GC percent: 
See Lab 1 for more specific details on calculating GC percent.
Your output file contains two tab-separated columns: sequence ID and unrounded GC percent.
Your output file starts with a header line (ID   GC%) or with all characters explicitly listed (ID\tGC%\n).
You must call a function named calcGC that takes two arguments of type string (the header and the valid sequence) and returns a string (the formatted tab-separated value record). Your function definition line might look like this: def calcGC(header, valid_sequence):

Reverse complement: 
See Lab 2 for more specific details.
You must call a function named revComp that takes two arguments of type string (the header and the valid sequence) and returns a string (the formatted fasta record). Your function definition might look like this:
def revComp(header, valid_sequence):

Transcription:
See Lab 2 for more specific details.
You must use a regular expression to convert the T's to U's.
Do not use the string.replace() function (or create a function with that name) anywhere in your program (even in other functions).
You must call a function named transcribe that takes two arguments of type string (the header and the valid sequence) and returns a string (the formatted fasta record). Your function definition might look like this:
def transcribe(header, valid_sequence):

Translation: 
See Lab 3 for more specific details.
You must call a function named translate that takes three arguments. Two of type string (the header and the valid sequence) and one of type dictionary (codons_dictionary). It should return a string (the formatted fasta record). Your function definition might look like this:
def translate(header, valid_sequence, codons_dictionary):

Count nucleotides:
See Lab 4 for more specific details.
You must call a function named countNucs that takes two arguments of type string (the header and the valid sequence) and returns a string (the formatted tab-separated value record). Your function definition might look like this:
def countNucs(header, valid_sequence):
"""

# * Program:
import sys
import re
import argparse

def exactErrorMessage():
    exact_error_message = (
    "Error: USAGE: python myprogram.py: option -i input.fasta -o output.txt\n"
    "Available options:\n"
    "-g GC percent\n"
    "-r reverse complement\n"
    "-s transcription\n"
    "-l translation\n"
    "-n count nucleotides\n" 
    )
    
    return exact_error_message


def toCaps(sequence): # Replaces the case conversion functions
    result = ""
    
    for char in sequence:
        if "a" <= char <= "z":
            result += chr(ord(char) - 32)
        else:
            result += char
    
    return result


def charsReplace(sequence, target, replacement): # Replaces the replace function
    result = ""
    
    for char in sequence:
        if char == target:
            result += replacement
        else: 
            result += char
    
    return result


def getSize(sequence): # Replaces len function
    size = 0
    
    for char in sequence:
        size += 1
    
    return size


def getTally(sequence, target): # Replaces count function
    tally = 0
    target_up = toCaps(target)
    
    for char in sequence:
        if toCaps(char) == target_up:
            tally += 1
    
    return tally


def codonDictionary(codon_file_name): # Turns the codon file into a dictionary
    codon_dict = {}
    
    with open(codon_file_name, "r") as inf:
        for raw in inf:
            line = raw.strip().split("\t")
            codon_dict[line[0]] = line[1]
    
    return codon_dict


def cleanHeader(header):
    clean_header = header.strip()
    
    if getSize(clean_header) > 0 and clean_header[0] == ">":
        clean_header = clean_header[1:]
        return clean_header
    else:
        return clean_header


def cleanWhitespace(sequence):
    clean_sequence = charsReplace(sequence, " ", "")
    clean_sequence = charsReplace(clean_sequence, "\t", "")
    clean_sequence = charsReplace(clean_sequence, "\n", "")
    clean_sequence = charsReplace(clean_sequence, "\r", "")
    
    return clean_sequence


def sequenceValid(sequence): # Checks if the sequence is valid
    clean_sequence = cleanWhitespace(sequence)
    
    if getSize(clean_sequence) == 0:
        return False
    
    for char in clean_sequence:
        if toCaps(char) not in "ATGC":
            return False
    
    return True


def checkArgs(args): # Checks if the system arguments are valid
    exact_error_message = exactErrorMessage()
    parser = argparse.ArgumentParser(add_help=False)

    def customError():
        print(exact_error_message, end="")
        sys.exit(1)
    
    for flag in ["-g", "-r", "-s", "-l", "-n", "-i", "-o", "-c"]:
        tally = sum([1 for arg in sys.argv if arg == flag])
        if tally > 1:
            print(exact_error_message, end="")
            sys.exit(1)

    parser.error = customError
    parser.add_argument("-i") # path to input file
    parser.add_argument("-o") # path to output file
    parser.add_argument("-c") # path to codon file
    parser.add_argument("-g", action="store_true") # calculate GC content function
    parser.add_argument("-r", action="store_true") # reverse complement function
    parser.add_argument("-s", action="store_true") # transcription function
    parser.add_argument("-l", action="store_true") # translation function
    parser.add_argument("-n", action="store_true") # count nucleotides function
    args, unknown = parser.parse_known_args()

    if unknown or not args.i or not args.o:
        print(exact_error_message, end="")
        sys.exit(1)
    
    operations_passed = sum([args.g, args.r, args.s, args.l, args.n])
    if operations_passed != 1:
        print(exact_error_message, end="")
        sys.exit(1)
    
    if args.l and not args.c:
        print(exact_error_message, end="")
        sys.exit(1)
    
    return args


def calcGC(header, valid_sequence): # GC content calculation function
    clean_header = cleanHeader(header)
    clean_sequence = cleanWhitespace(valid_sequence)
    
    if not sequenceValid(valid_sequence):
        return f"{clean_header}\tERROR\n"
    
    total_size = getSize(clean_sequence)
    if total_size == 0:
        return f"{clean_header}\tERROR\n"
    
    g_tally = getTally(clean_sequence, "G")
    c_tally = getTally(clean_sequence, "C")
    gc_tally = g_tally + c_tally
    percentage = (gc_tally / total_size) * 100
    
    return f"{clean_header}\t{percentage}%\n"


def revComp(header, valid_sequence): # Reverse complement function
    clean_header = cleanHeader(header)

    if not sequenceValid(valid_sequence):
        return f">{clean_header}\nERROR\n"
    
    else:
        clean_sequence = cleanWhitespace(valid_sequence)
        clean_sequence = toCaps(clean_sequence)
        sequence_complement = []
        for nuc in clean_sequence:
            if nuc == "A":
                nuc = "T"
                sequence_complement.append(nuc)
            elif nuc == "T":
                nuc = "A"
                sequence_complement.append(nuc)
            elif nuc == "G":
                nuc = "C"
                sequence_complement.append(nuc)
            elif nuc == "C":
                nuc = "G"
                sequence_complement.append(nuc)
        
        reverse_complement = sequence_complement[::-1]
        reverse_complement = "".join(reverse_complement)
        
        return f">{clean_header}\n{reverse_complement}\n"


def transcribe(header, valid_sequence): # Transcription function
    clean_header = cleanHeader(header)
    
    if not sequenceValid(valid_sequence):
        return f">{clean_header}\nERROR\n"
    
    else:
        clean_sequence = cleanWhitespace(valid_sequence)
        clean_sequence = toCaps(clean_sequence)
        rna_sequence = re.sub(r"[Tt]", r"U", clean_sequence)
        
        return f">{clean_header}\n{rna_sequence}\n"


def translate(header, valid_sequence, codons_dictionary): # Translation function
    clean_header = cleanHeader(header)
    
    if not sequenceValid(valid_sequence):
        return f">{clean_header}\nERROR\n"
    
    else:
        protein = ""
        rna_sequence = transcribe(header, valid_sequence)
        rna_sequence = rna_sequence.split("\n")[1]
        rna_sequence = toCaps(rna_sequence)
        
        for i in range(0, getSize(rna_sequence), 3):
            codon = rna_sequence[i:i+3]
            if getSize(codon) == 3:
                amino_acid = codons_dictionary.get(codon, "ERROR")
                if amino_acid == "*":
                    break
                protein += amino_acid
            elif getSize(codon) < 3:
                break
        
        return f">{clean_header}\n{protein}\n"


def countNucs(header, valid_sequence): # Nucleotide percentage calculation function
    clean_header = cleanHeader(header)
    clean_sequence = cleanWhitespace(valid_sequence)
    
    if not sequenceValid(valid_sequence):
        return f"{clean_header}\tERROR\n"
    
    total_size = getSize(clean_sequence)
    if total_size == 0:
        return f"{clean_header}\tERROR\n"
    
    a_tally = getTally(clean_sequence, "A")
    a_percentage = (a_tally / total_size) * 100
    c_tally = getTally(clean_sequence, "C")
    c_percentage = (c_tally / total_size) * 100
    g_tally = getTally(clean_sequence, "G")
    g_percentage = (g_tally / total_size) * 100
    t_tally = getTally(clean_sequence, "T")
    t_percentage = (t_tally / total_size) * 100
    
    return f"{clean_header}\t{total_size}\t{a_tally}({a_percentage}%)\t{c_tally}({c_percentage}%)\t{g_tally}({g_percentage}%)\t{t_tally}({t_percentage}%)\n"


def processSequence(args, header, raw_sequence, codons): # Sequence processor
    result = ""
    
    if header != "":
        if args.g:
            result += calcGC(header, raw_sequence)
        elif args.r:
            result += revComp(header, raw_sequence)
        elif args.s:
            result += transcribe(header, raw_sequence)
        elif args.l:
            result += translate(header, raw_sequence, codons)
        elif args.n:
            result += countNucs(header, raw_sequence)
    
    return result


def main():
    args = checkArgs(sys.argv)
    codons = {}
    
    if args.l:
        codons = codonDictionary(args.c)
    result = ""
    
    if args.g:
        result += "ID\tGC%\n"
    elif args.n:
        result += "ID\tLength\tA(%A)\tC(%C)\tG(%G)\tT(%T)\n"
    
    try:
        with open(args.i, "r") as inf:
            header = ""
            raw_sequence = ""     
            
            for line in inf:
                if not line.strip():
                    continue
                if line.startswith(">") and (header == "" or raw_sequence.strip() != ""):
                    result += processSequence(args, header, raw_sequence, codons)             
                    header = line.strip()
                    raw_sequence = ""
                else:
                    raw_sequence += line
            if header != "":
                result += processSequence(args, header, raw_sequence, codons)

        with open(args.o, "w") as outf:
            outf.write(result)
    
    except FileNotFoundError:
        exact_error_message = exactErrorMessage()
        print(exact_error_message, end="")
        sys.exit(1)


if __name__ == "__main__":
    main()
