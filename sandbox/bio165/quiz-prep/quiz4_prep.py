import sys

dna_seq = sys.argv[1]
index = 0

while index < len(dna_seq):
    nuc = dna_seq[index]
    print(f"The index is: {index}, and the nucleotide is: {nuc}.")
    index += 1

for index, nuc in enumerate(dna_seq):
    print(f"The index is: {index}, and the nucleotide is: {nuc}.")

# * For Loop Problem 1:
# Write a program that accepts one DNA sequence from the command line.
# Count how many times each nucleotide (A, T, G, C) appears in the sequence.
# Print the counts in this format: "A: X, T: Y, G: Z, C: W"
# You must use a for loop.

dna_seq = sys.argv[1].upper()

seq_list_A = []
seq_list_T = []
seq_list_G = []
seq_list_C = []

for nuc in dna_seq:
    if nuc == "A":
        seq_list_A.append(nuc)
    elif nuc == "T":
        seq_list_T.append(nuc)
    elif nuc == "G":
        seq_list_G.append(nuc)
    elif nuc == "C":
        seq_list_C.append(nuc)

print(f"A: {len(seq_list_A)}, T: {len(seq_list_T)}, G: {len(seq_list_G)}, C: {len(seq_list_C)}")

# * For Loop Problem 2:
# Write a program that accepts one DNA sequence from the command line.
# Reverse the sequence and print it to the screen.
# You may not use slicing (sequence[::-1]).
# You must use a for loop.

dna_seq = sys.argv[1].upper()
seq_list = []

for nuc in dna_seq:
    seq_list.insert(0, nuc)

print(seq_list)

# * For Loop Problem 3:
# Write a program that accepts an unknown number of numbers from the command line.
# Find and print the largest number in the list.
# You may not use max().
# You must use a for loop.

num_list = [int(x) for x in sys.argv[1:]]
biggest = num_list[0]

for num in num_list:
    if num > biggest:
        biggest = num

print(biggest)

# * While Loop Problem 1:
# Write a program that accepts one DNA sequence from the command line.
# Count how many times each nucleotide (A, T, G, C) appears in the sequence.
# Print the counts in this format: "A: X, T: Y, G: Z, C: W"
# You must use a while loop.

dna_seq = sys.argv[1].upper()
A_count = 0
T_count = 0
G_count = 0
C_count = 0
index = 0

while index < len(dna_seq):
    nuc = dna_seq[index]
    if nuc == "A":
        A_count += 1
    elif nuc == "T":
        T_count += 1
    elif nuc == "G":
        G_count += 1
    elif nuc == "C":
        C_count += 1
    index += 1

print(f"A: {A_count}, T: {T_count}, G: {G_count}, C: {C_count}")

# * While Loop Problem 2:
# Write a program that accepts one DNA sequence from the command line.
# Reverse the sequence and print it to the screen.
# You may not use slicing (sequence[::-1]).
# You must use a while loop.

dna_seq = sys.argv[1]
reverse_seq = []
index = 0

while index < len(dna_seq):
    nuc = dna_seq[index]
    reverse_seq.insert(0, nuc)
    index += 1

print("".join(reverse_seq))

# * While Loop Problem 3:
# Write a program that accepts an unknown number of numbers from the command line.
# Find and print the largest number in the list.
# You may not use max().
# You must use a while loop.

random_nums = sys.argv[1:]
index = 0
largest = int(random_nums[0])

while index < len(random_nums):
    num = int(random_nums[index])
    if num > largest:
        largest = num
    index += 1

print(largest)
