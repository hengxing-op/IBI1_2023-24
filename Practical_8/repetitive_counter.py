# Initialize the sequence with the given string
seq = 'ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA'

# Function to count overlapping instances of repetitive elements
def count_repetitive_elements(sequence, pattern):
    count = 0
    i = 0
    while i <= len(sequence) - len(pattern):
        # Check if the current substring matches the pattern
        if sequence[i:i+len(pattern)] == pattern:
            count += 1
            i += 1  # Move one position forward to count overlapping patterns
        else:
            i += 1
    return count

# Count the occurrences of 'GTGTGT' and 'GTCTGT'
count_GTGTGT = count_repetitive_elements(seq, 'GTGTGT')
count_GTCTGT = count_repetitive_elements(seq, 'GTCTGT')

# Sum both two types
Total_repetitive_count = count_GTGTGT + count_GTCTGT

# Print the counts
print(f"Number of repetitive instances: {Total_repetitive_count}")
