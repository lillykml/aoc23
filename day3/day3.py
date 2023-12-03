import re


# We only need to keep track of 3 lines & not the entire file
before = ""
current = ""
after = ""
sum = 0

# Helper function to extract the start and stop index (last digit ) of the next number
def extractNumberIndex(line, newStart):
    start_index = 0
    end_index = -1
    match = re.search(r'\d+', line[newStart:])
    if match:
        start_index = match.start()+newStart
        end_index = match.end()-1+newStart
    return (start_index, end_index)


# Helper function to extract the number 
def extractNumber(line, start, stop):
    return int(line[start:stop+1])

# Helper function to check if a string contains a symbol
def containsSymbol(text):
    return re.search(r'[\$\*\+\#\-\=\@\/\%\?\!\&]', text)

# Helper function to get substrings that need to be checked 
def getCheckStrings(before, current, after, start, stop):

    toCheck = []
    maxIndex = len(current) - 1
    startIndex = start - 1 if start > 0 else start
    stopIndex = stop + 1 if stop < maxIndex else maxIndex

    toCheck.append(current[startIndex])
    toCheck.append(current[stopIndex])
    if before !="":
        toCheck.append(before[startIndex:stopIndex+1])
    if after !="":
        toCheck.append(after[startIndex:stopIndex+1])
    return toCheck


def checkLine(before, current, after):
    index = 0
    sum = 0

    while index < len(current):
        (start, stop) = extractNumberIndex(current, index)
        if stop == -1:
            index = len(current)
        else:
            toCheck = getCheckStrings(before, current, after, start, stop)
            for s in toCheck:
                # if there is a symbol stop & add the number
                # continue 1 to the right or in the next row
                if containsSymbol(s):
                    number = extractNumber(current, start, stop)
                    sum += number
                    break
            index = stop+1
            
    return sum
    


# Loop over the file 
file = open('input.txt', 'r')

for line in file:
    line = line.strip()

    index = 0
    before = current
    current = after 
    after = line

    if current != "":
        sum += checkLine(before, current, after)

# Special case for the last row 
before = current
current = after
after = ""
sum += checkLine(before, current, after)

print(sum)
