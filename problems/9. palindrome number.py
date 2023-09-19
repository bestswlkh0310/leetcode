class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        l = len(s)
        t = True
        for i in range(l // 2):
            if s[i] != s[l - 1 - i]:
                t = False
        return t