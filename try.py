def remove_dups(name1, name2):
    return [e for e in name1 if e not in name2]

L1 = [1,2,3,4]
L2 = [1,2,5,6]
L1 = remove_dups(L1, L2)
print(L1)  # Output should be [3, 4]
print(L2)  # Output remains unchanged [1, 2, 5, 6]