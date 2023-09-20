class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = ""
        w1 = list(word1)
        w2 = list(word2)
        
        
        while len(w1) != 0 and len(w2) != 0:
            result += w1[0] + w2[0]
            
            del w1[0]
            del w2[0]
        
        if len(w1) != 0: result += "".join(w1)
        if len(w2) != 0: result += "".join(w2)
            
        
        return result
                
            
