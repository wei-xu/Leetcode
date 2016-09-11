class Solution:
    def exist(self, board, word):
        '''
        :param board: List[List[str]]
        :param word: str
        :return: bool
        '''
        visited = [[False for x in range(len(board[0]))] for y in range(len(board))]
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] != word[0]:
                    continue
                else:
                    if self.match(board, x, y, word, visited):
                        return True
        return False

    def match(self, board, i, j, word, visited):
        '''
        :param board:
        :param i:
        :param j:
        :param word:
        :param visited: List[List[bool]]
        :return: bool
        '''
        if word == "":
            return True
        if visited[i][j] == True:
            return False
        # new_visited = [[visited[x][y] for y in range(len(visited[0]))] for x in range(len(visited))]
        # new_visited[i][j] = True
        visited[i][j] = True
        if board[i][j] != word[0]:
            return False
        else:
            return self.match(board, min(i + 1, len(board) - 1), j, word[1:], visited) or \
                self.match(board, i, min(j + 1, len(board[0]) - 1), word[1:], visited) or \
                self.match(board, max(i - 1, 0), j, word[1:], visited) or \
                self.match(board, i, max(j - 1, 0), word[1:], visited)

s = Solution()
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
print s.exist(board, "ABCCED")
# print s.exist(board, "SEE")
# print s.exist(board, "ABCB")