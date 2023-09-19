import collections

class Solution(object):
    def go(self, startIdx, flag):
        if self.end: return
        arr1 = [i for (idx, i) in enumerate(self.arr) if flag[idx]]
        arr2 = [i for (idx, i) in enumerate(self.arr) if not flag[idx]]
        
        l1 = len(arr1)
        l2 = len(arr2)

        if l1 != 0 and l2 != 0 and sum(arr1) / float(l1) == sum(arr2) / float(l2):
            self.end = True
            return

        for i in range(startIdx, self.l):
            if not flag[i]:
                newFlag = flag[:]
                newFlag[i] = True
                self.go(i, newFlag)

    def splitArraySameAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        self.end = False
        self.arr = nums
        self.l = len(nums)
        flag = [False for _ in range(self.l)]

        for startIdx in range(self.l):
            newFlag = flag[:]
            newFlag[startIdx] = True
            self.go(startIdx, newFlag)

        return self.end

        