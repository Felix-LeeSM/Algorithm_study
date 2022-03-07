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
'''
문제
한국도로공사는 고속도로의 유비쿼터스화를 위해 고속도로 위에 N개의 센서를 설치하였다. 
문제는 이 센서들이 수집한 자료들을 모으고 분석할 몇 개의 집중국을 세우는 일인데, 
예산상의 문제로, 고속도로 위에 최대 K개의 집중국을 세울 수 있다고 한다.

각 집중국은 센서의 수신 가능 영역을 조절할 수 있다. 집중국의 수신 가능 영역은 
고속도로 상에서 연결된 구간으로 나타나게 된다. N개의 센서가 적어도 하나의 집중국과는 통신이 가능해야 하며, 
집중국의 유지비 문제로 인해 각 집중국의 수신 가능 영역의 길이의 합을 최소화해야 한다.

편의를 위해 고속도로는 평면상의 직선이라고 가정하고, 센서들은 이 직선 위의 한 기점인 
원점으로부터의 정수 거리의 위치에 놓여 있다고 하자. 따라서, 각 센서의 좌표는 정수 하나로 표현된다. 
이 상황에서 각 집중국의 수신 가능영역의 거리의 합의 최솟값을 구하는 프로그램을 작성하시오. 
단, 집중국의 수신 가능영역의 길이는 0 이상이며 모든 센서의 좌표가 다를 필요는 없다.

입력
첫째 줄에 센서의 개수 N(1 ≤ N ≤ 10,000), 둘째 줄에 집중국의 개수 K(1 ≤ K ≤ 1000)가 주어진다. 
셋째 줄에는 N개의 센서의 좌표가 한 개의 정수로 N개 주어진다. 각 좌표 사이에는 빈 칸이 하나 있으며, 좌표의 절댓값은 1,000,000 이하이다.

<<예시>>
6
2
1 6 9 3 6 7
출력 : 5

10
5
20 3 14 6 7 8 18 10 12 15
출력 : 7
'''
'''
문제
히스토그램은 직사각형 여러 개가 아래쪽으로 정렬되어 있는 도형이다. 
각 직사각형은 같은 너비를 가지고 있지만, 높이는 서로 다를 수도 있다. 
예를 들어, 왼쪽 그림은 높이가 2, 1, 4, 5, 1, 3, 3이고 너비가 1인 직사각형으로 이루어진 히스토그램이다.



히스토그램에서 가장 넓이가 큰 직사각형을 구하는 프로그램을 작성하시오.

입력
입력은 테스트 케이스 여러 개로 이루어져 있다. 각 테스트 케이스는 한 줄로 이루어져 있고, 
직사각형의 수 n이 가장 처음으로 주어진다. (1 ≤ n ≤ 100,000) 그 다음 n개의 정수 
h1, ..., hn (0 ≤ hi ≤ 1,000,000,000)가 주어진다. 이 숫자들은 히스토그램에 있는 직사각형의 높이이며, 
왼쪽부터 오른쪽까지 순서대로 주어진다. 모든 직사각형의 너비는 1이고, 입력의 마지막 줄에는 0이 하나 주어진다.

출력
각 테스트 케이스에 대해서, 히스토그램에서 가장 넓이가 큰 직사각형의 넓이를 출력한다.
'''
'''
while True:
    read = list(map(int, sys.stdin.readline().split()))
    if len(read) == 1:
        break
    n, heights = read[0], read[1:]
    keys = enumerate(heights)
    keys.sort(key = lambda x : -x[1])
'''
