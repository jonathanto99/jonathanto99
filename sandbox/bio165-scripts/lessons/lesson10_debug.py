import sys

##### Begin Part 1

seq1 = sys.argv[1]
seq1 = seq1.upper()

if len(seq1.replace(" ", "")) == 0:
    print("ERROR: You must enter a DNA sequence")
    sys.exit()

temp_seq = seq1.replace("A", "").replace("G", "").replace("C", "").replace("T", "").replace(" ", "")
if len(temp_seq) != 0:
    print("ERROR: Invalid DNA sequence")
    sys.exit()

seq2 = sys.argv[2]
seq2 = seq2.upper()

if len(seq2.replace(" ", "")) == 0:
    print("ERROR: You must enter a DNA sequence")
    sys.exit()

temp_seq = seq2.replace("A", "").replace("G", "").replace("C", "").replace("T", "").replace(" ", "")
if len(temp_seq) != 0:
    print("ERROR: Invalid DNA sequence")
    sys.exit()

seq3 = sys.argv[3]
seq3 = seq3.upper()

if len(seq3.replace(" ", "")) == 0:
    print("ERROR: You must enter a DNA sequence")
    sys.exit()

temp_seq = seq3.replace("A", "").replace("G", "").replace("C", "").replace("T", "").replace(" ", "")
if len(temp_seq) != 0:
    print("ERROR: Invalid DNA sequence")
    sys.exit()

##### End Part 1
##### Begin Part 2

seq1 = seq1.replace(" ", "")
seq2 = seq2.replace(" ", "")
seq3 = seq3.replace(" ", "")

print("Sequence 1: " + str(len(seq1)))
print("Sequence 2: " + str(len(seq2)))
print("Sequence 3: " + str(len(seq3)))

##### End Part 2
##### Begin Part 3

final_seq = seq1 + seq2 + seq3
countGC = final_seq.count("G") + final_seq.count("C")

print(final_seq)
print(float(countGC) / len(final_seq) * 100)

##### End Part 3
