from array import array
from itertools import chain, repeat
from _collections_abc import Iterable

['b', 'B', 'h', 'H', 'i', 'I', 'l', 'L', 'q', 'Q', 'f', 'd']
TypeCode = {
    'char': ('b', 'B'),
    'short': ('h', 'H'),
    'int': ('i', 'I'),
    'long': ('l', 'L'),
    'long long': ('q', 'Q'),
    'float': 'f',
    'double': 'd'
}


class Segment_Tree:
    def __init__(self, merge=lambda x, y: x+y, neutral_num=0, signed=True, type='long'):
        if type not in TypeCode:
            raise ValueError(
                f'Invalid type: {type}, valid types: {TypeCode.keys()}')
        if type in ['float', 'double']:
            code = TypeCode[type]
        else:
            code = TypeCode[type][0] if signed else TypeCode[type][1]

        self.neutral = neutral_num
        self.merge = merge
        self.type_code = code

    def init_tree(self, size: int, nums: Iterable):
        if self.init:
            raise RuntimeError('Tree already initialized')
        self.init = True
        self.size = size
        self.tree = tree = array(self.type_code, chain(repeat(0, size), nums))

        for i in range(size-1, 0, -1):
            tree[i] = self.merge(self.tree[2*i], self.tree[2*i+1])

    def update(self, idx: int, val):
        if not self.init:
            raise RuntimeError('Tree not initialized')

        tree = self.tree

        idx += self.size-1
        tree[idx] = val
        idx //= 2

        while idx:
            tree[idx] = self.merge(tree[2*idx], tree[2*idx+1])
            idx //= 2

    # input index starts from 1
    def query(self, start: int, end: int, neutral=None):
        if not self.init:
            raise RuntimeError('Tree not initialized')
        if start > end:
            return self.query(end, start)

        tree = self.tree
        start += self.size-1
        end += self.size-1
        answer = neutral
        if neutral is None:
            answer = self.neutral

        while start <= end:
            if start % 2:
                answer = self.merge(answer, tree[start])
                start += 1
            if not end % 2:
                answer = self.merge(answer, tree[end])
                end -= 1
            start //= 2
            end //= 2
        return answer
