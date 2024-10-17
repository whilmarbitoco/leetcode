# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        values = []
        self.helper(root, values)
        return values
    
    def helper(self, root: Optional[TreeNode], L):
        if root:
            L.append(root.val)
            self.helper(root.left, L)
            self.helper(root.right, L)