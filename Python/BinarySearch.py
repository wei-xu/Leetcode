class Solution:
    def binarySearch(self, nums, target):
        start, end = 0, len(nums)
        while start < end:
            mid = start + (end - start) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid
        print start
        print end
        return -1

nums = [1, 5, 9, 17, 30]
nums1 = [1]
s = Solution()
print s.binarySearch(nums, 16)