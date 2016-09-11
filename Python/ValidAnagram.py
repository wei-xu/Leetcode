class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        table_a = dict()
        table_b = dict()
        for i in range(len(s)):
            if s[i] not in table_a:
                table_a[s[i]] = 1
            else:
                table_a[s[i]] += 1
        for j in range(len(t)):
            if t[j] not in table_b:
                table_b[t[j]] = 1
            else:
                table_b[t[j]] += 1
        return table_a == table_b