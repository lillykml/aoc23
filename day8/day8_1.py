# Read instructions
# Read in all nodes and store them in a dict
# do a while not at goal loop and repeat the instruction set
# increment a counter

instructions = ""
nodes = {}
current_node = "AAA"
end_node = "ZZZ"
arrived = False
steps = 0

with open("input.txt", "r") as file:
    for line in file:
        if '(' in line:
            (key, value) = line.split('=')
            left = value[2:5]
            right = value[7:10]
            nodes[key.strip()] = {
                "left": left,
                "right": right
            }
        elif not line.startswith('\n'):
            instructions = line.strip()


while not arrived:
    for instruction in instructions:
        current_node = nodes[current_node]['left'] if instruction == 'L' else nodes[current_node]['right']
        arrived = True if current_node == end_node else False
        steps += 1

print(steps)