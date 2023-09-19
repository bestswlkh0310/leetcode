class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        l = len(nums)
        for i in range(l - 1):
            for j in range(i + 1, l):
                if nums[i] + nums[j] == target:
                    result.append(i)
                    result.append(j)
        return result