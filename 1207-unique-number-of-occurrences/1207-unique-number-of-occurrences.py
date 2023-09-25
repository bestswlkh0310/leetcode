class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        ar = [0 for _ in range(2001)]
        
        for i in arr:
            ar[i + 1000] += 1
            
        ls = [i for i in ar if i != 0]
        
        return True if len(set(ls)) == len(ls) else False