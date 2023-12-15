sum = 0
with open ("input.txt", "r") as file:
    for line in file:
        sequences = line.strip().split(",")
        for sequence in sequences:
            current_value = 0
            for char in sequence:
                current_value += ord(char)
                current_value *= 17
                current_value = current_value % 256
            sum+=current_value

print(sum)
