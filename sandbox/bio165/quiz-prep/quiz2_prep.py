# Quiz 2 prep 

import sys

## Problem 1
seq1 = sys.argv[1]
seq2 = sys.argv[2]
seq3 = sys.argv[3]

seq1_A = []
seq2_A = []

for i in seq1:
    if i == "A":
        seq1_A.append(i)
for i in seq2:
    if i == "A":
        seq2_A.append(i)

if len(seq1_A) > len(seq2_A):
    print("Sequence 1 has more adenine bases!")
elif len(seq2_A) > len(seq1_A):
    print("Sequence 2 has more adenine bases!")
else:
    print("They have the same amount of adenine bases!")

## Problem 2
if seq1 == seq2 or seq1 == seq3 or seq2 == seq3:
    print("There are some duplicates in your sequences!")

## Problem 3
seq1_AT = []
seq2_AT = []
seq3_AT = []

for char in seq1:
    if char in ["A", "T"]:
        seq1_AT.append(char)
for char in seq2:
    if char in ["A", "T"]:
        seq2_AT.append(char)
for char in seq3:
    if char in ["A", "T"]:
        seq3_AT.append(char)

seq1_AT_percentage = len(seq1_AT) / len(seq1) * 100
seq2_AT_percentage = len(seq2_AT) / len(seq2) * 100
seq3_AT_percentage = len(seq3_AT) / len(seq3) * 100

print(seq1_AT_percentage)
print(seq2_AT_percentage)
print(seq3_AT_percentage)

## Problem 4
seq1_GC = []
seq2_GC = []
seq3_GC = []

for nc in seq1:
    if nc in ["G", "C"]:
        seq1_GC.append(nc)
for nc in seq2:
    if nc in ["G", "C"]:
        seq2_GC.append(nc)
for nc in seq3:
    if nc in ["G", "C"]:
        seq3_GC.append(nc)

if len(seq1_AT) > len(seq1_GC) or seq1_AT_percentage > 50:
    print("Sequence 1 is AT rich")
elif len(seq1_AT) == len(seq1_GC):
    print("There is the same amount of AT and GC content")
if len(seq2_AT) > len(seq2_GC) or seq2_AT_percentage > 50:
    print("Sequence 2 is AT rich")
elif len(seq2_AT) == len(seq2_GC):
    print("There is the same amount of AT and GC content")
if len(seq3_AT) > len(seq3_GC) or seq3_AT_percentage > 50:
    print("Sequence 3 is AT rich")
elif len(seq3_AT) == len(seq3_GC):
    print("There is the same amount of AT and GC content")
