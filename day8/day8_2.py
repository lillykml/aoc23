import math


def lcm_of_two_numbers(a, b):
    return abs(a*b) // math.gcd(a, b)

def lcm_of_list(numbers):
    lcm = numbers[0]
    for n in numbers[1:]:
        lcm = lcm_of_two_numbers(lcm, n)
    return lcm

instructions = ""
nodes = {}
current_nodes = []
step_list=[]

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
            if key.strip().endswith('A'): current_nodes.append(key.strip())
        elif not line.startswith('\n'):
            instructions = line.strip()

# Approach 1: Brute force does not scale
# while not arrived:
#     for instruction in instructions:
#         continue_status = False
#         for index, node in enumerate(current_nodes):
#             current_nodes[index] = nodes[node]['left'] if instruction == 'L' else nodes[node]['right']
#             if not current_nodes[index].endswith('Z'):
#                 continue_status = True
        
#         arrived = not continue_status
#         steps += 1

# Approach 2: Use least common multiple approach
for node in current_nodes:
    arrived = False
    current_node = node
    steps = 0

    while not arrived:
        for instruction in instructions:
            current_node = nodes[current_node]['left'] if instruction == 'L' else nodes[current_node]['right']
            if current_node.endswith('Z'): arrived = True 
            steps += 1

    step_list.append(steps)

print(lcm_of_list(step_list))