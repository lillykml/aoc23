sum = 0 # variable to keep track of the sum

numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

file = open('input.txt', 'r') # read all the lines from the file
for line in file:

    first = ""
    last = ""
    line = line.strip()

    #go over string and replace textual numbers with actual digits
    #update: sometimes the same char is used for multiple digits, append & prepend number
    for key, value in numbers.items():
        if key in line:
            line = line.replace(key, key + value + key)

    for char in line: # for each character in the line check if its numeric
        if char.isnumeric(): #track the first and the currently last 
            if (first == ""):  
                first = char
            else:
                last = char
    
    #Check if there was only 1 digit
    if last == "":
        last = first

    number = first + last # at the end of the line put the 2 characters together & convert them into an integer 
    sum += int(number) # add the number to the sum

print(sum) #print the sum