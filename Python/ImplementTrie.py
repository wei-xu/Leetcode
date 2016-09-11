class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = dict()
        self.isWord = False


class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        p = self.root
        for c in word:
            if not c in p.children:
                p.children[c] = TrieNode()
            p = p.children[c]
        p.isWord = True


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        p = self.root
        for c in word:
            if not c in p.children:
                return False
            p = p.children[c]
        return p.isWord


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        p = self.root
        for c in prefix:
            if not c in p.children:
                return False
            p = p.children[c]
        return True


# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")