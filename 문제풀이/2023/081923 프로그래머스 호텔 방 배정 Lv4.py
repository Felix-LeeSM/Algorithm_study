from sys import setrecursionlimit
setrecursionlimit(1000000)

# k는 1 이상 10**12 이하인 자연수입니다.
# room_number 배열의 크기는 1 이상 200,000 이하입니다.
# room_number 배열 각 원소들의 값은 1 이상 k 이하인 자연수입니다.
# room_number 배열은 모든 고객이 방을 배정받을 수 있는 경우만 입력으로 주어집니다.
# 예를 들어, k = 5, room_number = [5, 5] 와 같은 경우는 방을 배정받지 못하는 고객이 발생하므로 이런 경우는 입력으로 주어지지 않습니다.

# k가 너무 커서 배열로 하면 시간 초과가 난다.


class Parent:
    def __init__(self):
        self.dict = dict()

    def __getitem__(self, key):
        if key in self.dict:
            return self.dict[key]
        return key

    def __setitem__(self, key, value):
        self.dict[key] = value

    def get_parent(self, key):
        if self[key] != key:
            self[key] = self.get_parent(self[key])
        return self[key]
    
    def set_parent(self, child, parent):
        self[child] = parent


def solution(k, room_numbers):
    p = Parent()
    answer = []

    for case in room_numbers:
        next_room = p.get_parent(case)
        answer.append(next_room)
        next_next_room = p.get_parent(next_room + 1)
        p.set_parent(next_room, next_next_room)

    return answer


print(solution(10, [1, 3, 4, 1, 3, 1]))
