from math import comb


# Helper function to find combinations
# First scan for incomplete combinations that need to be completed either with # or . next to it
# Create a list of all unknown sequences that can be populated (important )
# Input this list of unknown sequences and a list of the available combinations into a function
# calculate the possibilities

def count_working_spring_arrangements(unknown_segments, working_springs):
    """
    Count the number of ways to fit working springs within segments of unknown positions.

    Parameters:
    unknown_segments (list of int): Lengths of segments with unknown spring conditions.
    working_springs (list of int): Lengths of working springs to be fitted within each segment.

    Returns:
    int: Total number of valid arrangements.
    """
    def count_in_segment(unknown_length, spring_length):
        """
        Count the number of ways to fit a spring of given length within a segment of given length.
        """
        # The number of positions the spring can start in
        return unknown_length - spring_length + 1

    total_arrangements = 1

    # Iterate over each segment
    for segment_length, spring_length in zip(unknown_segments, working_springs):
        total_arrangements *= count_in_segment(segment_length, spring_length)

    return total_arrangements

# Example: Two segments of 2 unknowns each, with working springs of length 1 to be fitted in each
unknown_segments = [7] # Representing the "..??" and "..??"
working_springs = [2, 1] # Two working springs of length 1 each
result = count_working_spring_arrangements(unknown_segments, working_springs)
print(result)



########## Main Part #################
# Read in data
data = []
combinations = 0
with open("test.txt", "r") as file:
    for line in file:
        (row, conditions) = line.split()
        conditions = conditions.strip().split(',')
        data.append((row, conditions))
        # Use a function that returns the number of combinations for the row / pattern combination
        # Add the results to the combinations





#total_arrangements = sum(count_arrangements(row[0], row[1]) for row in rows)
#total_arrangements

