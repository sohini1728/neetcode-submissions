# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current is not None:
            nextNode = current.next   # save what's ahead before we overwrite it
            current.next = prev       # rewire backward
            prev = current            # slide prev forward
            current = nextNode        # slide current forward

        return prev  # prev is the new head once current falls off the end