from sys import stdin, stdout
def input(): return stdin.readline().rstrip()


DEFAULT = 1


def sign(x): return 1 if x > 0 else -1 if x < 0 else 0
def to_string(num): return '+' if num > 0 else '-' if num < 0 else '0'
def merge(a, b): return sign(a) * sign(b)


def init(nums):
    n = len(nums)
    tree = [0] * n + nums

    tree[n-1] = merge(DEFAULT, tree[2*n - 1])
    for i in range(n-2, -1, -1):
        tree[i] = merge(tree[i*2 + 1], tree[i*2+2])

    tree.append(DEFAULT)

    return tree


def query(tree, left, right, val=None):
    if val is None:
        data_length = len(tree) // 2
        return query(tree, data_length + left, data_length + right, DEFAULT)

    if left > right:
        return val

    if not left % 2:
        val = merge(val, tree[left])
        left += 1
    left //= 2

    if right % 2:
        val = merge(val, tree[right])
        right -= 1
    right = right // 2 - 1

    return query(tree, left, right, val)


def update(tree, idx, val):
    data_length = len(tree) // 2
    idx += data_length
    val = sign(val)

    tree[idx] = val
    idx = (idx - 1) // 2

    while idx > 0:
        tree[idx] = merge(tree[idx*2 + 1], tree[idx*2 + 2])
        idx = (idx - 1) // 2

    tree[0] = merge(tree[1], tree[2])


outputs = []

try:
    while True:
        output = []
        _, d = map(int, input().split())
        nums = list(map(lambda x: sign(int(x)), input().split()))

        tree = init(nums)

        for _ in range(d):
            command, a, b = input().split()

            if command == 'C':
                idx, val = int(a) - 1, sign(int(b))
                update(tree, idx, val)

            elif command == 'P':
                left, right = int(a) - 1, int(b) - 1

                output.append(to_string(query(tree, left, right)))

        outputs.append("".join(output))
except:
    pass


stdout.write('\n'.join(outputs))
