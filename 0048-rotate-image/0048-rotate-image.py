class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        h = len(matrix)
        w = len(matrix[0])
        arr = [[0] * w for i in range(h)]
        print(arr)
        for i in range(h):
          for j in range(w):
            arr[i][j] = matrix[w - j - 1][i]

        for i in range(h):
          for j in range(w):
            matrix[i][j] = arr[i][j]