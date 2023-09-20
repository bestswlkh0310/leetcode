class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        for i in range(l - 1):
            if nums[i] == 0:
                nums[i] = None
                nums.append(0)
                
        for i in range(l - 1, -1, -1):
            if nums[i] == None:
                del nums[i]