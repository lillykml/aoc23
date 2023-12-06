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


# So I start with the first seed range 
# I check wether many value of my seed range falls into the first mapping
# If yes I create a new range based on that mapping for the values falling into that, and keep going until my seed range is empty
# If I don't find a match I use my initial range
# Expects and array of array of tuples
def get_mapped_ranges(input_ranges, mapping, data_dict):
    mappings = []
    new_input_ranges = list(input_ranges)  # Copy the input ranges to a new list for further processing

    while new_input_ranges:
        range = new_input_ranges.pop()
        #print("Processed Range: " + str(range))
        input_start, input_length = range
        input_end = input_start + input_length - 1
        range_processed = False

        for map_entry in data_dict[mapping]:
            dest_start, source_start, map_length = map_entry
            source_end = source_start + map_length - 1
            #print("Mapping" + str(dest_start) + " " + str(source_start) + " " + str(map_length) + " " + str(source_end))

            if source_start <= input_start <= source_end:
                # Calculate the intersection
                intersect_start = max(input_start, source_start)
                intersect_end = min(input_end, source_end)

                # Apply the mapping to the intersecting range
                offset = dest_start - source_start
                mapped_start = intersect_start + offset
                intersect_length = intersect_end - intersect_start + 1

                #print("Appends: " + str(mapped_start) + " " + str(intersect_length))
                mappings.append((mapped_start, intersect_length))
                range_processed = True

                # Update remaining parts of the input range
                if input_start < intersect_start:
                    new_input_ranges.append((input_start, intersect_start - input_start))
                if input_end > intersect_end:
                    new_input_ranges.append((intersect_end + 1, input_end - intersect_end))
                break

        if not range_processed:
            # If no mapping was applied, add the range as-is to the mappings
            mappings.append(range)

    return mappings     

################# Main Part 2 ######################


# I keep doing that through all my mappings
# In the end I have a bunch of ranges and just need to find the minimum value
with open("input.txt", 'r') as file:
    file_content = file.readlines()

    # I preprocess the data in the same way (loading all the mappings)
    parsed_data = parse_and_sort_data(file_content)
    min_location = None

    # I then don't go value by value but range by range
    seed_ranges = parsed_data['seeds']
    map_key = ['seed-to-soil map', 'soil-to-fertilizer map', 'fertilizer-to-water map', 'water-to-light map', 'light-to-temperature map', 'temperature-to-humidity map', 'humidity-to-location map']

    for i in range(0, len(seed_ranges), 2):
        mappings = [(seed_ranges[i], seed_ranges[i+1])]
        for key in map_key:
            mappings = get_mapped_ranges(mappings, key, parsed_data)


        # keep track of the lowest location number
        current_min_location = min(mappings, key=lambda x: x[0])[0]
        if not min_location or current_min_location < min_location:
            min_location = current_min_location

print(min_location)

