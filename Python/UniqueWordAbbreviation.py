class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.pool = dict()
        self.not_unique = set()
        for word in dictionary:
            if len(word) < 3:
                # if word in self.pool:
                #     self.not_unique.add(word)
                #     del self.pool[word]
                if word not in self.pool and word not in self.not_unique:
                    self.pool[word] = word
            else:
                abbr = word[0] + str(len(word) - 2) + word[-1]
                if abbr in self.pool and self.pool[abbr] != word:
                    # self.pool[abbr] += 1
                    self.not_unique.add(abbr)
                    del self.pool[abbr]
                elif abbr not in self.pool and word not in self.not_unique:
                    self.pool[abbr] = word

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """

        if len(word) < 3:
            abbr = word
        else:
            abbr = word[0] + str(len(word) - 2) + word[-1]
        if abbr in self.not_unique:
            return False
        if abbr in self.pool:
            return word == self.pool[abbr]
        else:
            return True



# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")
# dictionary = ["deer", "door", "cake", "card"]
dictionary = ["happy", "hapay"]
vwa = ValidWordAbbr(dictionary)
print vwa.isUnique("h")
print vwa.isUnique("b")
print vwa.isUnique("happy")
print vwa.isUnique("dear")
print vwa.isUnique("cart")
print vwa.isUnique("cane")
print vwa.isUnique("make")