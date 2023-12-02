############ Part 1 ##################

rounds = {}
result = 0
cubes = {"red": 12, "green": 13, "blue": 14}


# Helper function checking if the individual Game is possible
def checkPossible(gameDict):
    for (key, value) in gameDict.items():
        if value > cubes[key]:
            return False
    return True


def getGames(input):
    possible = True
    games = []

    individualGames = input.split(";")
    for game in individualGames:
        individualGameDict = {}
        cubes = game.split(",")
        for cube in cubes:
            cube = cube.strip()
            (val, key) = cube.split()
            individualGameDict[key] = int(val)
        games.append(individualGameDict)
        if not checkPossible(individualGameDict): possible = False
    return [games, possible]


# read file into a dictionnary {Game: [dict, dict]}
with open('input.txt', 'r') as f:
    for line in f:
        (key, val) = line.split(":")
        (games, possible) = getGames(val.strip())
        rounds[key] = games
        if possible: result+=int(key.split()[1])

print(result)
