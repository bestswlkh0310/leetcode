class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        
        l1 = len(str1)
        l2 = len(str2)
        result = ""
        mn = str1 if l1 < l2 else str2
        mx = str1 if l1 >= l2 else str2
        mnl = min(l1, l2)
        mxl = max(l1, l2)
        for i in range(1, mnl + 1):
            if l1 % i != 0 or l2 % i != 0: continue
            a = mn[:i]
            v = a * (mxl // i)
            v2 = a * (mnl // i)
            
            if v == mx and v2 == mn:
                if len(a) > len(result):
                    result = a
        return result
    