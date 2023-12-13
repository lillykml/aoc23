# Have a dict that contains the pipe symbol and somehow how it is connected to other pipes
# Maybe a dict with the keys left, right, up & down
pipe_dict = {
    "|":  {"north": 1, "south": 1, "east": 0, "west": 0},
    "-":  {"north": 0, "south": 0, "east": 1, "west": 1},
    "L":  {"north": 1, "south": 0, "east": 1, "west": 0},
    "J":  {"north": 1, "south": 0, "east": 0, "west": 1},
    "7":  {"north": 0, "south": 1, "east": 0, "west": 1},
    "F":  {"north": 0, "south": 1, "east": 1, "west": 0},
    ".":  { "north": 0, "south": 0, "east": 0, "west": 0}
}

opposites = {
    "north": "south",
    "south": "north",
    "east": "west",
    "west": "east"
}

# Helper function to find out the symbol for s
def find_s_symbol(maze, s_coordinates):
    (x, y) = s_coordinates
    symbol = [0,0,0,0]
    north= maze[x-1][y] if x != 0 else "."
    south = maze[x+1][y] if x != len(maze)-1 else "."
    east = maze[x][y+1] if y != len(maze[0])-1 else "."
    west = maze[x][y-1] if y != 0 else "."

    if pipe_dict[north]['south'] == 1: symbol[0] = 1
    if pipe_dict[south]['north'] == 1: symbol[1] = 1
    if pipe_dict[east]['west'] == 1: symbol[2] = 1
    if pipe_dict[west]['east'] == 1: symbol[3] = 1

    if symbol[0] == 1 and symbol[1] == 1: return "|"
    if symbol[0] == 1 and symbol[2] == 1: return"L"
    if symbol[0] == 1 and symbol[3] == 1: return"J"
    if symbol[1] == 1 and symbol[2] == 1: return"F"
    if symbol[1] == 1 and symbol[3] == 1: return"7"
    if symbol[2] == 1 and symbol[3] == 1: return"-"


# Get incoming directions of an element
def get_outgoing_directions(element):
    directions = []
    for key, value in pipe_dict[element].items():
        if value == 1:
            directions.append(key)
    return directions

# Helper function to determine the new_position and the new_prev_direction
def find_next_element(current_coords, current_element, incoming_direction):
    # Define the connectivity dictionary
    connectivity = {
        "|": {"north": "south", "south": "north"},
        "-": {"east": "west", "west": "east"},
        "L": {"north": "east", "east": "north"},
        "J": {"north": "west", "west": "north"},
        "7": {"south": "west", "west": "south"},
        "F": {"south": "east", "east": "south"}
    }

    # Determine the outgoing direction based on the incoming direction and current element
    outgoing_direction = connectivity[current_element].get(incoming_direction)

    # Calculate new coordinates based on the outgoing direction
    if outgoing_direction == "north":
        new_coords = [current_coords[0] - 1, current_coords[1]]
    elif outgoing_direction == "south":
        new_coords = [current_coords[0] + 1, current_coords[1]]
    elif outgoing_direction == "east":
        new_coords = [current_coords[0], current_coords[1] + 1]
    elif outgoing_direction == "west":
        new_coords = [current_coords[0], current_coords[1] - 1]
    
    incoming_direction_next_step = {"north": "south", "south": "north", "east": "west", "west": "east"}[outgoing_direction]
    return new_coords, incoming_direction_next_step



# Helper function to find the next 2 elements for every direction
def find_next_elements(maze, coordinates, directions):
    new_coordinates = []
    new_directions = []

    new_cords_a, new_direction_a = find_next_element(coordinates[0], maze[coordinates[0][0]][coordinates[0][1]], directions[0])
    new_cords_b, new_direction_b = find_next_element(coordinates[1], maze[coordinates[1][0]][coordinates[1][1]], directions[1])

    new_coordinates.append(new_cords_a)
    new_coordinates.append(new_cords_b)
    new_directions.append(new_direction_a)
    new_directions.append(new_direction_b)

    return new_coordinates, new_directions


# Slightly different function for the starting point
def first_step(element, coordinates):
    new_coordinates = []
    new_directions = []
    directions = get_outgoing_directions(element)

    new_cords_a, new_direction_a = (find_next_element(coordinates, element, directions[0]))
    new_cords_b, new_direction_b = (find_next_element(coordinates, element, directions[1]))

    new_coordinates.append(new_cords_a)
    new_coordinates.append(new_cords_b)
    new_directions.append(new_direction_a)
    new_directions.append(new_direction_b)

    return new_coordinates, new_directions


# Store the maze in a array of arrays
maze=[]
with open("input.txt", "r") as file: 
    for line in file:
        maze.append([x for x in line.strip()])

# Find the coordinates and Symbol for S, our starting point
coordinates = [[i, j] for i, row in enumerate(maze) for j, element in enumerate(row) if element == "S"]
s = find_s_symbol(maze, coordinates[0])

# We continoue searching for our element as long as we didn't arrive at the same point
loop = False
incoming_directions = None
next_elements = []
steps=0

while not loop:
    if not incoming_directions:
        coordinates, incoming_directions = first_step(s, coordinates[0])
    else:
        coordinates, incoming_directions = find_next_elements(maze, coordinates, incoming_directions)
    if coordinates[0] == coordinates[1]: loop = True
    steps+=1

print(steps)
    

