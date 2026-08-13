import sys

"""
* #1 Convert DNA to RNA Using a For Loop 
Your program will accept one system argument: a DNA sequence (may contain upper/lower case letters or spaces). 
You may not use string.replace() for this practice. Remove all the white spaces and convert the “T” and “t” nucleotides to “U.” 
You must use a for loop. Your output should be in all upper case. 
"""

dna_seq = sys.argv[1]
rna_seq = []

for nuc in dna_seq:
    if nuc == " ":
        continue
    elif nuc == "t" or nuc == "T":
        nuc = "U"
    rna_seq.append(nuc)

rna_seq = "".join(rna_seq)
print(rna_seq.upper())


"""
* #2 Convert DNA to RNA Using a While Loop
Your program will accept one system argument: a DNA sequence (may contain upper/lower case letters or spaces). 
You may not use string.replace() for this practice. Remove all the white spaces and convert the “T” and “t” nucleotides to “U.” 
You must use a while loop. 
"""

dna_seq = sys.argv[1]
rna_seq = []
index = 0

while index < len(dna_seq):
    nuc = dna_seq[index]
    if nuc == " ":
        index += 1
        continue
    elif nuc == "t" or nuc == "T":
        nuc = "U"
    rna_seq.append(nuc)
    index += 1

rna_seq = "".join(rna_seq)
print(rna_seq.upper())


"""
* #3 Calculate the Length of a DNA Sequence
You will receive one system argument from the user: a DNA sequence. 
Calculate the length of the sequence without using len(). (You may not use len() anywhere in your program.) 
"""

dna_seq = sys.argv[1]
dna_len = 0

for nuc in dna_seq:
    dna_len += 1

print(dna_len)

"""
* #4 Alphabetize DNA With a For Loop
Your code will accept an unknown number of system arguments, each of which will be a DNA sequence. 
Convert the DNA sequences to uppercase using a for loop. Print the alphabetized list of sequences as a list. 
Your program should handle a mix of upper/lower case letters. You must use a for loop. You cannot use string.upper(). 
"""

dna_seqs = sys.argv[1:]
upper_seqs = []

for seq in dna_seqs:
    upper_seq = []
    for nuc in seq:
        if nuc == "a":
            nuc = "A"
        elif nuc == "c":
            nuc = "C"
        elif nuc == "g":
            nuc = "G"
        elif nuc == "t":
            nuc = "T"
        upper_seq.append(nuc)
    upper_seqs.append("".join(upper_seq))

upper_seqs.sort()
print(upper_seqs)

"""
* #5 Alphabetize DNA With a While Loop
Your code will accept an unknown number of system arguments, each of which will be a DNA sequence. 
Convert the DNA sequences to uppercase using a while loop. Print the alphabetized list of sequences as a list. 
Your program should handle a mix of upper/lower case letters. You must use a while loop. You cannot use string.upper(). 
"""

dna_seqs = sys.argv[1:]
upper_seqs = []
index = 0

while index < len(dna_seqs):
    upper_seq = []
    char = 0
    while char < len(dna_seqs[index]):
        nuc = dna_seqs[index][char]
        if nuc == "a":
            nuc = "A"
        elif nuc == "c":
            nuc = "C"
        elif nuc == "g":
            nuc = "G"
        elif nuc == "t":
            nuc = "T"
        char += 1
        upper_seq.append(nuc)
    index += 1
    upper_seqs.append("".join(upper_seq))

upper_seqs.sort()
print(upper_seqs)

"""
* #6 Split One List Into Two Lists With a For Loop
System arguments are stored as a list. Given an unknown number of system arguments, 
split the list of system arguments into two different lists: one that has the even numbers and one that has the odd numbers. 
Print the list with even numbers in ascending order on one line, and the list with odd numbers in ascending order on the next line. 
Just print the lists (no special formatting). You must use a for loop.
"""

sys_args = sys.argv[1:]
sys_args = [int(i) for i in sys_args]

even_args = []
odd_args = []

for arg in sys_args:
    if arg % 2 == 0:
        even_args.append(arg)
    elif arg % 2 == 1:
        odd_args.append(arg)

even_args.sort()
odd_args.sort()

print(even_args)
print(odd_args)

"""
* #7 Split One List Into Two Lists With a While Loop
System arguments are stored as a list. Given an unknown number of system arguments, 
split the list of system arguments into two different lists: one that has the even numbers and one that has the odd numbers. 
Print the list with even numbers in ascending order on one line and the list with odd numbers in ascending order on the next line. 
Just print the lists (no special formatting). You must use a while loop.
"""

sys_args = sys.argv[1:]

even_args = []
odd_args = []
index = 0

while index < len(sys_args):
    arg = sys_args[index]
    if int(arg) % 2 == 0:
        even_args.append(int(arg))
    elif int(arg) % 2 == 1:
        odd_args.append(int(arg))
    index += 1

even_args.sort()
odd_args.sort()

print(even_args)
print(odd_args)
