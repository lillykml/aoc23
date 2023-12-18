def print_grid(grid):
    for row in grid:
        print(row)

def sort_nodes(nodes):
    nodes.sort(key=lambda node: (node['visited'], node['cost']))



grid = []
nodes = []
neighbours = {
    "L": (-1, 0),
    "R": (1,0),
    "U": (0,-1),
    "D": (0,1)
}

opposites = {
    "L": "R",
    "R": "L",
    "U": "D",
    "D": "U"
}

with open("test.txt", "r") as file:
    for line in file:
        grid.append([int(x) for x in line.strip()])


# Initialize node matrix for updating costs
node_matrix = [[None for _ in range(len(grid[0]))] for _ in range(len(grid))]

for i in range(len(grid)):
    for j in range(len(grid[0])):
        node = {
            "row": i,
            "col": j,
            "visited": False,
            "cost": float('inf'),
            "directions": []
        }
        nodes.append(node)
        # Store the node in the matrix at its corresponding location
        node_matrix[i][j] = node

# Start from the top left corner
nodes[0]["cost"] = 0


while len(nodes) > 0:
    sort_nodes(nodes)
    current_node = nodes.pop(0)
    #print(current_node)
    current_node["visited"] = True
    row = current_node["row"]
    col = current_node["col"]
    current_node_cost = current_node["cost"]
    current_node_directions = current_node["directions"]

    for key, neighbour in neighbours.items():
        dr,dc = neighbour
        if 0 <= row+dr < len(grid) and 0 <= col+dc < len(grid[0]):
            neighbour_field_cost = grid[row+dr][col+dc]
            current_neighbour_cost = node_matrix[row+dr][col+dc]["cost"]

            if (len(current_node_directions) < 3 or current_node_directions[-3:] != [key]*3):
                if (len(current_node_directions) == 0 or current_node_directions[-1] != opposites[key]):
                    if current_node_cost + neighbour_field_cost <= current_neighbour_cost:
                        node_matrix[row+dr][col+dc]["cost"] = current_node_cost + neighbour_field_cost
                        node_matrix[row+dr][col+dc]["directions"] = current_node["directions"].copy()
                        node_matrix[row+dr][col+dc]["directions"].append(key) 

print(node_matrix[-1][-1])


# Store x & y location, cost to reach this point
# Check for points left & right with what total cost they can be reached based on this costs
# if it is less than the current costs update it
# mark each origin point that we checked as done
# stop once we checked all points

