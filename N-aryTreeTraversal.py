"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        values = []
        self.helper(root, values)
        return values
    
    def helper(self, root: Optional[TreeNode], L):
        if root:
            for i in root.children:
                self.helper(i, L)
                
            L.append(root.val)