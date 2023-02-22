

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head
        prev, cur = head, head.next
        saved = None
        while cur.next:
            prev.next = saved  # = 이전 cur?
            saved = prev
            prev, cur = cur, cur.next
        prev.next = saved
        cur.next = prev
        return cur
