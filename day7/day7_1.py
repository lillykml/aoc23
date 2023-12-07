import re


# Helper function to get the kind of the hand
def get_kind(hand):
    hand_dict = {}
    kind = ""
    unique_cards = list(set(hand))
    for card in unique_cards:
        count = len(re.findall(card, hand))
        hand_dict[card] = count
    
    if len(hand_dict.keys()) == 1:
        kind = "Five of a kind"
    elif len(hand_dict.keys()) == 2:
        if 4 in hand_dict.values():
            kind = "Four of a kind"
        else: kind = "Full house"
    elif len(hand_dict.keys()) == 3:
        if 3 in hand_dict.values():
            kind = "Three of a kind"
        else: kind = "Two pair"
    elif len(hand_dict.keys()) == 4: kind = "One pair"
    else: kind = "High card"
    return kind


# Helper Function to determine which hand is stronger, returns 0 if the first hand is stronger and 1 if the second hand
def compare_hand_strength(hand1, hand2):
    strengths = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    for card in zip(hand1, hand2):
        if strengths.index(card[0]) < strengths.index(card[1]):
            return 0
        elif strengths.index(card[0]) > strengths.index(card[1]):
            return 1
        
    
def insert_hand(hand, bid, card_dict, kind):
    inserted = False
    index = 0

    while not inserted and index < len(card_dict[kind]):
        if compare_hand_strength(card_dict[kind][index]['hand'], hand) == 0:
            card_dict[kind].insert(index, {
                "hand": hand,
                  "bid": bid
                  })
            inserted = True
        index += 1
    
    if not inserted:
        card_dict[kind].append({
            "hand": hand,
            "bid": bid
        })

    return card_dict



card_dict = {
    "High card": [],
    "One pair": [],
    "Two pair": [],
    "Three of a kind": [],
    "Full house": [],
    "Four of a kind": [],
    "Five of a kind": [], 
}

# Read in input line by line 
# Store it in a dict with the keys: cards, bid, kind
# For each line determine what "kind" it is 
# Store this again in a dict with the different kinds as keys and an array of the hands as values
with open("input.txt", "r") as file:
    for line in file:
        (hand, bid) = line.split()
        kind = get_kind(hand)
        # Directly sort them in at the correct point (ideally with a good sorting algorithm)
        card_dict = insert_hand(hand, bid, card_dict, kind)

# Do the math over the sorted dicts
result = 0
counter = 1
for key, values in card_dict.items():
    for card in values:
        result += counter * int(card["bid"])
        counter+= 1
print(result)
