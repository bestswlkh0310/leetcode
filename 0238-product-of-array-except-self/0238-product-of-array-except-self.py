class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = 1
        for i in nums:
            s *= i
        
        result = []
        
        for (idx, i) in enumerate(nums):
            if i == 0:
                s1 = 1
                for i in range(len(nums)):
                    if i == idx: continue
                    s1 *= nums[i]
                result.append(s1)
            else:
                result.append(s // i)
        return result