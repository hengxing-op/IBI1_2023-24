# count_repeat_duplicate_genes.py

import os

# Path to the input FASTA file
input_file = r"C:\Users\Star\Desktop\IBIpractice\IBI1_2023-24\Practical_8\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"

# Function to count overlapping instances of a pattern
def count_repeats(sequence, pattern):
    count = 0
    start = 0
    while True:
        start = sequence.find(pattern, start)
        if start == -1:
            break
        count += 1
        start += 1
    return count

# Function to read and filter duplicate genes with given repetitive sequence
def extract_and_count_repeats(input_path, pattern):
    output_file = f"{pattern}_duplicate_genes.fa"
    with open(input_path, 'r') as infile, open(output_file, 'w') as outfile:
        write_flag = False
        gene_name = ""
        sequence = ""

        for line in infile:
            if line.startswith(">"):
                if write_flag and pattern in sequence:
                    repeat_count = count_repeats(sequence, pattern)
                    outfile.write(f">{gene_name} | Repeats: {repeat_count}\n{sequence}\n")
                
                write_flag = "duplication" in line
                if write_flag:
                    gene_name = line.split()[0][1:] if len(line.split()) > 0 else "unknown"
                sequence = ""
            elif write_flag:
                sequence += line.strip()
        
        if write_flag and pattern in sequence:
            repeat_count = count_repeats(sequence, pattern)
            outfile.write(f">{gene_name} | Repeats: {repeat_count}\n{sequence}\n")

# Ask the user for the repetitive sequence
pattern = input("Enter the repetitive sequence (e.g., 'GTGTGT' or 'GTCTGT'): ").strip()

# Execute the function
extract_and_count_repeats(input_file, pattern)