class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        before = nums[0]
        s = sum(nums[:k])
        mx = s
        for i in range(k, len(nums)):
            s -= before
            before = nums[i - k + 1]
            s += nums[i]
            if mx < s:
                mx = s
        print(mx)
        return mx / float(k)
