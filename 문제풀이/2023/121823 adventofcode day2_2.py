import re
import sys


lines = sys.stdin.readlines()

pattern = re.compile(
    r'(\d+ red|\d+ green|\d+ blue)+')


sum = 0

for line in lines:
    min_req = {'red': 0, 'green': 0, 'blue': 0}

    game, line = line.rstrip().split(": ")
    game = int(game.split()[-1])

    rounds = line.split('; ')
    for round in rounds:

        for cube in pattern.findall(round):
            num, color = cube.split()
            num = int(num)
            min_req[color] = max(min_req[color], num)

    sum += min_req['red'] * min_req['green'] * min_req['blue']

print(sum)
