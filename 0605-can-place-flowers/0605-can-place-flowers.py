class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        cnt = 0
        start = True
        stack = 0
        isOne = False
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                stack += 1
                if i == len(flowerbed) - 1:
                    cnt += stack // 2
                    if not isOne and len(flowerbed) % 2 != 0:
                        cnt += 1
            else:
                isOne = True
                if start:
                    cnt += stack // 2
                    start = False
                else:
                    cnt += (stack - 1) // 2
                stack = 0
        return cnt >= n