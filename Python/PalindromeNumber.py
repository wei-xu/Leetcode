class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        new_num = 0
        target = x
        while target > 0:
            new_num = new_num * 10 + target % 10
            target /= 10
        return new_num == x

s = Solution()
print s.isPalindrome(1)