# Problem 1: Create a list and access elements
dna_bases = ["A", "T", "G", "C"]
print(dna_bases[0])  # What prints?
print(dna_bases[-1])  # What prints?

# Problem 2: Modify a list
proteins = ["methionine", "alanine"]
proteins.append("glycine")
proteins[0] = "valine"
# What does proteins look like now?

# Problem 3: Iterate through a list (for loop)
codons = ["ATG", "TAA", "GGC"]
for codon in codons:
    print(codon.lower())

# Problem 4: List slicing
sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sequence[2:5])  # What prints?
print(sequence[:4])   # What prints?
print(sequence[5:])   # What prints?

# Problem 5: Combining concepts (conditionals + lists)
genes = ["BRCA1", "TP53", "EGFR"]
search_gene = "TP53"
if search_gene in genes:
    print(f"{search_gene} found!")

# Problem 6: Using a for loop to filter
numbers = [1, 2, 3, 4, 5, 6]
evens = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)
# What does evens contain?
