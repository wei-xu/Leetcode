class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash = dict()
        for i in range(len(nums)):
            if nums[i] in hash:
                return [hash[nums[i]] + 1, i + 1]
            elif nums[i] not in hash:
                hash[target - nums[i]] = i


s = Solution()
print s.twoSum([1, 2, 3], 3)
print s.twoSum([2, 7, 6, 11, 15, 1], 7)
print s.twoSum([0, 4, 3, 0], 0)
print s.twoSum([-1, -2, -3, -4, -5], -8)