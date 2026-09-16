# Hollyn White
# CS417: Assignment 2
# Problem 4: 
# Using the random.randint() and random.choice()functions from the Python random module, write a function that 
# will mutate a DNA string. Then, use the frequency table function to analyze the changes that occur in frequencies 
# if you randomly change 100 positions in a 1000 gene DNA sequence. Your program should randomly generate a DNA 
# string with 1000 bases, display the frequency table of this string, apply 100 mutations to the string, and then 
# print the frequency table for the mutated string.

import random

# frequencyTable(dna) function
def frequencyTable(dna):
    frequency = {
        "A": 0,
        "C": 0,
        "G": 0,
        "T": 0
    }

    for base in dna:
        frequency[base] = frequency[base] + 1

    return frequency

# mutate(dna) function
def mutate(dna):
    for i in range(100):
        position = random.randint(0, 999)
        dna[position] = random.choice(["A", "C", "G", "T"])

# main() function
def main():
    dna = []

    for i in range(1000):
        dna.append(random.choice(["A", "C", "G", "T"]))

    frequency = frequencyTable(dna)
    print("-Frequency Tables-")
    print("Original frequency:")
    print("A:", frequency["A"])
    print("C:", frequency["C"])
    print("G:", frequency["G"])
    print("T:", frequency["T"])

    mutate(dna)
    frequency = frequencyTable(dna)
    print("Mutated frequency:")
    print("A:", frequency["A"])
    print("C:", frequency["C"])
    print("G:", frequency["G"])
    print("T:", frequency["T"])

if __name__ == "__main__":
    main()