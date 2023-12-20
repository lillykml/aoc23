# Try implementing a ray-casting algorithm

def is_inside_loop(matrix, row, col):
    intersections = 0
    for y in range(col, len(matrix[0])):
        if matrix[row][y] == 1:
            intersections += 1
    return intersections % 2 != 0

def count_elements_in_loop(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 1 and is_inside_loop(matrix, i, j):
                count += 1
    return count



with open("test.txt", "r") as file:
    for line in file:
        (direction, length, color) = line.strip().split()
        
        # Somehow dynamically generate my matrix (I don't know the dimensions beforehand)
        # I start from a point and then go left and right
        # I could also track up and down 
        # Count my track and all elements in the loop 




#print(count_elements_in_loop(maze))