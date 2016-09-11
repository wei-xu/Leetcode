class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        output = []
        cp = ''
        for i in range(len(s) - 1):
            if s[i] == '+' and s[i + 1] == '+':
                q = cp + '--' + s[i + 2:]
                output.append(q)
            cp += s[i]
        return output

s = Solution()
print s.generatePossibleNextMoves('++++')
print s.generatePossibleNextMoves('++')
print s.generatePossibleNextMoves('+')
print s.generatePossibleNextMoves('')
print s.generatePossibleNextMoves('-')
print s.generatePossibleNextMoves('--')
print s.generatePossibleNextMoves('+-')
print s.generatePossibleNextMoves('-+')
print s.generatePossibleNextMoves('----+-++')
print s.generatePossibleNextMoves('+++++++')