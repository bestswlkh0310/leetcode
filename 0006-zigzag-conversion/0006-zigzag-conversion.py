class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        result = []
        if numRows == 1:
            return s
        r = numRows - 1
        for i in range(numRows):
            s1 = 2 * (r - i)
            s2 = 2 * r - s1
            p = i
            t = True
            while p < len(s):
                result.append(s[p])
                if t:
                    p += s1
                    if s1 == 0:
                        p += s2
                else:
                    p += s2
                    if s2 == 0:
                        p += s1
                t = not t
        return "".join(result)