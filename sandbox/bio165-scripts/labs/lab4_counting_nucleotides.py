"""
# Lab 4: Counting Nucleotides
* Pseudocode:
1. Check system arguments.
    There should be three total system arguments: the name of your program and two additional arguments. 
    If there are more or fewer than three system arguments then you must print the following error message, 
    exactly as it appears (with uppercase and lowercase letters, punctuation, and spaces as indicated 
    or CodeBuddy will not recognize your output as correct, even if you correctly identified that 
    the number of arguments provided was incorrect) to the screen and exit using sys.exit():
    ERROR: Incorrect number of arguments.
2. Open the files.
    Open the input FASTA file for reading.
    Open the output tab-separated values (tsv) file for writing.
    Write a title line to the output file:
    ID\tLength\tA(%A)\tC(%C)\tG(%G)\tT(%T)\n
3. Read the input FASTA file one record at a time.
    You can read the FASTA file any way that you want:
    The first line will always be a header line.
    A single sequence line will always follow the header line.
    The FASTA file will always end with a sequence line.
4. Check the sequence for errors.
    Sequence error checking is exactly the same as the previous labs.
    We recommend (although do not require) that you use a function for error checking. 
    Using a function will make your tasks easier in this lab and Lab 5.
    Spaces and uppercase/lowercase nucleotides (A, C, G, and T) are not errors
    Spaces between nucleotides should be removed.
    If non-nucleotide characters appear anywhere in the DNA sequence (including the first character of the sequence), 
    then the header ID will be written to the file, followed by a tab (“\t”), followed by ERROR.
5. Calculate summary statistics
    - Calculate the length of the sequence.
    You may not use the len function anywhere in your program, 
    and you may not name any variables len or you will fail pass-off.
    You must create a function called (exactly) getLength with the same functionality as len. 
    Your function definition should look exactly like this: 
    def getLength(some_string_or_list): 
    and it must return an integer that is the length of the string or the number of elements in the list. 
    As demonstrated in class, we recommend including the function near the top of your program, 
    just under your import statement(s). Your function may not have any global variables, or you will fail pass-off.
    You will need this function to complete Lab 5. Efforts to write a robust function now will save you time on Lab 5.
    - Count the number of each nucleotide.
    You may not use the string.count() function, and you may not name any variables count or you will fail pass-off.
    You must create a function called (exactly) getCount with the same functionality as string.count(). 
    Your function definition should look exactly like this:
    def getCount (str_to_look_in, char_to_count): 
    and it must return an integer. 
    As demonstrated in class, we recommend including the function near the top of your program, 
    just under your import statement(s). Your function may not have any global variables, or you will fail pass-off.
    You will need this function to complete Lab 5. Efforts now to write a robust function will save you time on Lab 5.
    - Calculate the percent composition of each nucleotide.
    Remember, percent is (count / length) * 100. Percentages should be floats. 
    Do not round off the percentages or you may fail pass-off.
    If you fail to follow the instructions regarding naming your functions, 
    and which terms not to use, you will fail the pass-off.
6. Write the header ID and summary statistics to the output file.
    The header ID is the header line without the first >, 
    which is the first character of each header line in the input FASTA files.
    The header ID and summary statistics should be written to the file on a single line after the column headers.
    You must maintain the same order of header IDs in your output file as the input file.
7. Repeat Steps 3 through 6 for all sequences in the input file.
8. Close both files.
"""

# * Program:
#! /usr/bin/env python

import sys

def getCount(str_to_look_in, char_to_count_in_str):
    count = 0
    for char in str_to_look_in:
        if char == char_to_count_in_str:
            count += 1
    return count


def getLength(some_string_or_list):
    length = 0
    for char in some_string_or_list:
        length += 1
    return length


def isValidSequence(seq):
    valid_chars = set("ATGCatgc \t")
    return all(char in valid_chars for char in seq)


def errorChecker(seq):
    if not seq.strip():
        return False
    if not isValidSequence(seq):
        return False
    return True

if getLength(sys.argv) != 3:
    print("ERROR: Incorrect number of arguments")
    sys.exit()

input_file = sys.argv[1]
output_file = sys.argv[2]


def main(input_file, output_file):
    with open(input_file, "r") as inf, open(output_file, "w") as outf:
        outf.write("ID\tLength\tA(%A)\tC(%C)\tG(%G)\tT(%T)\n")   
        header = ""
        expecting_header = True

        for line in inf:
            field = line.strip()
            if expecting_header:
                header = field[1:]
                expecting_header = False
            else:
                expecting_header = True
                if errorChecker(field) is False:
                    outf.write(f"{header}\tERROR\n")
                else:
                    seq_clean = field.upper().replace(" ", "").replace("\t", "")
                    seq_size = getLength(seq_clean)     
                    A_num = getCount(seq_clean, "A")
                    A_perc = (A_num / seq_size) * 100
                    C_num = getCount(seq_clean, "C")
                    C_perc = (C_num / seq_size) * 100
                    G_num = getCount(seq_clean, "G")
                    G_perc = (G_num / seq_size) * 100
                    T_num = getCount(seq_clean, "T")
                    T_perc = (T_num / seq_size) * 100     
                    outf.write(f"{header}\t{seq_size}\t{A_num}({A_perc}%)\t{C_num}({C_perc}%)\t{G_num}({G_perc}%)\t{T_num}({T_perc}%)\n")

if __name__ == "__main__":
    main(input_file, output_file)
