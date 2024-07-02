from array import array
from itertools import chain, repeat
from _collections_abc import Iterable


class Segment_Tree:
    TypeCode = {
        'char': ('b', 'B'),
        'short': ('h', 'H'),
        'int': ('i', 'I'),
        'long': ('l', 'L'),
        'long long': ('q', 'Q'),
        'float': 'f',
        'double': 'd'
    }

    def __init__(self, merge=lambda x, y: x+y, neutral_num=0, signed=True, type='long'):
        if type not in self.TypeCode:
            raise ValueError(
                f'Invalid type: {type}, valid types: {self.TypeCode.keys()}')

        if type in ['float', 'double']:
            code = self.TypeCode[type]
        else:
            code = self.TypeCode[type][0] if signed else self.TypeCode[type][1]

        self.init = False
        self.neutral = neutral_num
        self.merge = merge
        self.type_code = code

    def init_tree(self, nums: Iterable):
        if self.init:
            raise RuntimeError('Tree already initialized')
        self.init = True
        self.size = len(nums)
        self.tree = tree = array(
            self.type_code, chain(repeat(self.neutral, self.size), nums))

        for i in range(self.size-1, 0, -1):
            tree[i] = self.merge(self.tree[2*i], self.tree[2*i+1])

    def update(self, idx: int, val):
        if not self.init:
            raise RuntimeError('Tree not initialized')

        tree = self.tree

        idx += self.size
        tree[idx] = val
        idx //= 2

        while idx > 0:
            tree[idx] = self.merge(tree[2*idx], tree[2*idx+1])
            idx //= 2

    # input index starts from 1
    def query(self, start: int, end: int):
        if not self.init:
            raise RuntimeError('Tree not initialized')
        if start > end:
            raise RuntimeError(
                'start index must be greater than or equal to end index')

        tree = self.tree
        start = start + self.size
        end = end + self.size
        answer = self.neutral

        while start <= end:
            if start % 2 == 1:
                answer = self.merge(answer, tree[start])
                start += 1
            if end % 2 == 0:
                answer = self.merge(answer, tree[end])
                end -= 1

            start //= 2
            end //= 2

        return answer


if __name__ == '__main__':
    tree = Segment_Tree()
    tree.init_tree([1, 2, 3])

    assert tree.query(0, 0) == 1
    assert tree.query(0, 1) == 3
    assert tree.query(0, 2) == 6
    assert tree.query(1, 1) == 2
    assert tree.query(1, 2) == 5
    assert tree.query(2, 2) == 3

    tree.update(1, 4)

    assert tree.query(0, 0) == 1
    assert tree.query(0, 1) == 5
    assert tree.query(0, 2) == 8
    assert tree.query(1, 1) == 4
    assert tree.query(1, 2) == 7
    assert tree.query(2, 2) == 3
