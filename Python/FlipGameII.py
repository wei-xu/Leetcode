class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(len(s) - 1):
            if s[i] == '+' and s[i + 1] == '+':
                new_s = s[:i] + '--' + s[i + 2:]
                canOpWin = self.canWin(new_s)
                if not canOpWin:
                   return True
        return False

sol = Solution()
print sol.canWin("+++++")