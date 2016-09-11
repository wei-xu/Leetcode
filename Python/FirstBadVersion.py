# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersionShort(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left <= right:
            mid = (left + right) / 2
            if self.isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left < right:
            mid = (left + right) / 2
            if self.isBadVersion(mid):
                if mid == 1:
                    return mid
                if not self.isBadVersion(mid - 1):
                    return max(mid, 1)
                else:
                    right = mid - 1
            else:
                if self.isBadVersion(mid + 1):
                    return mid + 1
                else:
                    left = mid + 1
        return max(left, 1)

    def isBadVersion(self, version):
        return True

s = Solution()
print s.firstBadVersion(2)