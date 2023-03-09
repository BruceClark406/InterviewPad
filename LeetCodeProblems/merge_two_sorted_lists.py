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

    def recursiveMerge(self, list1: Optional[ListNode], list2: Optional[ListNode], iterator: ListNode):

        if (list1.next is None and list2.next is None):
            return

        if (list1.next is not None and list2.next is not None):
            if list1.val > list2.val:
                list2 = list2.next
                iterator.next = list1
            else:
                list1 = list1.next
                iterator.next = list2

        elif (list1.next is None and list2.next is not None):
            list2 = list2.next
            iterator.next = list1

        elif (list1.next is not None and list2.next is None):
            list1 = list1.next
            iterator.next = list2

        self.recursiveMerge(list1, list2, iterator.next)

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (list1.val > list2.val):
            head = list2
        else:
            head = list1

        self.recursiveMerge(list1, list2, head)
        return head


if __name__ == "__main__":
    solution = Solution()

    # test 1
    list1Head = ListNode(1, ListNode(2, ListNode(4)))
    list2Head = ListNode(1, ListNode(3, ListNode(4)))
    print(list1Head.val)
    head = solution.mergeTwoLists(list1Head, list2Head)
    solution.printLinkedList(head)
