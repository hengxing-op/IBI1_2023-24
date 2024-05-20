# Path to the input FASTA file
input_file = r"C:\Users\Star\Desktop\IBIpractice\IBI1_2023-24\Practical_8\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
# Path to the output FASTA file
output_file = r"C:\Users\Star\Desktop\IBIpractice\IBI1_2023-24\Practical_8\duplicate_genes.fa"

# Function to read and filter duplicate genes
def extract_duplicate_genes(input_path, output_path):
    with open(input_path, 'r') as infile, open(output_path, 'w') as outfile:
        write_flag = False
        gene_name = ""
        
        for line in infile:
            if line.startswith(">"):
                if "duplication" in line:
                    write_flag = True
                    # Extract and simplify the gene name
                    parts = line.split()
                    gene_name = parts[0][1:] if len(parts) > 0 else "unknown"
                    outfile.write(f">{gene_name}\n")
                else:
                    write_flag = False
            elif write_flag:
                outfile.write(line)

# Execute the function
extract_duplicate_genes(input_file, output_file)