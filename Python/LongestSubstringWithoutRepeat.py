class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        hash = dict()
        output = 0
        for i in range(len(s)):
            if s[i] in hash:
                left = max(left, hash[s[i]] + 1)
            hash[s[i]] = i
            output = max(output, i - left + 1)

        return output

s = Solution()

print s.lengthOfLongestSubstring("")
print s.lengthOfLongestSubstring("b")
print s.lengthOfLongestSubstring("bbbb")
print s.lengthOfLongestSubstring("abcabcbb")
print s.lengthOfLongestSubstring("abcc")
print s.lengthOfLongestSubstring("abcd")
print s.lengthOfLongestSubstring("aabc")
print s.lengthOfLongestSubstring("abccdef")
print s.lengthOfLongestSubstring("abcdbefghi")
