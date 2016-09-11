class Solution(object):
    def findPeakElementBin(self, nums):
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = low + (high - low) / 2
            if nums[mid] < nums[mid + 1]:
                low = mid + 1
            else:
                high = mid
        return low

    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import sys
        nums.append(-sys.maxint - 1)
        prev = -sys.maxint - 1
        for i in range(len(nums) - 1):
            if nums[i] > prev and nums[i + 1] < nums[i]:
                return i
            prev = nums[i]
        return -1

s = Solution()
nums = [1, 2, 3, 1]
print s.findPeakElement(nums)