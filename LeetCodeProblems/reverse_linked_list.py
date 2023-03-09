# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def printLinkedList(self, head: Optional[ListNode]):
        while (head.next is not None):
            print(head.val)
            head = head.next

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head

        while head:
            print(head.val)
            temp = current.next
            head.next = previous
            previous = head
            head = temp

        return previous


if __name__ == "__main__":
    solution = Solution()

    # test 1
    list1Head = ListNode(1, ListNode(2, ListNode(4)))
    head = solution.reverseList(list1Head)
    solution.printLinkedList(head)
