#! /usr/bin/env python3

import sys

# Bioinformatics is so fun!
print("Bioinformatics")
print("is")
print("fun!")

# What car is this?
car = "subaru"
print("Is car == 'subaru'? I predict True.")
print(car == "subaru")

print("\nIs car == 'audi'? I predict False")
print(car == "audi")

# Basic math fun
subtraction  = 11-3
division = 16/2
addition = 4+4
modulus = 88 % 10

print(subtraction)
print(int(division))
print(addition)
print(modulus)

# Which famous person said this? 
famous_person = "Albert Einstein" # Famous theoretical physicist
famous_quote = "A person who never made a mistake never tried anything new."
message = f'{famous_person} once said: "{famous_quote}"'
print(message)

ada = "\nAda\t"
lovelace = "\nLovelace\t"
ada_stripped = ada.strip().lstrip("\n").rstrip("\t")
lovelace_stripped = lovelace.strip().lstrip("\n").rstrip("\t")
print(ada + " " + lovelace)
print(ada_stripped + " " + lovelace_stripped)

name = "ada lovelace" # British computer scientist
print(name.title())

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)

# Greets the user using all kinds of neat tricks!
user_name = input()
greeting_title = f"Hello {user_name.title()}, would you like to learn about Python today?"
greeting_lower = f"Hello {user_name.lower()}, would you like to learn about Python today?"
greeting_upper = f"Hello {user_name.upper()}, would you like to learn about Python today?"
print(greeting_title, greeting_lower, greeting_upper)

# System variables
var1 = sys.argv[1] # What variable type is var1?
var2 = sys.argv[2] # What variable type is var2?

print(var1)
print(var2)

var1 = sys.argv[1]
var2 = sys.argv[2]

total = var1 + var2

var3 = var1.upper()
var2 = var2.upper()

var4 = var1.count("T")
var5 = var2.count("T")

var6 = len(var1)

print(var4)

# Booleans
a = True
b = False
c = 7 > 8
d = 8 < 9

print(c)
print(d)
print(a and b)
print(a and c)
print(a and d)
print(b and c)
print(b and d)
print(c and d)
print(b and a)
print(d and c)

# Is your favorite food hamburger?
var1 = "hi"
hi = "goodbye"
var2 = "hello"
food = "hamburger"
nucleotide = "A"

print("hi")
print(var1)
print("My favorite food is",food)

# Passing system arguments and printing them on the screen by indices
file_name = sys.argv[0]
arg1 = sys.argv[1]
arg2 = sys.argv[2]
arg1_num = int(arg1)
arg2_num = int(arg2)

print(arg1)
print(arg2)

num_sum = arg1_num + arg2_num
print(num_sum)

# Running out of gas, what do? 
gasMeter = 1
stationNearby = False

if gasMeter <= 2:
    print("Your vehicle is low on gasoline.")
if gasMeter <= 2 and stationNearby is True:
    print("There is a station nearby.")
if gasMeter <= 2 and stationNearby is False:
    print("You will soon be stranded on the side of the road.")
if gasMeter > 2:
    print("Take it easy.")

# Why is Python so popular?
message = "One of Python's strengths is its diverse community."
print(message)

# Assigning values to multiple variables in 1 line!
x, y, z = 0, 1, 2  
print(x, y, z)

# This is a CONSTANT variable and should never be changed
MAX_CONNECTIONS = 1_000_000 
print(MAX_CONNECTIONS)

# Prints and remove the suffix of a file name
file_name = "python_notes.txt" 
print(file_name.removesuffix(".txt"))

# Find our if the number from user input is even or odd
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")

# Tests the call of a function
def addZeroes(aString, integer):
    newString = ""
    integerStr = range(integer)
    while len(aString) < len(integerStr):
        newString = aString[0] + "0"
    return newString

# Conditionals are fun!
Var1 = True
Var2 = False
Var3 = "help"
Var4 = "Help"

if Var1:
     print("I'm here")
elif Var3 == Var4:
     print("I'm here 2")
else:
     print("I'm here 3")

if Var3 == Var4:
     print("I'm here 4")
elif Var3 != Var4:
     print("I'm here 5")

# While loop practice:
seq = "ATGATGATG"
valid_nucleotides = ["A", "T", "G", "C"]
adenosine = "A"
guanine = "G"
cytosine = "C"
thymine = "T"

index = 0
count = 0
while index < len(seq):
    if seq[index] == adenosine:
        count += 1
    index += 1

index = 0
while index < len(seq):
    if seq[index] == guanine:
        print(f"Found {guanine} at index {index}")
        break
    index += 1

