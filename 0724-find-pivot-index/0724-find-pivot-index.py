class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = sum(nums)
        result = -1
        
        for i in range(0, len(nums)):
            if l == r - nums[i]:
                result = i
                break
            l += nums[i]
            r -= nums[i]
            
        return result