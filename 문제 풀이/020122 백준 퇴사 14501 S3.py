import sys
read = sys.stdin.readline

days = int(read())
works = [tuple(map(int, read().split())) for _ in range(days)]
works = list(enumerate([0] + works))

def dp_work(date, money):
    if date >= days:
        return money if works[-1][1][0] > 1 else money + works[-1][1][1]
    else:
        if date + works[date][1][0] > days + 1:
            return dp_work(date+1, money)
        else:
            return max(dp_work(date + 1, money), dp_work(date + works[date][1][0], money + works[date][1][1]))


def newone(date, money):
    

print(dp_work(1, 0))