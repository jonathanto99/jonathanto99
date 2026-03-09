# 1. We define our data: A dictionary mapping Amino Acids (Key) to Monoisotopic Mass (Value)
# Note: These are simplified masses for the exercise.
aa_weights = {
    'A': 71.03711, 'R': 156.10111, 'N': 114.04293, 'D': 115.02694,
    'C': 103.00919, 'E': 129.04259, 'Q': 128.05858, 'G': 57.02146,
    'H': 137.05891, 'I': 113.08406, 'L': 113.08406, 'K': 128.09496,
    'M': 131.04049, 'F': 147.06841, 'P': 97.05276, 'S': 87.03203,
    'T': 101.04768, 'W': 186.07931, 'Y': 163.06333, 'V': 99.06841
}

# 2. Our input data (A fake protein sequence)
protein_sequence = "SKADYEK"

# 3. Initialize variable to track total mass
total_mass = 0.0

# --- TODO: YOUR CODE STARTS HERE ---

# Task: Iterate through 'protein_sequence'. 
# For every amino acid, look up its weight in 'aa_weights' and add it to 'total_mass'.
# Hint: Use a for loop: `for aa in protein_sequence:`
# Hint: Access dict values using `aa_weights[aa]`



# --- YOUR CODE ENDS HERE ---

# 4. output the result
# In real mass spec, we usually add the weight of a water molecule (approx 18.01056) to the final uncharged polymer
total_mass = total_mass + 18.01056

print(f"Sequence: {protein_sequence}")
print(f"Total Mass: {total_mass:.4f} Da")

# Verification: For "SKADYEK", the result should be roughly ~825.36 Da