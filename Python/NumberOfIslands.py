class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if j > len(grid[0]) - 1 or i > len(grid) - 1 or i < 0 or j < 0:
            return
        elif grid[i][j] != '0':
            grid[i][j] = '0'
            self.dfs(grid, i + 1, j)
            self.dfs(grid, i, j + 1)
            self.dfs(grid, i - 1, j)
            self.dfs(grid, i, j - 1)

s = Solution()
grid = [
    [1, 1, 1, 0],
    [1, 0, 0, 0],
    [1, 0, 0, 1],
    [0, 1, 1, 1],
]
grid2 = []
grid3 = [
    [0, 0],
    [0, 0]
]
grid4 = [
    [1],
]
grid5 = [
    [0]
]
grid6 = [
    ['1', '0', '1', '1', '0', '1', '1']
]
# print s.numIslands(grid)
# print s.numIslands(grid2)
# print s.numIslands(grid3)
# print s.numIslands(grid4)
# print s.numIslands(grid5)
print s.numIslands(grid6)
print grid6