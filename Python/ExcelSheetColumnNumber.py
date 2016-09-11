class Solution:
    def titleToNumber(self, s):
        dist = ord("A") - 1
        sum = 0
        count = 0
        for i in range(len(s) - 1, -1, -1):
            num = ord(s[i]) - dist
            sum += num * 26 ** count
            count += 1
        return sum

n = Solution()
print n.titleToNumber("BA")
print n.titleToNumber("AB")
print n.titleToNumber("AAA")
print n.titleToNumber("AZ")
print n.titleToNumber("ZZ")
print n.titleToNumber("AAZ")