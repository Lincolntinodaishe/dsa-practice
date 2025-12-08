# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # base case for null roots
        if not root: return 0
        # use recursive to store the length of each node in the root
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        # return 1+the max lenghts of nodes in both sides 
        return 1+max(left, right)