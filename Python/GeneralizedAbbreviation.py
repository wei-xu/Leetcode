class Solution:
    def generateAbbreviations(self, word):
        ret = []
        if word != '':
            self.backtracking(ret, word, 0, '', 0)
        return ret

    def backtracking(self, ret, word, count, abbr, loc):
        if loc == len(word):
            if count > 0:
                abbr += str(count)
            ret.append(abbr)
        else:
            self.backtracking(ret, word, count + 1, abbr, loc + 1)
            self.backtracking(ret, word, 0, abbr + (str(count) if count > 0 else '') + word[loc], loc + 1)


s = Solution()
print s.generateAbbreviations("word")
print s.generateAbbreviations("no")
print s.generateAbbreviations("")