index = 0
sequence_is_valid=True
while index < len(seq):
    if seq[index] not in valid_nucleotides:
        sequence_is_valid = False
        break
    index += 1

print(count)
print(sequence_is_valid)

"""
Quiz 4 Problem 2: 

TGA is one of 64 codons and is usually a stop codon. 
However, in a small fraction of genes, TGA encodes selenocysteine, the 21st amino acid (this is real, not a fabricated example). 
You work in a lab where you recently sequenced 231 different genes. 
You want to figure out how many genes have at least one selenocysteine.
Write a program that takes a DNA sequence from the command line. 
You may assume the following: 
1) your sequence will only contain nucleotides (A, C, G, and T), 
2) all of the nucleotides will be uppercase, and 
3) the length of the sequence will be a multiple of three.
If TGA is the last codon in a gene sequence, then it is a stop codon and not the codon for selenocysteine. 
In your program, count how many times the codon TGA appears in your sequence when it's not the last codon. 
Report the number of selenocysteines in the gene or if there are no selenocysteines in the gene. 
Don't forget that since this sequence only contains codons, codons start at positions 0, 2, 5, 8, etc. 
You must use a while loop for this problem, or you will fail. You may not use the word for anywhere in your program.
"""

# Incorrect code: 
seq = sys.argv[1]
selenocysteine_count = 0
index = 0

while index < len(seq):
    codon = seq[::3]
    if codon == "TGA":
        selenocysteine_count += 1
    index += 3
if seq[-1:-4] == "TGA":
    selenocysteine_count -= 1

print(f"{seq}: {selenocysteine_count} selenocysteines")

# Correct code:
seq = sys.argv[1]
selenocysteine_count = 0
index = 0

while index < len(seq) - 3:  # Stop BEFORE the last codon
    codon = seq[index:index+3]
    if codon == "TGA":
        selenocysteine_count += 1
    index += 3

for index in range(0, len(seq) - 3, 3):  # Start at 0, stop before last codon, step by 3
    codon = seq[index:index+3]
    if codon == "TGA":
        selenocysteine_count += 1

print(f"{seq}: {selenocysteine_count} selenocysteines")

"""
* Quiz 5 Problem 1:
Write a program that takes two arguments from the command line. The first is the file to open and read. 
The second is the file to write to. The first file has two numbers on each line, separated by a tab. 
Your task is to read the numbers, add them, and write them and their sum to the new file. 
The input file is tab-delimited, and the output will be tab-delimited. 
Your program will fail if you use the words inputfile or outputfile anywhere in your program. 
You must retrieve the names of the input and output files from the command line. 
You will not print anything to the screen, but after the program runs, 
I'll print the contents of your file to the screen so you can see what your output has in it. 

Each line of the input will be formatted as such (tabs shown):  2\t3

Given the above input, the output should be: 2\t+\t3\t=\t5

Example 1:
Example input file (I have included the tabs, in red, below even though they're actually invisible to us):

3\t5

-1\t0

37\t19

1111\t19

Given the example file above, your program should create the following exact file:

3\t+\t5\t=\t8 

-1\t+\t0\t=\t-1

37\t+\t19\t=\t56

1111\t+\t19\t=\t1130
"""

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, "r") as inf, open(output_file, "w") as outf:
    for line in inf:
        line = line.strip()
        parts = line.split("\t")
        num1 = int(parts[0])
        num2 = int(parts[1])
        total = num1 + num2
        outf.write(f"{num1}\t+\t{num2}\t=\t{total}\n")

"""
* Quiz 5 Problem 2:
Write a program that takes three arguments from the command line. The first is the file to open and read. 
The second is the file to write to. The third is a codon. The first file you will read is sequences, one per line. 
You may assume that the sequences are all valid and all uppercase. 
The second argument is the file to which you will create and write your answers. For this program, do the following:

Open the file for reading.
Read one line from the file.
Count how often the codon (the third command line argument) appears in the sequence. 
Write the sequence followed by a tab, the codon you searched for followed by a tab, 
and the number of times the codon appears in the sequence.
You may not use any of the following: string.count(), string.replace(), or a regular expression. 
Anything else we have covered so far this semester is allowed. 
Finally, you must get the names of the input and output files from the command line. 
(I will change the names each time to make sure your code will only work if you do.)
You won't print anything to the screen. All of your answers will be written to the output file. 
However, after your program runs, I will print the contents of your file to the server, 
so you can see that you are writing the correct things to the output file.

Examples 1 and 2 use the following input file called input.txt (there are no blank lines in the file):

ATGATGGATGCCC

AAAA

AAACCCTTTGGG

Example 1:
If I execute the following command:

studentcode.py "input.txt" "output.txt" "ATG"

Example output file (I have included the tabs, in red, below even though they're actually invisible to us):

ATGATGGATGCCC\tATG\t3

AAAA\tATG\t0

AAACCCTTTGGG\tATG\t0

Example 2:
If I execute the following command:

studentcode.py "input.txt" "output.txt" "AAA"

Example output file (I have included the tabs, in red, below even though they're actually invisible to us):

ATGATGGATGCCC\tAAA\t3

AAAA\tAAA\t2 (***note that the count here is two-overlapping AAA; this will make it easier for you to code)

AAACCCTTTGGG\tAAA\t1
"""

