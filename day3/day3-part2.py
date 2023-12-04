import re


def find_numbers_with_indices(input_string):
    numbers_with_indices = []
    for match in re.finditer(r'\d+', input_string):
        number = int(match.group())
        start_index = match.start()
        end_index = match.end() - 1  # end() returns the index after the last matched character
        numbers_with_indices.append((number, start_index, end_index))
    return numbers_with_indices


def calculate_gear_ratio(before, current, after):
    gear_ratio_sum = 0
    before_numbers = find_numbers_with_indices(before)
    after_numbers = find_numbers_with_indices(after)
    current_numbers = find_numbers_with_indices(current)

    for i, char in enumerate(current):
        if char == '*': #Find numbers around it
            numbers = []

            # Filter numbers based on indices
            for number, start, end in before_numbers + after_numbers + current_numbers:
                if start <= i + 1 and end >= i - 1:
                    numbers.append(number)

            # Calculate gear ratio if exactly two numbers are found
            if len(numbers) == 2:
                gear_ratio_sum += numbers[0] * numbers[1]

    return gear_ratio_sum



############# Main Part ################
before = ""
current = ""
after = ""
sum = 0
file = open('input.txt', 'r')

for line in file:

    line = line.strip()
    index = 0
    before = current
    current = after 
    after = line

    if current != "":
        sum += calculate_gear_ratio(before, current, after)

# Special case for the last row 
before = current
current = after
after = ""
sum += calculate_gear_ratio(before, current, after)

print(sum)
