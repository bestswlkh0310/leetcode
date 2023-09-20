class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        arr = []
        def a(s, l, r):
            if l + r == n * 2 - 1:
                arr.append(s + ")")
            else:
                if l < n:
                    a(s + "(", l + 1, r)
                if r < l:
                    a(s + ")", l, r + 1)
        a("(", 1, 0)
        return arr