class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary = '{0:032b}'.format(n)
        print binary
        binary = binary[::-1]
        print binary
        return int(binary, 2)

s = Solution()
print s.reverseBits(2)