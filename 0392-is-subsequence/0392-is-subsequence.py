class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        idx = 0
        for i in s:
            v = t.find(i)
            if v == -1: return False
            else:
                t = t[v + 1:]
        return True