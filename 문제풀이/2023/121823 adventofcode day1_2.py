import re
import sys

lines = sys.stdin.readlines()

pattern = re.compile(
    r'(?=(0|1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine))')
map = {
    '1': 1,
    'one': 1,
    '2': 2,
    'two': 2,
    '3': 3,
    'three': 3,
    '4': 4,
    'four': 4,
    '5': 5,
    'five': 5,
    '6': 6,
    'six': 6,
    '7': 7,
    'seven': 7,
    '8': 8,
    'eight': 8,
    '9': 9,
    'nine': 9,

}
sum = 0
for line in lines:
    match = pattern.findall(line)

    sum += map[match[0]] * 10 + map[match[-1]]

print(sum)
