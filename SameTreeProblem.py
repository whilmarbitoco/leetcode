# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        nq = []
        np = []
        self.traverseTree(q, nq)
        self.traverseTree(p, np)

        return np == nq

    def traverseTree(self, root, V):
        if root:
            self.traverseTree(root.left, V)
            self.traverseTree(root.right, V)  
            V.append(root.val)
        
        else:
            V.append(None)

        return V


