class Solution:
    def search(self, nums, target):
        if len(nums) < 3:
            return nums.index(target)
        max_pos = self.findMax(nums)
        start, end = 0, max_pos
        while start <= end:
            mid = start + (end - start) / 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1

        start, end = max_pos + 1, len(nums) - 1
        while start <= end:
            mid = start + (end - start) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                start = mid + 1
            else:
                end = mid - 1
        return -1

    def findMax(self, nums):
        # find the max index
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) / 2
            if nums[mid] < nums[mid + 1]:
                start = mid + 1
            else:
                end = mid - 1
        return start

s = Solution()
nums = [1, 2]
print s.search(nums, 1)