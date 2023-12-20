import re

# Read in input and store the rules in a dict
# Store elements in a list of lists with 4 element 
# Loop through all elements 
# Have a function that takes the element and the rule and then returns the location
# If the location is A add up 
# If the location is R next element
# Otherwise go again 

def get_next_element(rule_list, elements):
    indexes = ["x", "m", "a", "s"]
    for rule in rule_list:
        if "<" not in rule and ">" not in rule:
            return rule
        else:
            for i in range(len(elements)):
                if indexes[i] == rule[0]:
                    value = int(rule[2:rule.index(":")])
                    result = rule[rule.index(":")+1:]
                    if rule[1] == ">" and elements[i] > value: return result
                    if rule[1] == "<" and elements[i] < value: return result

rules = {}
elements = []
sum_accepted = 0
with open("input.txt", "r") as file:
    first_part = True
    for line in file:
        if line == "\n": first_part = False
        elif first_part: #Extract rules px: [condition, condition]
            (key, rule_set) = line.strip().split("{")
            rule_set = rule_set[:-1]
            rules[key] = [rule for rule in rule_set.split(",")]
        else: #Extract numbers of all elements [x, m, a, s]
            numbers = re.findall(r'\d+', line)
            numbers = [int(num) for num in numbers]
            elements.append(numbers)

while len(elements) > 0:
    element = elements.pop(0)
    rejected = False
    accepted = False
    next_rule = "in"
    while not rejected and not accepted:
        rule_list = rules[next_rule]
        next_rule = get_next_element(rule_list, element)
        rejected = next_rule == "R"
        accepted = next_rule == "A"
    if accepted: 
        sum_accepted+= sum(element)

print(sum_accepted)