input_file = sys.argv[1]
output_file = sys.argv[2]
codon = sys.argv[3]

with open(input_file, "r") as inf, open(output_file, "w") as outf:
    for line in inf:
        sequence = line.strip()
        count = 0
        # Slide through the sequence checking for the codon
        for i in range(len(sequence) - len(codon) + 1):
            if sequence[i:i+len(codon)] == codon:
                count += 1
        outf.write(f"{sequence}\t{codon}\t{count}\n")

"""
* Quiz 5 Problem 3
Write a program that takes two arguments from the command line. The first is the file to open and read. The second is the file to write to. The file you will read has names of people: first name, middle name, and last name. The file is tab-delimited. Names may be all uppercase, all lowercase, or mixed case. Your task is to open the file, read the names, remove the middle name, alphabetize them, and print the names in the new order to the second command line argument. All text printed to the out file should be lowercase, and there should not be blank lines between each name you print to the screen. Your program will fail if you use the words inputfile or outputfile anywhere in your program. You must retrieve the names of the input and output files from the command line. You will not print anything to the screen, but after the program runs, I'll print the contents of your file to the screen so you can see what your output has in it. (Hint: You do not need to try alphabetizing the names by considering the first and second names separately. After converting the names to lowercase, concatenate them with a tab between them and then alphabetize them.)

Example 1:
Example input file (I have included the tabs, in red, below even though they're actually invisible to us):

Joseph\tF.\tSmith

George\tAlbert\tSMITH

joseph\tfieldinG\tsmiTH

eLiza\troxcy\tSNOw

CaMiLle\tN\tJohnSon

Given the example file above, your program should create the following exact file:

camille\tjohnson

eliza\tsnow

george\tsmith

joseph\tsmith

joseph\tsmith
"""

infile = sys.argv[1]
outfile = sys.argv[2]
names_sorted = []

with open(infile, "r") as inf:
    for line in inf:
        line = line.strip()
        names = line.split("\t")
        first_last = f"{names[0]}\t{names[2]}".lower()
        names_sorted.append(first_last)
names_sorted.sort()

with open(outfile, "w") as outf:
    for name in names_sorted:
        outf.write(f"{name}\n")

"""
# Quiz 8 Problem 2
Build a small peptide given RNA codons
"""

# Incorrect Code:
codons_file = sys.argv[1]
codon = sys.argv[2]
codons = {}
    
with open(codons_file, "r") as inf:
    for line in inf:
        field = line.strip().split("\t")
        codons[field[0]] = field[1]

def FindAmino(codons, codon):
    prot_seq = []
    with open(codon, "r") as inf:
        for line in inf:
            field = line.strip()
            for key, value in codons.items():
                if field == codons.keys():
                    prot_seq.append(codons.values())
        "".join(prot_seq)
        return prot_seq

peptide = FindAmino(codons, codon)
print(peptide)

# Corrected Code:
codons_file = sys.argv[1]
codon = sys.argv[2]
codons = {}

with open(codons_file, "r") as inf:
    for line in inf:
        field = line.strip().split("\t")
        codons[field[0]] = field[1]

def FindAmino(codons, codon): # If one codon per line
    prot_seq = []
    with open(codon, "r") as inf:
        for line in inf:
            field = line.strip()
            prot_seq.append(codons.get(field, "X"))  # "X" for unknown codons
    prot_seq = "".join(prot_seq)
    return prot_seq


def FindAmino(codons, codon): # If codons all on one line
    prot_seq = []
    with open(codon, "r") as inf:
        for line in inf:
            sequence = line.strip()
            # Split sequence into 3-letter codons
            for i in range(0, len(sequence), 3):
                triplet = sequence[i:i+3]
                if len(triplet) == 3:  # skip incomplete trailing codons
                    amino_acid = codons.get(triplet, "X")  # "X" = unknown codon
                    prot_seq.append(amino_acid)
    prot_seq = "".join(prot_seq)
    return prot_seq

peptide = FindAmino(codons, codon)
print(peptide)
