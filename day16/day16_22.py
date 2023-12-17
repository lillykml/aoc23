grid = []
beams = [{"location": (0,0), "direction": 0}]
max_energy = 0
starting_locations = []
directions = { #0 positive x, 1 negative  x, 2 positive y, 3 negative y
    0: (1, 0),
    1: (-1, 0),
    2: (0, -1),
    3: (0, 1)
}


def count_energized(grid):
    count = 0
    for row in grid:
        for cell in row:
            if cell["energized"]:
                count += 1
    return count
def reset_energized(grid):
    for row in grid:
        for cell in row:
            cell["energized"] = False
            cell["splitted"] = False


# Create an matrix of tile objects
with open("input.txt", "r") as file:
    for line in file:
        grid.append([{"tile": x, "energized": False, "splitted": False} for x in line.strip()])


# Create a list of all starting location / direction combinations
# Top row, direction down
for x in range(len(grid[0])):
    starting_locations.append({"location": (x, 0), "direction": 3})
# Left column, direction right
for y in range(len(grid)):
    starting_locations.append({"location": (0, y), "direction": 0})
# Right column, direction left
for y in range(len(grid)):
    starting_locations.append({"location": (len(grid[0]) - 1,y), "direction": 1})
# Bottom row, direction up
for x in range(len(grid[0])):
    starting_locations.append({"location": (x,len(grid) - 1), "direction": 2})


#Loop through all starting locations
while len(starting_locations) > 0:
    starting_tile = starting_locations.pop(0)
    beams = [starting_tile] # new beams array with the starting tile
    #print("Starting Tile: " + str(starting_tile["location"]) + " Direction " + str(starting_tile["direction"]))

    # Go over the beams 1 by 1 for every starting point
    while len(beams) > 0:
        beam = beams.pop(0)
        (x, y) = beam["location"]
        direction = beam["direction"]
        visited = set()
        #print("New Beam Starting location: (" + str(x) + "," + str(y) + ") Direction: " + str(direction))

        while 0 <= x < len(grid) and 0 <= y < len(grid[0]):
            current_tile = grid[y][x]
            grid[y][x]["energized"] = True
            visited.add((x, y, direction))
            
            if current_tile["tile"] == '|' and (direction == 0 or direction == 1):
                if not current_tile["splitted"]:
                    beams.append({"location": (x, y), "direction": 2}) # we always append the beam going up
                    #print("Appended new beam starting at (" + str(next_tile_location[0]) + "," + str(next_tile_location[1]) + ")")
                    current_tile["splitted"] = True
                direction = 3
            elif current_tile["tile"] == '-' and (direction == 2 or direction == 3):
                if not current_tile["splitted"]:
                    beams.append({"location": (x, y), "direction": 1}) # we always append the beam going left
                    #print("Appended new beam starting at (" + str(next_tile_location[0]) + "," + str(next_tile_location[1]) + ")")
                    current_tile["splitted"] = True
                direction = 0
            elif current_tile["tile"] == '/' and direction == 0:
                direction = 2
            elif current_tile["tile"] == '/' and direction == 1:
                direction = 3
            elif current_tile["tile"] == '/' and direction == 2:
                direction = 0
            elif current_tile["tile"] == '/' and direction == 3:
                direction = 1
            elif current_tile["tile"] == "\\" and direction == 0:
                direction = 3
            elif current_tile["tile"] == '\\' and direction == 1:
                direction = 2
            elif current_tile["tile"] == '\\' and direction == 2:
                direction = 1
            elif current_tile["tile"] == '\\' and direction == 3:
                direction = 0
            

            dx, dy = directions[direction]
            if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]):
                current_tile = grid[y + dy][x + dx]
                x+=dx
                y+=dy
            #print("Next Tile: " + next_tile["tile"] + " Next Tile Location (" + str(next_tile_location[0]) + "," + str(next_tile_location[1]) + ")")
            else:
                break

            if (x, y, direction) in visited:
                break
            
    energy_level = count_energized(grid)
    if energy_level > max_energy: max_energy = energy_level
    reset_energized(grid)

print(max_energy)