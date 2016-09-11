import math
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        primes = set()
        i = 2
        while i * i < n:
            for j in range(i * i, n, i):
                primes.add(j)
            i += 1

        count = 0
        for m in range(2, n):
            if m not in primes:
                count += 1
        return count

s = Solution()
print s.countPrimes(1500000)