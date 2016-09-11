class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.m, self.n = len(board), len(board[0])
        dx = (1, 1, 1, 0, 0, -1, -1, -1)
        dy = (1, 0, -1, 1, -1, 1, 0, -1)
        for i in range(self.m):
            for j in range(self.n):
                lives = 0
                for z in range(8):
                    nx, ny = i + dx[z], j + dy[z]
                    lives += self.getStatus(board, nx, ny)
                if lives == 3 or board[i][j] + lives == 3:
                    board[i][j] |= 2
        for i in range(self.m):
            for j in range(self.n):
                board[i][j] >>= 1

    def getStatus(self, board, x, y):
        if x < 0 or y < 0 or x >= self.m or y >= self.n:
            return 0
        return board[x][y] & 1