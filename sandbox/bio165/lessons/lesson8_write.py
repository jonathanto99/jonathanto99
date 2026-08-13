import sys

# * Write Practice Problem 1
# Write a program that accepts two arguments from the command line. 
# The first is a file for reading and the second is the file where you will write your output. 
# Each line in the input file will have two numbers, separated by a tab (\t). 
# Your program should read each line from the input file and print the two numbers and their sum to the output file. 

file1 = sys.argv[1]
file2 = sys.argv[2]

with open(file1, "r") as infile, open(file2, "w") as outfile:
    for line in infile:
        nums = line.strip().split("\t")
        num1 = int(nums[0])
        num2 = int(nums[1])
        total = num1 + num2
        outfile.write(f"{num1}\t{num2}\t{total}\n")

# * Write Practice Problem 2
# Write a program that accepts an input and an output file from the command line. 
# You will read the input file, a fasta file, and the output file will be a new, corrected fasta file. 
# In the input fasta file, sequence lines may contain spaces. 
# Your program should create a fasta file with all the sequences from the input file and identical title lines, 
# but with all spaces removed from the sequence lines. 
# The records in the output file must appear in the same order as the input file,
# and the case of all characters in the output file should be the same as in the input file. 

file_in = sys.argv[1]
file_out = sys.argv[2]

with open(file_in, "r") as infile, open(file_out, "w") as outfile:
    for line in infile:
        if line.startswith(">"):
            header = line.strip()
            outfile.write(f"{header}\n")
        else:
            clean_line = line.strip().replace(" ", "")
            outfile.write(f"{clean_line}\n")
