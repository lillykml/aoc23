def find_differences(number_list):
    differences = []
    for i in range(len(number_list)-1):
        differences.append(number_list[i]-number_list[i+1])
    return differences


sum_next_values = 0
with open('input.txt', 'r') as file:
    for line in file:
        numbers = [int(x) for x in line.split()]
        all_zero = False
        cache = [numbers[0]]
        while not all_zero:
            numbers = find_differences(numbers)
            cache.append(numbers[0])
            all_zero = all(x == 0 for x in numbers)
        #print(cache)
        sum_next_values+= sum(cache)
        
print(sum_next_values)