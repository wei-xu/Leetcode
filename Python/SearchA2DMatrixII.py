class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m, n, r, c = len(matrix), len(matrix[0]), 0, len(matrix[0]) - 1
        while r < m and c >= 0:
            if matrix[r][c] == target:
                return True
            if matrix[r][c] > target:
                c -= 1
            else:
                r += 1
        return False

    def searchMatrix2(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        row, col = len(matrix), len(matrix[0])
        bottom_right = min(row, col)
        start, end = 0, bottom_right
        while start < end:
            mid = start + (end - start) / 2
            if matrix[mid][mid] == target:
                return True
            elif matrix[mid][mid] < target:
                start = mid + 1
            else:
                end = mid
        bottom_left = [matrix[x][:start] for x in range(row) if x >= start] #
        upper_right = [matrix[y][start:] for y in range(col) if y < start] #
        return self.helper(bottom_left, target) or self.helper(upper_right, target)

s = Solution()
matrix =  [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
print s.searchMatrix(matrix, 0)