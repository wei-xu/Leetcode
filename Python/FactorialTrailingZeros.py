class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        num_zero = 0
        denominator = 5
        while n / denominator != 0:
            num_zero += n / denominator
            denominator *= 5
        return num_zero

s = Solution()
print s.trailingZeroes(5)