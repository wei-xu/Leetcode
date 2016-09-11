class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        LCP = ""
        if len(strs) == 0:
            return ""
        prefix_set = set()
        p = 0
        while True:
            for word in strs:
                if len(word) < (p + 1):
                    return LCP
                prefix_set.add(word[p])
            if len(prefix_set) > 1:
                return LCP
            LCP += prefix_set.pop()
            p += 1
        return LCP

s = Solution()
strs = [
    'str',
    'str',
    'str',
]
strs2 = [
    'str',
    's',
    'str'
]
strs3 = [
    'str',
    'sar',
    'str',
]
strs4 = [
    'str',
    'a',
    'str'
]
strs5 = []
strs6 = [
    'str',
    '',
    'str'
]
strs7 = [
    ''
]

print s.longestCommonPrefix(strs)
print s.longestCommonPrefix(strs2)
print s.longestCommonPrefix(strs3)
print s.longestCommonPrefix(strs4)
print s.longestCommonPrefix(strs5)
print s.longestCommonPrefix(strs6)
print s.longestCommonPrefix(strs7)