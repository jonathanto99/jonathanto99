# Problem 4: Computing GC Content

# Pseudocode:
'''
1. Read the FASTA file and parse the sequences in each line. Consider the lines starting with '>' as headers and the subsequent lines as sequences.
2. For each line, count the instances where G and C appear. Add these counts to get the total GC count for that sequence.
3. Calculate the GC content percentage using the formula: (GC count / total length of the sequence) * 100. 
4. Record the sequence ID that has the highest percentage of GC content along with the percentage value. 
5. Print the sequence ID and the highest GC content percentage. 
'''

# Program:
from collections import Counter

fasta_ID = {}

# 1. The Parser
with open("rosalind_gc.md") as dna_fasta: # Opens the file
    for line in dna_fasta: # Reads it line by line
        if line.startswith(">"): # Checks if the line starts with ">"
            current_ID = line.strip().lstrip(">") # Strips the ">" and other possible whitespace characters
            fasta_ID[current_ID] = "" # Records the current_ID into the dictionary first
        else:
            current_sequence = line.strip().lstrip(">") # Strips the ">" and other possible whitespace characters
            fasta_ID[current_ID] += current_sequence # Joins the current_sequence to the current_ID

# 2. The Calculator
def calculate_gc_content(dna_seq):
    counts = Counter(dna_seq) # Uses counter function to count DNA sequences
    gc_counts = counts["G"] + counts["C"] # Adds the counts of G & C together
    gc_percentage = (gc_counts / len(dna_seq)) * 100 # Calculates the percentage through dividing by 100
    return gc_percentage # returns the number

# 3. The Referee
def get_score(seq_id):
    return calculate_gc_content(fasta_ID[seq_id]) # Takes an ID, looks up the DNA, and returns the score

if __name__ == "__main__":
    winner_id = max(fasta_ID, key=get_score) # Finds the ID with the highest score in one line
    # Printing the results
    print(winner_id)
    print(calculate_gc_content(fasta_ID[winner_id]))
