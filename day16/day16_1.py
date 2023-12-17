# Store the grid in a matrix
# I could also do a matrix that contains objects to track the thing being energized
# Have a list of beams and their starting position
# Write a function that moves the beam of light 
# If it splits I append this specific beam and use it once my current beam is done
# While it moves I change the energized property of the matrix items
# I stop as soon as the moving indexes are out of the grid

grid = []
beams = [{"location": (0,0), "direction": 0}]
directions = { #0 positive x, 1 negative  x, 2 positive y, 3 negative y
    0: (1, 0),
    1: (-1, 0),
    2: (0, -1),
    3: (0, 1)
}

with open("input.txt", "r") as file:
    for line in file:
        grid.append([{"tile": x, "energized": False, "splitted": False} for x in line.strip()])


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


def count_energized(grid):
    count = 0
    for row in grid:
        for cell in row:
            if cell["energized"]:
                count += 1
    return count

def print_grid(grid):
    for row in grid:
        for cell in row:
            if cell["energized"]:
                print("#", end="")
            else:
                print(".", end="")
        print()

print(count_energized(grid))
#print_grid(grid)
