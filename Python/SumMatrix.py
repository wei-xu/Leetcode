class Solution:
    def sumMatrix(self, matrix):
        '''

        :param matrix: List[List[int]]
        :return: List[List[int]]
        '''
        row = len(matrix)
        col = len(matrix[0])
        output = [[0 for _ in range(col)] for _ in range(row)] # be careful of the order of row and col!!
        for i in range(row):
            sum_left = 0
            for j in range(col):
                if i == 0:
                    output[i][j] = sum_left + matrix[i][j]
                else:
                    output[i][j] = output[i - 1][j] + sum_left + matrix[i][j]
                # print matrix[i][j]
                sum_left += matrix[i][j]
        return output

s = Solution()
m = [
    [1, 2, 3],
    [4, 5, 6]
]
print s.sumMatrix(m)