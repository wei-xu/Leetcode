class Codec:
    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        output = str(len(strs[0])) + '#'
        output += reduce(lambda x, y: x + str(len(y)) + '#' + y, strs)
        return output


    def decode(self, s):
        """Decodes a single string to a list of strings

        :type s: str
        :rtype: List[str]
        """
        # method 1
        # output = []
        # while s != '':
        #     idx = s.index('#')
        #     header = s[:s.index('#')]
        #     next_word_len = int(header)
        #     next_word = s[idx + 1: idx + 1 + next_word_len]
        #     output.append(next_word)
        #     s = s[idx + 1 + next_word_len:]
        # return output

        # method 2
        

strs = [
    "#hello",
    "wor#ld",
    "",
    "dear#",
]
strs2 = []
c = Codec()
cipher = c.encode(strs2)
print c.decode(cipher)