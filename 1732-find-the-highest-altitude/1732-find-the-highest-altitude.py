class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        start = 0
        result = 0
        for i in gain:
            start += i
            if result < start:
                result = start
        return result