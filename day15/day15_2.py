# Running the first algorithm on the label
# This yields a number between 0 and 255 = box
# if dash, go to the box and remove the lens with the label from the box and move all lenses forward
# if = take the lense with that focal length from the outside, label it 


def hash_sequence(sequence):
    current_value = 0
    for char in sequence:
        current_value += ord(char)
        current_value *= 17
        current_value = current_value % 256
    return current_value

def calculate_power(box_table):
    result = 0
    for box_index, box in enumerate(box_table):
        for item_index, item in enumerate(box):
            result += (box_index+1)*(item_index+1)*int(item.split()[1])
    return result




boxes = [[] for _ in range(256)]
focal_lenses = [i+1 for i in range(9)]
sum = 0

with open ("input.txt", "r") as file:
    for line in file:
        sequences = line.strip().split(",")
        for sequence in sequences:
            if '=' in sequence:
                (label, value) = sequence.split('=')
                equals = True
            else: 
                (label, value) = sequence.split('-')
                equals = False

            box_number = hash_sequence(label)

            if not equals: #it's a dash
                boxes[box_number] = [item for item in boxes[box_number] if label not in item]
            else: #it's a =
                exists = False
                for index, item in enumerate(boxes[box_number]):
                    if label in item:
                        exists = True
                        boxes[box_number][index] = ' '.join([label, value])  # item[1] represents the value associated with the label in the item
                if not exists:
                    boxes[box_number].append(' '.join([label, value]))


print(calculate_power(boxes))
