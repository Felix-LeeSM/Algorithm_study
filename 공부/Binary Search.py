# 이진 탐색이란, 배열이 정렬되어 있다면 굳이 처음부터 끝까지 볼 필요가 없다는
# 아이디어에서 시작된 탐색 기법이다. 중앙을 기준으로 하여 정렬 기준에 따라
# 비교한 뒤, 그 결과를 기준으로 새로운 기준을 또 찾아 비교하는 방식으로 탐색
# 하는 것이다.

# 여기서의 핵심은 탐색이 대상이 되는 것이 정렬되어 있어야 한다는 것이다.
# 정렬이 되어 있다면, 하나의 원소를 탐색했을 때 다만 그 원소에 대한 일치 여부를
# 넘어서 추가적인 정보를 얻을 수 있기 때문이다.
# 다만, 정렬 그 자체가 대개 NlogN의 시간 복잡도를 가지고, 이진 탐색은 logN의
# 시간 복잡도를 가지므로 정렬되어 있지 않은 것을 새로이 정렬하고 탐색하는 것은
# 현명하지 않을 것 같다. 물론, 2개 이상의 원소를 찾는 경우에는 이진 탐색이 더
# 효율적이겠지만.


def search(array, target):
    def binary_search(left, right):
        if left > right:
            return -1

        mid = (left + right) // 2

        if array[mid] < target:
            return binary_search(mid+1, right)
        elif array[mid] > target:
            return binary_search(left, mid-1)
        else:
            return mid
    return binary_search(0, len(array) - 1)


# 파이썬 내장함수.
def bisect_left(a, x, lo=0, hi=None):
    """Return the index where to insert item x in list a, assuming a is sorted.

    The return value i is such that all e in a[:i] have e < x, and all e in
    a[i:] have e >= x.  So if x already appears in the list, a.insert(x) will
    insert just before the leftmost x already there.

    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """

    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        # Use __lt__ to match the logic in list.sort() and in heapq
        if a[mid] < x:
            lo = mid+1
        else:
            hi = mid
    return lo

# try:
#     from _bisect import *
# except ImportError:
#     pass

# 위의 try except 구문을 통해 C로 구현된 module을 import하고, 이에 실패한 경우,
# python으로 구현한 함수를 통해 진행되는 것으로 보인다.


n, c = map(int, input().split())
locations = [int(input()) for _ in range(n)]
locations.sort()


def binary_search(start, end):  # start, end 간격에 대한 개념이고
    if start > end:
        return end
    mid = (start+end) // 2  # 간격

    now = locations[0]
    count = 1
    for location in locations[1:]:
        if location - now >= mid:
            count += 1
            now = location
    if count >= c:
        start = mid + 1
    else:
        end = mid - 1
    return binary_search(start, end)


print(binary_search(1, locations[-1] - locations[0]))
