class Solution:
    def permute(self, word):
        '''

        :param word: str
        :return: List[string]
        '''
        self.strs = []
        s = set(word)
        self.helper("", len(word), s)
        return self.strs

    def helper(self, w, n, s):
        if n == 0:
            self.strs.append(w)
        else:
            for c in s:
                new_w = w + c
                new_set = set(s)
                new_set.remove(c)
                self.helper(new_w, n - 1, new_set)

s = Solution()
print s.permute("ron")
print s.permute("")
print s.permute("helo")