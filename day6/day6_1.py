import math
# Read file & the input / distance pairs
# I could compute all possible outcomes for every combination and count how many are above the record
# This wouldn't be very efficient
# I think I actually only need to find the minimum and maximum value to beat the distance
# And then take the difference to get the amount of ways 


def get_travelled_distance(button_time, race_time):
    speed = button_time * 1
    distance = (race_time-button_time) * speed # same as (rt*-bt) *bt
    return distance


def get_possibilities(race_time, max_distance):
    # use abc formula to get exact values for the current max_distance
    # Then we need to round up to the next integer
    # If x1 and x2 are integers we need to go to the next
    x1 = (-race_time + ((race_time**2 - 4*-1*-1*max_distance)**(1/2))) / (2*-1)
    x2 = (-race_time - ((race_time**2 - 4*-1*-1*max_distance)**(1/2))) / (2*-1)

    # Round to the NEXT integers
    x1 = math.ceil(mutate_int(x1))
    x2 = math.floor(mutate_int(x2))
    return (x2-x1+1)

def mutate_int(value):
    # Check if value is equivalent to an integer
    if value == int(value):
        return int(value) + 1
    return value


############# Main Part 1 #############
data_dict = {}
possibilities = 1
with open('input2.txt', 'r') as file:
    for line in file:
        (key, values) = line.split(":")
        values = [int(num) for num in values.strip().split()]
        data_dict[key] = values
    
    combinations = list(zip(data_dict['Time'], data_dict['Distance']))
    for combination in combinations:
        c = get_possibilities(combination[0], combination[1])
        print(c)
        possibilities *= c

print(possibilities)
