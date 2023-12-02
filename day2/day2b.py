power = 0

def getPower(games):
    minCubes = {"red": 0, "green": 0, "blue": 0}
    power = 1

    individualGames = games.split(";")
    for game in individualGames:
        cubes = game.split(",")
        for cube in cubes:
            cube = cube.strip()
            (val, key) = cube.split()
            if minCubes[key] < int(val):
                minCubes[key] = int(val)

    for i in minCubes.values():
        power*=i
    
    return power


with open('input.txt', 'r') as f:
    for line in f:
        (key, val) = line.split(":")
        gamePower = getPower(val.strip())
        power += gamePower

print(power)
