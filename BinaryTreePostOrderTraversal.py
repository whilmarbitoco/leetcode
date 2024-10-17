# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        values = []
        
        self.helper(root, values)
        return values
    
    def helper(self, root, V):
        if root:
            self.helper(root.left, V)
            self.helper(root.right, V)
            V.append(root.val)