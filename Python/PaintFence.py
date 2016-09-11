class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0 or k == 0:
            return 0
        if n == 1:
            return k
        if n > 2 and k == 1:
            return 0
        d, s = [0] * n, [0] * n
        d[0] = 0
        s[0] = k
        d[1] = (k - 1) * (s[0] + d[0])
        s[1] = k
        for i in range(2, n):
            s[i] = d[i - 1]
            d[i] = (k - 1) * (s[i - 1] + d[i - 1])
        return s[n - 1] + d[n - 1]

s = Solution()
print s.numWays(2, 1)