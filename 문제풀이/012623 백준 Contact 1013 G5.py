from sys import stdin
import re
input = stdin.readline


def main():
    try:
        N = int(input())
        patterns = [input().rstrip() for _ in range(N)]
        answer = solution(N, patterns)

        print(*answer, sep='\n')
        return 1

    except BaseException as e:
        print(e.__class__.__name__, e, 'Error Occured', sep='\n')

        return 0


def solution(N, patterns):
    answers = []
    pattern = re.compile(r'^(100+1+|01)+$')
    for p in patterns:
        if pattern.match(p):
            answers.append('YES')
        else:
            answers.append('NO')

    return answers


main()
