from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def recursiveMerge(self, list1: Optional[ListNode], list2: Optional[ListNode], iterator: ListNode):
        if

        if list1.val > list2.val:
            iterator.next = list2
        else:
            iterator.next = list1

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode], head: Optional[ListNode]) -> Optional[ListNode]:
        if (head == None):
            if (list1.val > list2.val):
                head = list2
            else:
                head = list1


if __name__ == "__main__":
    solution = Solution()

    # test 1
    list1Head = ListNode(1, ListNode(2, ListNode(4)))
    list2Head = ListNode(1, ListNode(3, ListNode(4)))
    print(list1Head.val)
    solution.mergeTwoLists(list1Head, list2Head)
