import sys

'''
# * Function Practice Problem 1
 Write a program that accepts two numbers from the command line (start and stop numbers). 
 These numbers will both be non-negative and the first will always be smaller than, or equal to, the second number. 
 Your program should print all the prime numbers between the two provided numbers.  
 Write a function that determines whether or not a number is prime. 
 If there are no prime numbers, your program should report that, too.  
'''

start_num = int(sys.argv[1])
stop_num = int(sys.argv[2])

def isPrime(num):
    # if the number is prime return True
    if num < 2:
        return False
    is_prime = True
    for divisor in range(2, num):
        if num % divisor == 0:
            is_prime = False
            break
    return is_prime

primes = [num for num in range(start_num, stop_num + 1) if isPrime(num)]

if primes:
    for prime in primes:
        print(prime)
else: # if the number isn't prime return False
    print(f"There are no prime numbers between {start_num} and {stop_num}.")

'''
# * Function Practice Problem 2
Given a file with the masses of each amino acid, aminoacidweights.txt, write a program that opens the amino acid file
and loads the weights into a dictionary (amino acid:mass key/value pairs). 
The program should accept the weights file and the protein sequence from the command line. 
Use a function that takes the dictionary and amino acid sequence as parameters and returns the mass of the protein sequence. 
The weights file is tab delimited: the single letter amino acid abbreviation is listed, then a tab, and then it's molecular weight.  
'''

amino_acid_file_path = sys.argv[1]
protein_seq = sys.argv[2]

def LoadDictionary(amino_acid_file_path):
    # populate the weights dictionary with the amino acid as key and its weight as value
    weights = {}
    with open(amino_acid_file_path, "r") as inf:
        for raw in inf:
            line = raw.strip().split("\t")
            weights[line[0]] = line[1]
    return weights

    
def CalcWeight(weights, protein_seq):
    #use the weights dictionary to calculate the mass of protein_seq
    total_mass = 0
    for amino_acid in protein_seq:
        total_mass += float(weights[amino_acid])
    return total_mass

weights = LoadDictionary(amino_acid_file_path)
result = CalcWeight(weights, protein_seq)
print(result)
