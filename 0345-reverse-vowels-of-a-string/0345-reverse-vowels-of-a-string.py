class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        mo = ('i', 'o', 'u', 'e', 'a', 'A', 'I', 'O', 'E', 'U')
        
        idxs = []
        mos = []
        
        for i in range(len(s)):
            if s[i] in mo:
                idxs.append(i)
                mos.append(s[i])
                
        s = list(s)
        
        mos.reverse()
        
        for i in range(len(idxs)):
            s[idxs[i]] = mos[i]
            
        return "".join(s)