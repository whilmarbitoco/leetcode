class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        
        L, R = 0, 0

        while (R < len(nums)):
            if nums[L] != target:
                L += 1
                R += 1
            
            elif nums[L] == target and nums[R] == target:
                R += 1
            
            else:
                break
        
        return [L, R - 1]