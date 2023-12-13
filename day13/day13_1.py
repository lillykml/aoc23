# Read in all patterns
# Compare lines & find 2 lines after each other that match 
# Check if the lines above and below also match (basically only need to check the top/ bottom most line in the pattern)
# If yes all top rows 
# Do the same for vertical patterns comparing columns

# Function to get a column from a matrix
def get_column(matrix, column_index):
    return [row[column_index] for row in matrix]


def check_other_columns(matrix, mirror_index):
    num_cols = len(matrix[0])
    offset_left = 1
    offset_right = 2

    while mirror_index - offset_left >= 0 and mirror_index + offset_right < num_cols:
        left_col = mirror_index - offset_left
        right_col = mirror_index + offset_right
        if get_column(matrix, left_col) != get_column(matrix, right_col):
            return False
        offset_left += 1
        offset_right += 1
    return True


def check_other_rows(matrix, mirror_index):
    num_rows = len(matrix)
    offset_top = 1
    offset_bottom = 2

    while mirror_index - offset_top >= 0 and mirror_index + offset_bottom < num_rows:
        upper_row = mirror_index - offset_top
        lower_row = mirror_index + offset_bottom
        if matrix[upper_row] != matrix[lower_row]:
            return False
        offset_top += 1
        offset_bottom += 1
    return True

patterns = []
with open("input.txt", "r") as file: 
    pattern = []
    for line in file:
        content = [x for x in line.strip()]
        if len(content) > 0:
            pattern.append(content)
        else:
            patterns.append(pattern)
            pattern = []
    patterns.append(pattern)

sum = 0
for pattern in patterns:
    # compare rows & stores the index after which the mirroring occurs
    row_pattern = 0
    col_pattern = 0
    for i in range(len(pattern)-1):
        if pattern[i] == pattern[i+1]:
            if check_other_rows(pattern, i):
                row_pattern = i
                sum+= ((i+1)*100)

    # compare columns & stores the index after which the mirroring occurs
    for j in range(len(pattern[0])-1):
        if get_column(pattern, j) == get_column(pattern, j+1):
            if check_other_columns(pattern, j):
                col_pattern = j
                sum+= (j+1)

print(sum)