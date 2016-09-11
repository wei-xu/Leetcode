class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ugly = [1]
        k = len(primes)
        divide = [0] * k
        index = [0] * k
        while len(ugly) < n:
            for i in range(len(primes)):
                divide[i] = ugly[index[i]] * primes[i]
            m = min(divide)
            for j in range(len(divide)):
                if m == divide[j]:
                    index[j] += 1
            ugly.append(m)
        return ugly[-1]
