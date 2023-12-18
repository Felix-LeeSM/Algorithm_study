# Game 1: 1 blue, 8 green; 14 green, 15 blue; 3 green, 9 blue; 8 green, 8 blue, 1 red; 1 red, 9 green, 10 blue
# Game 2: 3 blue, 1 green, 2 red; 2 red, 2 green, 5 blue; 3 green, 10 blue; 8 red, 1 blue; 3 red, 1 green, 5 blue; 1 blue, 5 red, 3 green
# Game 3: 4 green, 1 blue; 6 blue, 5 green, 1 red; 11 green, 10 blue
# Game 4: 12 blue, 12 green, 3 red; 15 blue, 1 green, 10 red; 8 blue, 3 red, 2 green; 14 red, 8 blue
# Game 5: 7 blue, 8 red, 5 green; 15 blue, 16 red, 14 green; 3 blue, 14 red, 10 green
# Game 6: 4 blue, 13 red; 1 green, 13 blue, 11 red; 4 red, 19 blue; 18 blue, 10 red, 1 green
# Game 7: 8 green, 3 blue, 3 red; 2 red, 7 green, 10 blue; 6 green, 11 red, 3 blue
# Game 8: 10 red, 6 green, 1 blue; 15 green, 10 red, 3 blue; 8 red, 10 green, 5 blue
# Game 9: 2 green, 8 blue, 1 red; 6 blue, 10 red; 13 blue, 12 red, 7 green
# Game 10: 2 blue, 8 red, 10 green; 1 green, 2 blue; 1 red, 1 green; 7 red, 2 blue, 1 green
# Game 11: 8 green, 1 blue; 6 green; 2 green, 1 blue; 2 blue, 11 green; 1 red, 12 green
# Game 12: 3 red, 2 green, 15 blue; 1 blue, 1 green, 4 red; 1 green, 12 blue, 3 red; 1 red, 10 blue; 3 red, 2 green, 14 blue; 3 red, 13 blue
# Game 13: 7 blue, 5 red; 7 red, 3 green, 9 blue; 9 green, 7 blue, 7 red; 6 blue, 8 red; 11 red; 3 green, 7 blue, 8 red
# Game 14: 4 blue, 6 green, 7 red; 8 red, 4 green, 11 blue; 3 green, 9 red, 13 blue
# Game 15: 3 green, 1 blue, 5 red; 2 red; 1 red, 4 green
# Game 16: 1 green, 7 blue; 3 red, 5 blue; 1 green, 5 blue; 5 blue, 1 green; 1 green, 1 red, 13 blue
# Game 17: 4 blue, 2 red, 4 green; 1 blue, 7 red, 4 green; 4 red, 4 green, 10 blue; 1 blue, 4 red, 14 green
# Game 18: 7 blue, 5 green; 4 blue, 3 green; 1 red, 6 green, 7 blue
# Game 19: 10 blue, 3 red, 6 green; 3 blue, 4 red, 17 green; 19 green, 3 red, 3 blue; 19 green, 3 blue; 4 red, 7 green, 7 blue; 10 blue, 13 green, 1 red
# Game 20: 3 blue, 6 red, 1 green; 6 green, 7 red, 18 blue; 1 green, 5 red, 14 blue; 1 green, 12 blue, 8 red
# Game 21: 16 blue, 7 green, 13 red; 11 red, 7 blue, 5 green; 4 green, 3 blue
# Game 22: 14 blue, 6 red, 1 green; 9 red, 1 green, 11 blue; 3 red, 13 blue; 6 red, 10 blue; 13 red, 1 green, 2 blue
# Game 23: 17 red, 1 blue, 13 green; 19 green, 1 blue, 3 red; 7 red, 19 green; 16 red, 10 green; 16 red, 12 green, 1 blue
# Game 24: 1 green, 2 blue; 10 green, 4 blue; 8 blue, 11 green, 14 red
# Game 25: 9 blue, 10 red; 2 red, 7 green, 5 blue; 4 green, 10 red, 5 blue; 6 red, 6 blue; 12 blue, 4 green
# Game 26: 9 red, 2 blue, 5 green; 3 red, 4 green, 1 blue; 5 red, 2 blue, 13 green
# Game 27: 1 green, 14 blue, 2 red; 9 red, 7 blue, 7 green; 9 blue, 10 red, 7 green; 1 blue, 5 red, 3 green; 1 blue, 4 red; 9 red, 1 green
# Game 28: 11 red, 13 blue, 12 green; 8 blue, 4 green, 6 red; 2 blue, 9 green

import re
import sys

pocket = {'red': 12, 'green': 13,  'blue': 14}

lines = sys.stdin.readlines()

pattern = re.compile(
    r'(\d+ red|\d+ green|\d+ blue)+')

sum = 0
for line in lines:
    add = True
    game, line = line.rstrip().split(": ")
    game = int(game.split()[-1])

    rounds = line.split('; ')
    for round in rounds:
        if not add:
            break
        for cube in pattern.findall(round):
            num, color = cube.split()
            num = int(num)
            if pocket[color] < num:
                add = False
                break

    if add:
        sum += game


print(sum)
