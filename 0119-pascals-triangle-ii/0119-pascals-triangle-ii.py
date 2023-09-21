class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        rowIndex += 1
        arr = [[0] * rowIndex for _ in range(rowIndex)]
        
        for i in range(rowIndex):
            arr[0][i] = 1
            arr[i][0] = 1
            
        result = []
        
        for i in range(rowIndex - 1):
            for j in range(rowIndex- 1):
                arr[i + 1][j + 1] = arr[i][j + 1] + arr[i + 1][j]
        print(arr)
        
        for i in range(rowIndex - 1, -1, -1):
            for j in range(rowIndex):
                if i + j == rowIndex - 1:
                    result.append(arr[i][j])
                
                
        return result
        