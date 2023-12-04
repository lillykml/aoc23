######## Part 1 ##########
# loop over my own numbers and count matches 
def getMatches(winningNumbers, ownNumbers):
    matches = 0
    for myNumber in ownNumbers:
        for winner in winningNumbers:
            if int(myNumber) == int(winner): matches+=1
    return matches

# calculate the points
def getPoints(matches):
    return 2**(matches-1) if matches > 0 else 0
    

########## Main Part ##########
#sum = 0
id = 1
cards = {}

# read file line by line 
with open('input.txt', 'r') as f:
    for line in f:
        (card, numbers) = line.split(":")
        (winners, own) = numbers.split("|")
        winningNumbers = winners.strip().split()
        ownNumbers = own.strip().split()
        
        ######## Part 1 ##########
        #sum += getPoints(getMatches(winningNumbers, ownNumbers))

        ########### Part 2 ################
        # Add card occurence to collection
        if id in cards:
            cards[id] += 1
        else: cards[id] = 1
        # get number of matches per card
        matches = getMatches(winningNumbers, ownNumbers)

        # for each match add +1 to the occurences of the respective next card
        # If the card does not exist yet, add it to the collection with its ID as long as the id is smaller than the length of the file
        for i in range(id+1, id+matches+1):
            if i in cards:
                cards[i] += cards[id]
            else:
                cards[i] = cards[id]
        
        #print("Round " + str(id) + str(cards))
        id+=1

#print(sum)
print(sum(cards.values()))