import sys

# Problem 1:
num1 = sys.argv[1]
num2 = sys.argv[2]
num3 = sys.argv[3]
num4 = sys.argv[4]

num1_list = [int(num1[:2])]
num3_list = [int(num3[:2])]
num2_list = [int(num2[:2])]
num4_list = [int(num4[:2])]

total_list = num1_list + num2_list + num3_list + num4_list
total_list.sort()

print(total_list)

# Problem 2:
exons = sys.argv[1:]

start_codon = []

for seq in exons:
    if seq[:3] == "ATG":
        start_codon.append(seq)
        print(seq)

if start_codon == []:
    print("There is no start codon.")
