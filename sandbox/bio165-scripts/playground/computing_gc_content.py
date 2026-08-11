'''
# Computing GC Content
# Pseudocode:
1. Read the FASTA file and parse the sequences in each line. Consider the lines starting with '>' as headers and the subsequent lines as sequences.
2. For each line, count the instances where G and C appear. Add these counts to get the total GC count for that sequence.
3. Calculate the GC content percentage using the formula: (GC count / total length of the sequence) * 100. 
4. Record the sequence ID that has the highest percentage of GC content along with the percentage value. 
5. Print the sequence ID and the highest GC content percentage. 
'''

# * Program:
#! /usr/bin/env python

from collections import Counter

path = "rosalind_gc.txt"

def parse_fasta(path):
    # 1. The Parser
    headers = {}
    header = None
    with open(path, "r") as inf: # Opens the file
        for raw in inf: # Check each line in the file
            line = raw.strip() # Clean up each line as we parse through it
            if not line:
                continue
            if line.startswith(">"): # If the line starts with ">", its an ID
                header = line.lstrip(">").strip() # Strip the ID of its ">" and any other potential whitespace
                headers[header] = [] # Adds the ID to the dictionary
            else:
                if header is None:
                    raise ValueError("FASTA missing initial header")
                headers[header].append(line) # If the line doesn't start with a ">", then its a sequence and we'll glue it to the ID
    return {key: "".join(value) for key, value in headers.items()}

# 2. The Calculator
# We need variables to keep track of the winner as we look at them one by one. We manually pull each ID out of the dictionary
def find_best_gc(headers):
    # Find sequence ID with highest GC content
    best_id = "" # Who's the winner? 
    highest_gc = 0.0 # What is the highest GC count? 
    
    for seq_id in headers: 
        current_dna_string = headers[seq_id] # A. Get the explicit Input for this round
        counts = Counter(current_dna_string) # B. Calculate the GC (Modular logic inline)
        gc_count = counts["G"] + counts["C"]
        current_gc_percentage = (gc_count / len(current_dna_string)) * 100 # Explicitly divide by the length of the current string
        
        if current_gc_percentage > highest_gc: # C. Compare Output. If this one is better than our current best, update the record
            highest_gc = current_gc_percentage
            best_id = seq_id
    
    return best_id, highest_gc

# 3. The Result 
if __name__ == "__main__":
    headers = parse_fasta(path)
    best_id, highest_gc = find_best_gc(headers)
    print(best_id)
    print(highest_gc)
