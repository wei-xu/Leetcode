class Solution:
    def convertToTitle(self, n):
        dist = ord("A") - 1
        if n <= 26:
            return chr(n + dist)
        elif n % 26 == 0:
            return self.convertToTitle((n - 1) / 26) + 'Z'
        else:
            return self.convertToTitle(n / 26) + chr(n % 26 + dist)

s = Solution()
print s.convertToTitle(1)
print s.convertToTitle(26)
print s.convertToTitle(27)
print s.convertToTitle(51)
print s.convertToTitle(52)
print s.convertToTitle(702)
print s.convertToTitle(728)
