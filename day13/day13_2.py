def rows_differ_by_one(row1, row2):
    difference_count = 0
    for i in range(len(row1)):
        if row1[i] != row2[i]:
            difference_count += 1
    return difference_count == 1


# Function to get a column from a matrix
def get_column(matrix, column_index):
    return [row[column_index] for row in matrix]


def get_difference_index(row1, row2):
    for i in range(len(row1)):
        if row1[i] != row2[i]:
            return i


def check_other_columns(matrix, mirror_index, smudge):
    num_cols = len(matrix[0])
    offset_left = 1
    offset_right = 2

    while mirror_index - offset_left >= 0 and mirror_index + offset_right < num_cols:
        left_col = mirror_index - offset_left
        right_col = mirror_index + offset_right


        if get_column(matrix, left_col) == get_column(matrix, right_col) or (rows_differ_by_one(get_column(matrix, left_col), get_column(matrix, right_col)) and not smudge):
            offset_left += 1
            offset_right += 1
            if get_column(matrix, left_col) != get_column(matrix, right_col): smudge = True
        else: 
            return (False, False)

    return (True, smudge)


def check_other_rows(matrix, mirror_index, smudge):
    num_rows = len(matrix)
    offset_top = 1
    offset_bottom = 2

    while mirror_index - offset_top >= 0 and mirror_index + offset_bottom < num_rows:
        upper_row = mirror_index - offset_top
        lower_row = mirror_index + offset_bottom
        if matrix[upper_row] == matrix[lower_row] or (rows_differ_by_one(matrix[upper_row], matrix[lower_row]) and not smudge):
            offset_top += 1
            offset_bottom += 1
            if matrix[upper_row] != matrix[lower_row]: smudge = True

        else:
            return (False, False)
    return (True, smudge)

patterns = []
with open("test.txt", "r") as file: 
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

    smudge = False # At the beginning of each pattern we have this "joker"
    # compare rows & stores the index after which the mirroring occurs
    for i in range(len(pattern)-1):
        differ_by_one = rows_differ_by_one(pattern[i],pattern[i+1])
        if pattern[i] == pattern[i+1] or (differ_by_one and not smudge):
            if differ_by_one:
                smudge = True
                pattern[i][get_difference_index(pattern[i], pattern[i+1])] = '.' if pattern[i][get_difference_index(pattern[i], pattern[i+1])] == '#' else '#'
            status, smudge = check_other_rows(pattern, i, smudge)
            if status:
                sum+= ((i+1)*100)

    # compare columns & stores the index after which the mirroring occurs
    for j in range(len(pattern[0])-1):
        differ_by_one = rows_differ_by_one(get_column(pattern, j), get_column(pattern, j+1))
        if get_column(pattern, j) == get_column(pattern, j+1) or (differ_by_one and not smudge):
            if differ_by_one:
                smudge = True
                pattern[get_difference_index(get_column(pattern, j), get_column(pattern, j+1))][j] = '.' if pattern[get_difference_index(get_column(pattern, j), get_column(pattern, j+1))][j] == '#' else '#'

            status, smudge = check_other_columns(pattern, j, smudge)
            if status:
                sum+= (j+1)

    print(sum)


# TO DO: Somehow update the smudged pixel 