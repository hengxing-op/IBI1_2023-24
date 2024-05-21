# Import necessary libraries
import blosum as bl

# Define the paths to the FASTA files using raw strings to avoid Unicode escape errors
file_path_human = r"C:\Users\Star\Desktop\IBIpractice\IBI1_2023-24\Practical_13\SLC6A4_HUMAN.fa"
file_path_mouse = r"C:\Users\Star\Desktop\IBIpractice\IBI1_2023-24\Practical_13\SLC6A4_MOUSE.fa"
file_path_rat = r"C:\Users\Star\Desktop\IBIpractice\IBI1_2023-24\Practical_13\SLC6A4_RAT.fa"

# Function to read the sequence from a FASTA file
def read_sequence(file_path):
    sequence = ''
    with open(file_path, 'r') as file:
        for line in file:
            if not line.startswith('>'):  # Ignore header lines
                sequence += line.strip()  # Append sequence lines
    return sequence

# Read sequences from the files
seq_human = read_sequence(file_path_human)
seq_mouse = read_sequence(file_path_mouse)
seq_rat = read_sequence(file_path_rat)

# Initialize BLOSUM62 matrix
matrix = bl.BLOSUM(62)

# Function to calculate alignment score and identical percentage
def calculate_alignment(seq1, seq2, matrix):
    alignment_score = 0
    identical_count = 0
    
    for i in range(len(seq1)):
        alignment_score += matrix[seq1[i]][seq2[i]]  # Sum the BLOSUM scores
        if seq1[i] == seq2[i]:
            identical_count += 1  # Count identical amino acids
    
    identical_percentage = (identical_count / len(seq1)) * 100  # Calculate percentage
    return alignment_score, identical_percentage

# Calculate alignment scores and identical percentages for each pair of sequences
alignment_score_human_mouse, identical_percentage_human_mouse = calculate_alignment(seq_human, seq_mouse, matrix)
alignment_score_human_rat, identical_percentage_human_rat = calculate_alignment(seq_human, seq_rat, matrix)
alignment_score_mouse_rat, identical_percentage_mouse_rat = calculate_alignment(seq_mouse, seq_rat, matrix)

# Print the results
print(f"The alignment score for human and mouse sequence is {alignment_score_human_mouse}.")
print(f"The identical percentage of human and mouse sequence is {identical_percentage_human_mouse}%.")
print(f"The alignment score for human and rat sequence is {alignment_score_human_rat}.")
print(f"The identical percentage of human and rat sequence is {identical_percentage_human_rat}%.")
print(f"The alignment score for mouse and rat sequence is {alignment_score_mouse_rat}.")
print(f"The identical percentage of mouse and rat sequence is {identical_percentage_mouse_rat}%.")

# Determine which sequences are most closely related
if alignment_score_mouse_rat > alignment_score_human_rat and alignment_score_mouse_rat > alignment_score_human_mouse:
    print("The sequence of mouse and the sequence of rat are most closely related.")
elif alignment_score_human_rat > alignment_score_human_mouse and alignment_score_human_rat > alignment_score_mouse_rat:
    print("The sequence of human and the sequence of rat are most closely related.")
else:
    print("The sequence of human and the sequence of mouse are most closely related.")

# Determine which rodent is a better model organism for human studies
better_model_organism = "mouse" if alignment_score_human_mouse > alignment_score_human_rat else "rat"
print(f"The {better_model_organism} would be a better model organism for studying variation in the SLC6A4 gene in humans.")