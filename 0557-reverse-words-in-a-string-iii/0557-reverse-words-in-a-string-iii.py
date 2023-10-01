class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        for i in s.split():
            result.append("".join(reversed(list(i))))
        return " ".join(result)