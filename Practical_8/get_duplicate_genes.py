def get_duplicate_genes(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        write_flag = False
        for line in infile:
            if line.startswith('>'):
                # Check if the description contains the word 'duplication'
                if 'duplication' in line:
                    # Extract the gene name (assumed to be the first word after '>')
                    gene_name = line.split()[0][1:]
                    outfile.write(f">{gene_name}\n")
                    write_flag = True
                else:
                    write_flag = False
            else:
                if write_flag:
                    outfile.write(line)

# Run the function with the given file names
get_duplicate_genes('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'duplicate_genes.fa')