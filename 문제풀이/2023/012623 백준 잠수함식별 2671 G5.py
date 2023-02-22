from sys import stdin
import re
input = stdin.readline


def main():
    try:
        pattern = input().rstrip()

        answer = solution(pattern)

        print(answer)
        return 1

    except BaseException as e:
        print(e.__class__.__name__, e, 'Error Occurred', sep='\n')

        return 0


def solution(pattern):
    regex = re.compile(r'^(100+1+|01)+$')

    if regex.match(pattern):
        return 'SUBMARINE'

    return 'NOISE'


main()
