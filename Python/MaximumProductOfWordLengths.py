class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        # bit manipulation
        bitMasks = [0] * len(words)
        wordLength = [len(word) for word in words]
        for i in range(len(words)):
            val = 0
            for c in words[i]:
                val |= 1 << (ord(c) - ord('a'))
            bitMasks[i] = val
        maximum = 0
        for i in range(len(bitMasks)):
            for j in range(i + 1, len(bitMasks)):
                if bitMasks[i] & bitMasks[j] == 0:
                    maximum = max(maximum, wordLength[i] * wordLength[j])
        return maximum


        # naive method
        # maximum = 0
        # for i in range(len(words)):
        #     length1 = len(words[i])
        #     for j in range(i + 1, len(words)):
        #         length2 = len(words[j])
        #         if len(set(words[i]) & set(words[j])) == 0:
        #             maximum = max(maximum, length1 * length2)
        # return maximum

s = Solution()
words = ["a", "aa", "aaa", "aaaa"]
words2 = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
words3 = ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
print s.maxProduct(words)
print s.maxProduct(words2)
print s.maxProduct(words3)