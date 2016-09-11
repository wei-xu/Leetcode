'''
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint
stopping you from robbing each of them is that adjacent houses have
security system connected and it will automatically contact the police
if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of
money of each house, determine the maximum amount of money you can
rob tonight without alerting the police.
'''

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        d_n_2 = 0
        d_n_1 = nums[0]
        for i in range(1, len(nums)):
            new_value = max(d_n_2 + nums[i], d_n_1)
            d_n_2 = d_n_1
            d_n_1 = new_value
        return d_n_1


nums = [2, 4, 5, 100, 3, 1]
s = Solution()
ans = s.rob(nums)
print ans
