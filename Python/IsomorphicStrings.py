class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        table = dict()
        reverse_table = dict()
        for i in range(len(s)):
            if s[i] not in table and t[i] not in reverse_table:
                table[s[i]] = t[i]
                reverse_table[t[i]] = s[i]
            elif s[i] in table and t[i] in reverse_table:
                if table[s[i]] != t[i] or reverse_table[t[i]] != s[i]:
                    return False
            else:
                return False
        return True

s = Solution()
# print s.isIsomorphic('paper', 'title')
# print s.isIsomorphic('egg', 'add')
# print s.isIsomorphic('foo', 'bar')
print s.isIsomorphic('ab', 'ba')
print s.isIsomorphic('ab', 'bc')
print s.isIsomorphic('abb', 'abb')
print s.isIsomorphic('abb', 'baa')
print s.isIsomorphic('bb', 'cc')
print s.isIsomorphic('ab', 'cd')

print s.isIsomorphic('ab', 'bb')
print s.isIsomorphic('bb', 'ab')
print s.isIsomorphic('apple', 'cllkl')
print s.isIsomorphic('bb', 'cb')

