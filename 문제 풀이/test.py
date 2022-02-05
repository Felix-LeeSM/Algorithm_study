'''
class binaryheap(object):
    def __init__(self):
        self.items = [None]

    def __len__(self):
        return len(self.items) -1
    
    def _up_(self):
        i = len(self)
        parent = i//2
        while parent > 0:
            if self.items[i] < self.items[parent]:
                self.items[i], self.items[parent] = self.items[parent], self.items[i]
            i = parent
            parent = i//2
    
    def push(self, val):
        self.items.append(val)
        self._up_()
    
    def _down_(self, idx):
        left, right = idx*2, idx*2 +1
        small = idx
        
        if left <= len(self) and self.items[left] < self.items[small]:
            small = left
        if right <= len(self) and self.items[right] < self.items[right]:
            small = right
        if small != idx:
            self.items[idx], self.items[small] = self.items[small], self.items[idx]
            self._down_(small)
    
    def pop(self):
        self.items[1] = self.items[-1]
        ret = self.items.pop()
        self._down_(1)
        return ret

class my_list:
    def __init__(self, obj):
        self.items = obj
    
    def bubblesort(self):
        iters = len(self.items)-1

        for iter in range(iters):
            wall = iters - iter
            for cur in range(wall):
                if self.items[cur] > self.items[cur+1]:
                    self.items[cur], self.items[cur+1] = self.items[cur+1], self.items[cur]
        return self.items
    
    def selectionssort(self):
        iters = len(self.items) -1
        for iter in range(iters):
            minimum = iter
            for cur in range(iter+1, len(self.items)):
                if self.items[cur] < self.items[minimum]:
                    minimum = cur
            
            if minimum != iter:
                self.items[iter], self.items[minimum] = self.items[minimum], self.items[iter]
        return self.items

    def insertionsort_my(self):
        for i in range(1, len(self.items)):
            if self.items[i-1] > self.items[i]:
                for j in range(i-1, -1, -1):
                    if self.items[j] > self.items[j+1]:
                        self.items[j], self.items[j+1] = self.items[j+1], self.items[j]
                    else:
                        break
        return self.items

    def insertionsort(self):
        for cur in range(1, len(self.items)):
            for delta in range(1, cur+1):
                cmp = cur - delta
                if self.items[cmp] > self.items[cmp+1]:
                    self.items[cmp], self.items[cmp+1] = self.items[cmp+1], self.items[cmp]
                else:
                    break

def solution(arrows):
    x, y = 0, 0
    dx = (0, 1, 1, 1, 0, -1, -1, -1)
    dy = (1, 1, 0, -1, -1, -1, 0, 1)
    visited = collections.defaultdict(list)
    figures = 0
    dup = False # 현재 위치가 이미 방문한 위치인가.
    on_line = False

    for i in arrows:
        x = x + dx[i]
        y = y + dy[i]
        if (x, y) in visited:
            if dup:
                dup = True
                continue
            else:
                figures += 1
                dup = True
        else:
            visited.append((x, y))
            dup = False
    
    return figures


def destination(n, moves):
    vect = {'U': 0, 'R': 1, 'D': 2, 'L': 3}
    dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
    x, y = 1, 1
    for move in moves:
        nx = x + dx[vect[move]]
        ny = y + dy[vect[move]]
        if nx < 1 or n < nx or ny < 1 or n < ny:
            continue
        else:
            x, y = nx, ny
    return (x, y)

print(destination(int(input()), input().split()))
'''
'''
class Node_:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList_:
    def __init__(self):
        init = Node_('init')
        self.head = init
        self.tail = init

        self.node = None
        self.datas = 0

    def __len__(self):
        return self.datas

    def __str__(self):
        node = self.head
        node = node.next
        s = ''

        for i in range(self.datas):
            s += f'{node.data}, '
            node = node.next

        return f'[{s[:-2]}]'

    def __iter__(self):
        node = self.head
        node = node.next

        while node:
            yield node.data
            node = node.next

    def insert(self, input_index, input_data):
        node = self.head

        for i in range(input_index):
            node = node.next

        new_node = Node_(input_data)
        new_node.next = node.next
        node.next = new_node

        self.datas += 1

    def append(self, data):
        newnode = Node_(data)
        self.tail.next = newnode
        self.tail = newnode
        self.datas += 1

    def pop(self):
        end_node = self.tail.data
        node = self.head

        for i in range(self.datas):
            if node.next is self.tail:
                self.tail = node
                break
            node = node.next

        self.datas -= 1
        return end_node

    def find(self, data):
        index = -1
        node = self.head

        for i in range(self.datas+1):
            if node.data == data:
                return index
            index += 1
            node = node.next

        return -1
'''
'''
import heapq
def solution(scoville, K):
    tries = 0
    heapq.heapify(scoville)
    length = len(scoville)
    while length >= 2:
        a, b = heapq.heappop(scoville), heapq.heappop(scoville)
        length -= 2
        if a < K:
            c = a + 2*b
            tries += 1
            if c < K:
                heapq.heappush(scoville, c)
                length += 1
        else:
            return tries
    else:
        if min(scoville) >= K:
            return tries
        else:
            return -1
            
solution([1, 2, 3, 9, 10, 12], 1)
'''
import sys
read = sys.stdin.readline
row, col = map(int, read().split())
arr = [list(map(int, list(read().strip()))) for _ in range(row)]


def solution(arr, row, col):
    for side in range(min(row, col)-1, -1, -1):
        for i in range(row-side):
            for j in range(col-side):
                if arr[i][j] == arr[i+side][j] == arr[i][j+side] == arr[i+side][j+side]:
                    return (side+1)**2


print(solution(arr, row, col))
