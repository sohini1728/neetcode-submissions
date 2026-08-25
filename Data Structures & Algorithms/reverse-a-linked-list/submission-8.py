# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr is not None:
            nxt = curr.next      # remember what curr used to point to
            curr.next = prev     # spin curr around to point backward
            prev = curr          # step prev forward
            curr = nxt           # step curr forward

        return prev