def longest_zeros(sequence):
    longest = 0
    current = 0
    for i in range(len(sequence)):
        if sequence[i] == '0':
            current += 1
        else:
            longest = max(longest, current)
            current = 0
        
    return longest
