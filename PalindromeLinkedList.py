# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values = []
        
        self.helper(head, values)
        
        return values[::-1] == values
        
    
    def helper(self, head, V):
        if head:
            V.append(head.val)
            self.helper(head.next, V)
        
        return V