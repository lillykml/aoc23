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


# Afterwards Create another dictionnary with the initial seeds 
# the value is another dictionnary with the converted numbers 
# Soil, fertilizer, water, light, temperature, humidity, location 
def create_seed_dict(data_dict):
    seed_dict = {}
    for seed in data_dict['seeds']:
        seed_dict[seed] = {
            'soil': 0,
            'fertilizer': 0,
            'water': 0,
            'light': 0,
            'temperature': 0,
            'humidity': 0,
            'location ': 0
        }
    return seed_dict


#Helper function to find the correct ratio
def convert(mapping, value, parsed_data):
    for ratio in parsed_data[mapping]:
        if ratio[1] <= value <= (ratio[1] + ratio[2]-1):
            return (value - ratio[1]+ ratio[0])
    return value





################# Main Part 1 ######################
with open("input.txt", 'r') as file:
    file_content = file.readlines()

parsed_data = parse_and_sort_data(file_content)
seed_dict = create_seed_dict(parsed_data)

# Calculate conversion for each seed
min_location = None

for seed in seed_dict.keys():
    seed_dict[seed]['soil'] = convert('seed-to-soil map', seed, parsed_data)
    seed_dict[seed]['fertilizer'] = convert('soil-to-fertilizer map', seed_dict[seed]['soil'], parsed_data)
    seed_dict[seed]['water'] = convert('fertilizer-to-water map', seed_dict[seed]['fertilizer'], parsed_data)
    seed_dict[seed]['light'] = convert('water-to-light map', seed_dict[seed]['water'], parsed_data)
    seed_dict[seed]['temperature'] = convert('light-to-temperature map', seed_dict[seed]['light'], parsed_data)
    seed_dict[seed]['humidity'] = convert('temperature-to-humidity map',  seed_dict[seed]['temperature'], parsed_data)
    seed_dict[seed]['location'] = convert('humidity-to-location map',  seed_dict[seed]['humidity'], parsed_data)

    # keep track of the lowest location number
    if min_location:
        if seed_dict[seed]['location'] < min_location:
            min_location = seed_dict[seed]['location']
    else:
        min_location = seed_dict[seed]['location']

#print(parsed_data)
#print(seed_dict)
print(min_location)






