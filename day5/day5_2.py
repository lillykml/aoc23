# So basically just tracking all the seeds consumes to much memory
# I don't need to store all the seeds but only need to keep track of the lowest location

# Read the input into a dictionnary with the keys: seeds and the different maps
# The values of the dictionnary should be and array of arrays with the mappings sorted by the source range (medium number)
def parse_and_sort_data(lines):
    data_dict = {}
    current_key = None
    current_values = []

    for line in lines:
        if 'seeds' in line:
            (key, value) = line.split(':')
            values = [int(num) for num in value.strip().split()]
            data_dict[key] = values

        # Check if line is a key (contains ':')
        elif ':' in line:
            # If there's a previous key, save its data
            if current_key:
                # Sort based on the middle number
                current_values.sort(key=lambda x: x[1])  
            data_dict[current_key] = current_values
            # Start new key
            current_key = line.split(':')[0].strip()  # Get key name
            current_values = []
        elif line.strip():  # If line is not empty
            # Convert line to list of integers and append to current values
            current_values.append(list(map(int, line.split())))
    
    # Don't forget to add the last key-value pair
    if current_key:
        current_values.sort(key=lambda x: x[1])  # Sort based on middle number
        data_dict[current_key] = current_values

    return data_dict


#Helper function to find the correct ratio
def convert(mapping, value, parsed_data):
    for ratio in parsed_data[mapping]:
        if ratio[1] <= value <= (ratio[1] + ratio[2]-1):
            return (value - ratio[1]+ ratio[0])
    return value


################# Main Part 2 ######################
with open("input.txt", 'r') as file:
    file_content = file.readlines()

parsed_data = parse_and_sort_data(file_content)
min_location = None

# Now I iterate over the seed ranges
# For each seed in the range I calculate the min_location and only keep track if it is smaller than the min location
# So I won't store anything in a dict anymore
#data_dict[key] = getSeeds(values) # Part 2 -> To memory heavy
seed_ranges = parsed_data['seeds']
for i in range(0, len(seed_ranges), 2):
    for j in range(seed_ranges[i],seed_ranges[i]+seed_ranges[i+1]):
        soil = convert('seed-to-soil map', j, parsed_data)
        fertilizer = convert('soil-to-fertilizer map', soil, parsed_data)
        water = convert('fertilizer-to-water map', fertilizer, parsed_data)
        light = convert('water-to-light map', water, parsed_data)
        temperature = convert('light-to-temperature map', light, parsed_data)
        humidity = convert('temperature-to-humidity map',  temperature, parsed_data)
        location = convert('humidity-to-location map', humidity, parsed_data)

        # keep track of the lowest location number
        if not min_location or location < min_location:
            min_location = location

print(min_location)
