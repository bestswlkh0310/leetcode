class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if a == "0" and b == "0": return "0"
        l1 = list(reversed(list(map(int, list(a)))))
        l2 = list(reversed(list(map(int, list(b)))))
        print(l1)
        s1 = 0
        
        for (idx, i) in enumerate(l1):
            s1 += i * (2 ** idx)
        for (idx, i) in enumerate(l2):
            s1 += i * (2 ** idx)
        
        result = []
        
        while s1 != 0:
            result.append(s1 % 2)
            s1 //= 2
        
        result.reverse()
        
        return "".join(list(map(str, result)))