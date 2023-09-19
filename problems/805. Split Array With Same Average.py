
import collections

class Solution(object):
    def go(self, startIdx, flag):
        checkSum = 0
        for i in range(self.l):
            if flag[i]:
                checkSum += self.arr[i]
        if self.total / 2 == checkSum:
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
        self.total = sum(nums)
        self.end = False
        self.arr = nums
        self.l = len(nums)
        flag = [False for _ in range(self.l)]

        for startIdx in range(self.l):
            newFlag = flag[:]
            newFlag[startIdx] = True
            self.go(startIdx, newFlag)

        return self.end