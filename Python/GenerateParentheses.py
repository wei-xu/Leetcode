class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = []
        self.backtrack(ret, 0, 0, n, '')
        return ret

    def backtrack(self, ret, left, right, n, s):
        if left > n or right > n:
            return
        if left == n and right == n:
            ret.append(s)
            return
        elif left > right:
            self.backtrack(ret, left + 1, right, n, s + '(')
            self.backtrack(ret, left, right + 1, n, s + ')')
        elif left == right:
            self.backtrack(ret, left + 1, right, n, s + '(')

sol = Solution()
print sol.generateParenthesis(4)