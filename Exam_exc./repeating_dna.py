# FUNCTION HELP 100%
def get_repeating_DNA(sequence):
    subsequences = []
    for i in range(len(sequence) - 10):
        current = sequence[i: i + 10]
        chopped_sequence = sequence[i + 1:]
        if current not in subsequences and current in chopped_sequence:
            subsequences.append(current)
    return subsequences


test = "AAAAAACCCCAAAAAACCCCTTCAAAATCTTTCAAAATCT"
result = get_repeating_DNA(test)
print(result)