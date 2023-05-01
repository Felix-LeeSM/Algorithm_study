from heapq import heappop, heappush
from sys import argv, stdin
input = stdin.readline

class myHeap(list):
    def __init__(self, *args):
        super().__init__(*args)
    
    def push(self, item):
        return heappush(self, item)

    def pop(self):
        if self:
            return heappop(self)
        return 0

def solution(N: int, nums: list[int]):
    negatives, positives = myHeap(), myHeap()
    zero = False
    answer = 0

    for num in nums:
        if num < 0:
            negatives.push(num)
        elif num == 1:
            answer += 1
        elif num > 0:
            positives.push(-num)
        else:
            zero = True

    while len(negatives) > 1:
        answer += heappop(negatives) * heappop(negatives)
    while len(positives) > 1:
        answer += heappop(positives) * heappop(positives)
    
    answer -= positives.pop()
    if zero:
        return answer 
    return answer + negatives.pop()
    

    pass


def main(args: list[str] = argv[1:]):
    try:
        N = int(input( ))
        nums = [int(input()) for _ in range(N)]

        answer = solution(N, nums)
        print(answer)
        return 0
    
    except:
        return 1
    


if __name__ == '__main__':
    exit(main())