import hashlib


############ Function to perform all 4 turns ################
def spin_north(field):
    # Turn north
    for row_index, row in enumerate(field):
        for col_index, item in enumerate(row):
            if item == 'O':
                roll = 0
                comparison_row = row_index-1
                while comparison_row >= 0:
                    if field[comparison_row][col_index] == '.':
                        roll+=1
                        comparison_row-=1
                    else:
                        break
                if roll > 0:
                    field[row_index-roll][col_index] = 'O'
                    field[row_index][col_index] = '.'
    return field

def spin_west(field):
    for row_index in range(len(field)):
        for col_index in range(len(field[row_index])):
            if field[row_index][col_index] == 'O':
                roll = 0
                comparison_col = col_index - 1
                while comparison_col >= 0:
                    if field[row_index][comparison_col] == '.':
                        roll += 1
                        comparison_col -= 1
                    else:
                        break
                if roll > 0:
                    field[row_index][col_index - roll] = 'O'
                    field[row_index][col_index] = '.'
    return field


def spin_south(field):
    for row_index in range(len(field) - 1, -1, -1):
        for col_index in range(len(field[row_index])):
            if field[row_index][col_index] == 'O':
                roll = 0
                comparison_row = row_index + 1
                while comparison_row < len(field):
                    if field[comparison_row][col_index] == '.':
                        roll += 1
                        comparison_row += 1
                    else:
                        break
                if roll > 0:
                    field[row_index + roll][col_index] = 'O'
                    field[row_index][col_index] = '.'
    return field


def spin_east(field):
    for row_index in range(len(field)):
        for col_index in range(len(field[row_index]) - 1, -1, -1):  # Iterate from right to left in each row
            if field[row_index][col_index] == 'O':
                roll = 0
                comparison_col = col_index + 1
                while comparison_col < len(field[row_index]):
                    if field[row_index][comparison_col] == '.':
                        roll += 1
                        comparison_col += 1
                    else:
                        break
                if roll > 0:
                    field[row_index][col_index + roll] = 'O'
                    field[row_index][col_index] = '.'
    return field



def spin_cycle(field):
    field = spin_north(field)
    #print_field(field, "North")
    field = spin_west(field)
    #print_field(field, "West")
    field = spin_south(field)
    #print_field(field, "South")
    field = spin_east(field)
    #print_field(field, "East")
    return field


def print_field(field, title):
    print(title)
    for row in field:
        print(row)


def hash_matrix(matrix):
    """ Create a hash for a given matrix """
    return hashlib.md5(''.join([''.join(row) for row in matrix]).encode()).hexdigest()


def detect_and_confirm_cycle(field, additional_cycles=3):
    # Initial cycle detection
    slow = field
    fast = spin_cycle([row[:] for row in field])  # Deep copy for independent spin

    while hash_matrix(slow) != hash_matrix(fast):
        slow = spin_cycle(slow)
        fast = spin_cycle(spin_cycle([row[:] for row in fast]))  # Two steps for fast

    # Cycle detected, now find the start of the cycle
    fast = field  # Reset fast to the start
    while hash_matrix(slow) != hash_matrix(fast):
        slow = spin_cycle(slow)
        fast = spin_cycle(fast)

    # Now find the length of the cycle
    cycle_length = 0
    initial_hash = hash_matrix(slow)
    while True:
        slow = spin_cycle(slow)
        cycle_length += 1
        if hash_matrix(slow) == initial_hash:
            break

    # Confirming the cycle by running additional cycles
    for _ in range(additional_cycles):
        slow = spin_cycle(slow)
        if hash_matrix(slow) != initial_hash:
            return -1, -1  # No confirmed cycle

    return cycle_length, initial_hash  # Confirmed cycle


field = []
with open ("input.txt", "r") as file:
    for line in file: 
        row = [x for x in line.strip()]
        field.append(row)

# field = spin_cycle(field)
# print("cycle 1:")
# for row in field: 
#     print(row)

# field = spin_cycle(field)
# print("cycle 2:")
# for row in field: 
#     print(row)

# field = spin_cycle(field)
# print("cycle 3:")
# for row in field: 
#     print(row)

# Detect and confirm the cycle
confirmed_cycle_length, confirmed_cycle_hash = detect_and_confirm_cycle(field)

# Proceed with the remaining iterations calculation and the rest of your code only if a cycle is confirmed
if confirmed_cycle_length > 0:
    # Calculate how many iterations remain after the cycles
    remaining_iterations = (1000000000 - confirmed_cycle_length * 3) % confirmed_cycle_length

    # Perform the remaining iterations
    for _ in range(remaining_iterations):
        field = spin_cycle(field)

# for i in range(1000000000):
#     field = spin_cycle(field)
#     #print(i)

# Calculate the result
field_length = len(field)
result = 0
for row in field:
    count = sum(item.count('O') for item in row)
    result += count * field_length
    field_length -= 1

print(result)