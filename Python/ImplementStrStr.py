class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack == needle:
            return 0
        length = len(needle)
        for i in range(len(haystack) - length + 1):
            if haystack[i:i+length] == needle:
                return i
        return -1

s = Solution()
print s.strStr("helloworld", "owo")
print s.strStr("h", "")
print s.strStr("hal", "lah")
print s.strStr("", "ah")
print s.strStr("", "")
print s.strStr("ppi", "pi") # right aligning
