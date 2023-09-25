
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        arr = [[0] * (n + 1) for _ in range(n + 1)]
        
        for i in range(n + 1):
            arr[i][0] = 1
            arr[i][i] = 1
        
        for i in range(1, n):
            for j in range(n):
                arr[i + 1][j + 1] = arr[i][j] + arr[i][j + 1]
        for i in arr:
            print(i)
        j = 0
        for i in range(n + 1, 0, -1):
            cnt += arr[i - 1][i - j - 1]
            j += 1
            if i - j < 0:
                break
            
        for i in arr:
            print(i)
        return cnt