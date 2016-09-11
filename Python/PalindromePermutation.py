class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        blanket = set()
        for i in range(len(s)):
            if s[i] in blanket:
                blanket.remove(s[i])
            else:
                blanket.add(s[i])
        return len(blanket) == 0 or len(blanket) == 1

s = Solution()
# print s.canPermutePalindrome('aab')
print s.canPermutePalindrome('code')
# print s.canPermutePalindrome('carerac')
# print s.canPermutePalindrome('')
# print s.canPermutePalindrome('aa')
# print s.canPermutePalindrome('b')
