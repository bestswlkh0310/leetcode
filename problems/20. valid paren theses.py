class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        opens = ('(', '[', '{')
        stack = []
        result = True
        for i in s:
            print(i)
            if i in opens:
                stack.append(i)
            elif len(stack) == 0:
                return False
            else:
                p = stack.pop()
                if not ((i == '}' and p == '{') or(i == ')' and p == '(') or(i == ']' and p == '[')):
                    result = False
        return result and len(stack) == 0