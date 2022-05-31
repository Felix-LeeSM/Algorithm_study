'''
Given the head of a singly linked list, group all the nodes with odd indices together 
followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.



Example 1:


Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]
Example 2:


Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]

'''
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        head = self
        temp = []
        while head:
            temp.append(head.val)
            head = head.next
        return str(temp)


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None or head.next.next is None:
            return head
        odd = head
        even = evenHead = head.next
        while even.next and even.next.next:
            odd.next, even.next = even.next, even.next.next
            odd, even = odd.next, even.next

        if even.next is not None:
            odd.next = even.next
            odd = odd.next
        even.next = None
        odd.next = evenHead

        return head


head = node = ListNode(1)
for i in range(2, 100):
    node.next = ListNode(i)
    node = node.next

print(Solution().oddEvenList(head))
