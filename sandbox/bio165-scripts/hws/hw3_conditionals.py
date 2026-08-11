import sys

# 1. Longest name
first_name = sys.argv[1]
last_name = sys.argv[2]

if len(first_name) > len(last_name):
    print(f"{first_name} is longer than {last_name}.")
elif len(last_name) > len(first_name):
    print(f"{last_name} is longer than {first_name}.")
elif len(first_name) == len(last_name):
    print(f"{first_name} is the same length as {last_name}.")

# 2. Same DNA?
dna_seq = sys.argv[1]
dna_seq2 = sys.argv[2]

if dna_seq == dna_seq2:
    print("They are the same sequence.")
elif dna_seq != dna_seq2:
    print("They are not the same sequence.")

# 3. Highest GC content
dna_gc_seq = sys.argv[1]
dna_gc_seq_list = []

dna_gc_seq2 = sys.argv[2]
dna_gc_seq2_list = []

dna_gc_seq3 = sys.argv[3]
dna_gc_seq3_list = []

for i in dna_gc_seq:
    if i in ["G", "C"]:
        dna_gc_seq_list.append(i)
for i in dna_gc_seq2:
    if i in ["G", "C"]:
        dna_gc_seq2_list.append(i)
for i in dna_gc_seq3:
    if i in ["G", "C"]:
        dna_gc_seq3_list.append(i)

if len(dna_gc_seq_list) > len(dna_gc_seq2_list) and len(dna_gc_seq_list) > len(dna_gc_seq3_list):
    print(f"{dna_gc_seq} has the highest GC content.")
elif len(dna_gc_seq2_list) > len(dna_gc_seq_list) and len(dna_gc_seq2_list) > len(dna_gc_seq3_list):
    print(f"{dna_gc_seq2} has the highest GC content.")
elif len(dna_gc_seq3_list) > len(dna_gc_seq_list) and len(dna_gc_seq3_list) > len(dna_gc_seq2_list):
    print(f"{dna_gc_seq3} has the highest GC content.")

# 4. Order DNA Shortest to Longest
seq1 = sys.argv[1]
seq2 = sys.argv[2]
seq3 = sys.argv[3]

if len(seq1) < len(seq2) and len(seq1) < len(seq3):
    shortest = seq1
    if len(seq2) < len(seq3):
        middle, longest = seq2, seq3 # Python can only handle it this way
    else:
        middle, longest = seq3, seq2
elif len(seq2) < len(seq1) and len(seq2) < len(seq3):
    shortest = seq2
    if len(seq1) < len(seq3):
        middle, longest = seq1, seq3
    else:
        middle, longest = seq3, seq1
elif len(seq3) < len(seq1) and len(seq3) < len(seq2):
    shortest = seq3
    if len(seq1) < len(seq2):
        middle, longest = seq1, seq2
    else:
        middle, longest = seq2, seq1

# 4.1 A different (and shorter) way of doing this
print(f"{shortest},{middle},{longest}")

sequences = [sys.argv[1], sys.argv[2], sys.argv[3]]
sorted_sequences = sorted(sequences, key=len)

print(f"{sorted_sequences[0]},{sorted_sequences[1]},{sorted_sequences[2]}")
