# Read input file into array of arrays (?)
# Expand universe
# Assign each # a number
# Store each # in a dict with its distances
# somehow calculate the distance based on array location


# Helper function to expan the universe
def expand_universe(universe):
    expansion_indices = []
    i = 0
    while i < len(universe[0]):
        expand = True
        for j in range(len(universe)):
            if universe[j][i] != '.': expand = False
        if expand: expansion_indices.append(i)
        i+=1
    
    shift = 0
    for row in universe:
        for expansion in expansion_indices:
            row.insert(expansion + shift, '.')
            shift+=1
        shift = 0
    
    return universe


# Helper function to store all galaxies and their location in a dict
def store_galaxies(universe):
    galaxy_dict = {}
    total_distances = 0
    for i in range(len(universe)):
        for j in range(len(universe[i])):
            if isinstance(universe[i][j], int):
                galaxy_dict[universe[i][j]] = {
                    "location": (i+1, j+1),
                    "distances": []
                }
                for key in galaxy_dict.keys():
                    distance = calculate_distance(galaxy_dict[universe[i][j]]["location"], galaxy_dict[key]["location"])
                    galaxy_dict[universe[i][j]]["distances"].append(distance)
                    total_distances += distance

    return (galaxy_dict, total_distances)

# Helper function to calculate distance between galaxies (input are a tuple of the coordinates)
def calculate_distance(galaxy_a, galaxy_b):
    base_distance = abs(galaxy_a[0] - galaxy_b[0]) + abs(galaxy_a[1] - galaxy_b[1])
    return base_distance


############ Main Part 1 ###############
universe = []
galaxy_counter = 0

with open("input.txt", "r") as file: 
    for line in file:
        no_galaxies = True
        universe.append([x for x in line.strip()])
        for i in range(len(universe[-1])):
            if universe[-1][i] != '.': 
                no_galaxies = False
                galaxy_counter += 1
                universe[-1][i] = galaxy_counter
        if no_galaxies: universe.append([x for x in line.strip()])

universe = expand_universe(universe)
universe_dict, total_distances = store_galaxies(universe)

print(total_distances)