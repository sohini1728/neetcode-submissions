# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # scaffolding node, never part of the real answer
        tail = dummy         # tail tracks "the last node I've attached so far"

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                tail.next = list1   # attach list1's node
                list1 = list1.next  # advance ONLY list1
            else:
                tail.next = list2   # attach list2's node
                list2 = list2.next  # advance ONLY list2
            tail = tail.next        # move tail forward to whatever we just attached

        # one list ran out — attach whatever's left of the other
        if list1 is not None:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next  # skip the scaffolding, return the real head