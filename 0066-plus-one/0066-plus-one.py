class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[len(digits) - 1] += 1
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 10:
                digits[i] = 0
                if i != 0:
                    digits[i - 1] += 1
                else:
                    digits.insert(0, 1)
                    
        return digits