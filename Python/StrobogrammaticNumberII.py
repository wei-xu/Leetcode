class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        a = list()
        s = ""
        self.R(a, n, s)
        return a

    def R(self, slist, n, s):
        if n < 1:
            if s[0] != '0' or len(s) == 1:
                slist.append(s)
        elif n & 1 != 0:  # odd
            self.R(slist, n - 1, '1')
            self.R(slist, n - 1, '0')
            self.R(slist, n - 1, '8')
        elif n & 1 == 0:
            self.R(slist, n - 2, '1' + s + '1')
            self.R(slist, n - 2, '0' + s + '0')
            self.R(slist, n - 2, '8' + s + '8')
            self.R(slist, n - 2, '6' + s + '9')
            self.R(slist, n - 2, '9' + s + '6')


s = Solution()
ans = s.findStrobogrammatic(2)
print ans