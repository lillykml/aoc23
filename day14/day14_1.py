# Read the input line by line into a matrix
# For each line search for the round rocks
# For each round rock check if you can move it to rows before (keep checking until you reach another rock or #)
# switch the . and the o
# Keep track of the rocks per row and calculate result in the end 

field = []
field_length = 0
with open ("input.txt", "r") as file:
    for line in file: 
        row = [x for x in line.strip()]
        if field_length > 0:
            for i in range(len(row)):
                if row[i] ==  'O':
                    roll = 0
                    comparison_row = field_length-1
                    while comparison_row >= 0:
                        if field[comparison_row][i] == '.': 
                            roll+=1
                            comparison_row-=1
                        else:
                            break
                    if roll > 0:
                        field[field_length-roll][i] = 'O'
                        row[i] = '.'
                i+=1
        field.append(row)
        field_length+=1

result = 0
for row in field:
    count = sum(item.count('O') for item in row)
    result += count * field_length
    field_length-=1

print(result)