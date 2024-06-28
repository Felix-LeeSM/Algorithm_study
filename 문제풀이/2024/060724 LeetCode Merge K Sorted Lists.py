# Definition for singly-linked list.
from typing import List, Optional
from heapq import heappop as hpop, heappush as hpush


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        if self.next is None:
            return f"{self.val}]"
        return f"{self.val}, {self.next}"


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = tail = ListNode()

        hq = []
        for idx, node in enumerate(lists):
            if node:
                hpush(hq, (node.val, idx, node))

        while hq:
            _, idx, node = hpop(hq)
            tail.next, nxt, node.next = node, node.next, None
            tail = tail.next

            if nxt is not None:
                hpush(hq, (nxt.val, idx, nxt))

        return root.next


Solution().mergeKLists([
    ListNode(1, ListNode(4, ListNode(5))),
    ListNode(1, ListNode(3, ListNode(4))),
    ListNode(2, ListNode(6))])
