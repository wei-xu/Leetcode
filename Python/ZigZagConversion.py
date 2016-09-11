class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        num_in_block = 2 + 2 * (numRows - 2)
        line = 1
        output = ""
        while line <= numRows:
            i = 0
            if line == 1 or line == numRows:
                while line + num_in_block * i <= len(s):
                    output += s[line + num_in_block * i - 1]
                    i += 1
            else:
                while line + num_in_block * i <= len(s):
                    output += s[line + num_in_block * i - 1]
                    D = 2 * (numRows - 2)
                    d = D - (line - 2) * 2
                    if line + num_in_block * i + d <= len(s):
                        output += s[line + num_in_block * i + d - 1]
                    i += 1
            line += 1
        return output

s = Solution()
print s.convert("123456789ABCDEF", 3)
print s.convert("123456789ABCD", 3)
print s.convert("PAYPALISHIRING", 3)
print s.convert("123456789", 2)
print s.convert("123456789", 1)
print s.convert("123456789", 6)
