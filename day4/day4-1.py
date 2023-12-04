# read file line by line 
# store winning numbers in a list
# loop over my own numbers and count matches 
# do the calculation
# print then number

sum = 0


with open('input.txt', 'r') as f:
    for line in f:
        matches = 0
        (card, numbers) = line.split(":")
        (winners, own) = numbers.split("|")
        winningNumbers = winners.strip().split()
        ownNumbers = own.strip().split()
        
        for myNumber in ownNumbers:
            for winner in winningNumbers:
                if int(myNumber) == int(winner): matches+=1
        
        if matches > 0:
            sum += 2**(matches-1)


print(sum)