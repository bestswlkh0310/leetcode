class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = 0
        
        while s ** 2 <= x:
            s += 1
            
        print(s - 1)
        
        return s - 1