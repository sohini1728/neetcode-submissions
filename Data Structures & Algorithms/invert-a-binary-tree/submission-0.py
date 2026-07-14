# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:              # base case: empty node, nothing to invert
            return None

        root.left, root.right = root.right, root.left   # swap children

        self.invertTree(root.left)    # recurse into (now-swapped) left
        self.invertTree(root.right)   # recurse into (now-swapped) right

        return root
