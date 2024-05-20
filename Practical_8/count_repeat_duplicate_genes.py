# count_repeat_duplicate_genes.py

def count_repetitive_elements(sequence, pattern):
    count = 0
    i = 0
    while i <= len(sequence) - len(pattern):
        if sequence[i:i+len(pattern)] == pattern:
            count += 1
            i += 1
        else:
            i += 1
    return count

def get_duplicate_genes_with_repeats(input_file, output_file, pattern):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        write_flag = False
        gene_sequence = ""
        gene_name = ""
        for line in infile:
            if line.startswith('>'):
                if write_flag and gene_sequence:
                    repeat_count = count_repetitive_elements(gene_sequence, pattern)
                    outfile.write(f">{gene_name} | Repeats: {repeat_count}\n{gene_sequence}\n")
                if 'duplication' in line:
                    gene_name = line.split()[0][1:]
                    write_flag = True
                    gene_sequence = ""
                else:
                    write_flag = False
            else:
                if write_flag:
                    gene_sequence += line.strip()
        if write_flag and gene_sequence:
            repeat_count = count_repetitive_elements(gene_sequence, pattern)
            outfile.write(f">{gene_name} | Repeats: {repeat_count}\n{gene_sequence}\n")

# Ask user for the repetitive sequence
repeat_sequence = input("Please enter the repetitive sequence (GTGTGT or GTCTGT): ")

# Create the output file name based on the repetitive sequence
output_file_name = f"{repeat_sequence}_duplicate_genes.fa"

# Run the function with the given file names and repetitive sequence
get_duplicate_genes_with_repeats('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', output_file_name, repeat_sequence)