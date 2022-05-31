'''
# 연결리스트 구현
# 1. 노드 클래스 작성


class Node:
    def __init__(self, key=None, value=None):
        self.key = key  # 노드의 고유값 key
        self.value = value  # 필요한 경우의 추가 데이터 value
        self.next = None  # 노드의 포인터


    def __str__(self):
        return str(self.key)  # print(node)인 경우 출력할 문자열


# 2. 연결리스트 클래스 작성
class LinkedList:  # 단일 연결 리스트 클래스
    def __init__(self):

        self.head = None  # 연결 리스트의 가장 앞의 노드. 초기값은 None
        self.size = 0  # 노드 사이즈. 초기값은 0

    def __iter__(self):  # generator 정의 : iterator을 생성해주는 함수
        v = self.head  # yield from으로 요소를 하나씩 꺼내 밖으로 전달함.
        while v != None:  # iterator과의 차이점은 메모리를 반환시키는 것
            yield v
            v = v.next

    def __str__(self):  # print(LinkedList) 연결리스트 값 출력
        return " -> ".join(str(v) for v in self)
        # generator을 이용하여 for문으로 노드를 순서대로 접근하여 join
        # 값 사이의 구분자 '->'를 넣어 출력

    def __len__(self):
        return self.size  # len(A) = A라는 연결클래스 노드 개수 리턴

    # 3. 연결리스트의 메소드 구현
    def pushFront(self, key, value=None):  # head에 노드 삽입
        new_node = Node(key, value)
        new_node.next = self.head  # self.node(이전의 헤드)에 새노드의 next를 연결! 매우 중요
        self.head = new_node  # self.node를 새로운 노드로 바꿔줌
        self.size += 1  # 노드의 사이즈를 1개 더함

    def pushBack(self, key, value=None):  # tail에 노드 삽입
        # 중요한 점은 tail 다음에 삽입이 되므로 빈 리스트라면 새로운 노드가 head 노드가 됨
        new_node = Node(key, value)
        if self.size == 0:  # 빈 리스트라면
            self.head = new_node  # 새 노드가 리스트의 헤드가 된다
        else:
            tail = self.head  # 리스트의 헤드를 테일로 설정
            while tail.next != None:  # tail 노드 찾기 (tail.next가 None인 노드 찾기)
                tail = tail.next
            tail.next = new_node  # 새로운 노드를 tail.next에 넣는다
            self.size += 1  # 사이즈 1 증가

    def popFront(self):  # 리스트의 head 노드 삭제 후 key 반환
        if self.size == 0:  # 빈 리스트라면
            return None  # pop할게 없다
        else:
            x = self.head  # self.head를 x에 담는다
        key = x.value
        self.head = x.next  # x의 다음 노드가 head가 된다
        self.size -= 1  # 노드 삭제 후 사이즈 1 감소
        del x  # x 삭제
        return key  # key 반환

    def popBack(self):  # 맨 뒤의 리스트 삭제. 3가지의 경우를 다룬다
        # 1) 리스트가 비었을 경우
        if self.size == 0:
            return None
        else:
            prev, tail = None, self.head  # prev은 아직 X, tail은 head를 가리키게 함
        while tail.next != None:  # tail을 탐색
            prev = tail  # tail에 prev 값을 대입하고
            tail = tail.next  # tail의 다음 노드를 tail로 만들어 줌
            # 2) 리스트에 노드가 1개일 경우
        if prev == None:  # if len(self) == 1 // head == tail이 되므로
            # 이 경우에는 self.head가 None을 가리켜야 되므로 (리스트가 비어지게 되므로)
            self.head = None
            # 3) 리스트에 노드가 2개 이상일 경우
        else:
            prev.next = tail.next  # tail.next의 노드가 전 노드를 가리키게 한다.
        key = tail.key
        del tail
        self.size -= 1
        return key

    def search(self, key):  # key 값을 저장한 노드를 찾아 리턴, 없으면 None
        # 방법1 : head 노드부터 next로 search
        v = self.head  # v를 head에 넣고 next로 가면서 key값이 같을 경우 키값 리턴
        while v != None:
            if v.key == key:
                return v
        v = v.next
        return v

        # 방법2 : for 루프 사용 __iter__(self)사용

    def search2(self, key):
        for v in self:
            if v.key == key:
                return v

        return None

    def remove(self, key):  # 노드 v를 리스트에서 제거
        # case1 : 리스트가 비어있거나 노드 v가 None
        if len(self) == 0:
            return None
        # case 2: 리스트에 노드가 2개 이상인 경우
        v = self.head
        if v.key == key:
            self.popFront()
            return True
        else:
            while v.next:
                prev, v = v, v.next
                if v.key == key:
                    break
            else:  # 하나짜리는 여기서 걸러짐.
                return None
        # 현재 v는 있는 상태
        # v의 key는 key인 상태.
        prev.next = v.next
        del v
        self.size -= 1
        return True

a = LinkedList()
a.pushFront(3)
a.pushFront(4)
a.pushBack(123)
a.pushBack(432)
a.pushBack(6)
a.pushBack(7)
print(a)
for i in a:
    print(i)
print(3)
'''


class Node:
    def __init__(self, val=None, next=None) -> None:
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def pushFront(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self.tail = self.tail or node
        self.size += 1

    def push(self, value):
        node = Node(value)
        if self.tail:
            self.tail.next = node
            self.tail = node
            self.size += 1
            return
        self.tail = node
        self.head = node
        self.size = 1

    def popFront(self):
        head = self.head
        if head:
            self.head = head.next
            self.size -= 1
            self.tail = self.tail if self.size else None
            return head.val
        else:
            raise ReferenceError

    def pop(self):
        if not self.tail:
            raise ReferenceError

        tail = self.tail

        if self.size == 1:
            self.size = 0
            self.head = None
            self.tail = None
            return tail.val

        if self.size == 2:
            self.tail = self.head
            self.size = 1
            return tail.val

        node = self.head
        while node.next.next:
            node = node.next
        node.next = None
        self.tail = node
        self.size -= 1
        return tail.val


class stack:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0
        return

    def push(self, val) -> None:
        self.size += 1
        node = Node(val)
        if self.tail:
            self.tail.next = node
            self.tail = node
            return
        self.head = self.tail = node
        return

    def pop(self) -> int:
        if not self.size:
            raise ReferenceError
        if self.size == 1:
            ret = self.head.val
            self.head = self.tail = None
            self.size = 0
            return ret

        elif self.size == 2:
            ret = self.tail.val
            self.tail = self.head.next
            self.tail.next = None
            self.size = 1
            return ret

        node, ret = self.head, self.tail.val
        while node.next.next:
            node = node.next
        node.next = None
        self.tail = node
        self.size -= 1
        return ret


class queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, val):
        node = Node(val)
        if not self.head:
            self.head = self.tail = node
            self.size = 1
            return
        self.tail.next = node
        self.tail = node
        self.size += 1

    def popleft(self):
        head = self.head
        if not self.head:
            raise ReferenceError
        self.head = head.next
        self.size -= 1
        return head.val


s = queue()


for i in range(10):
    s.push(i)

for i in range(11):
    print(s.popleft())
