class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) > 1:
            for i in range(1, len(nums)):
                if (not (i & 1) and nums[i] > nums[i - 1]) or ((i & 1) and nums[i] < nums[i - 1]):
                    nums[i] , nums[i - 1] = nums[i - 1], nums[i]

s = Solution()
nums = [3, 5, 2, 1, 6, 4]
nums2 = [6, 5, 4, 3, 2, 1]
nums3 = [2, 2, 2, 2, 1]
nums4 = []
nums5 = [-8]
nums6= [3, 1]
s.wiggleSort(nums)
s.wiggleSort(nums2)
s.wiggleSort(nums3)
s.wiggleSort(nums4)
s.wiggleSort(nums5)
s.wiggleSort(nums6)
print nums
print nums2
print nums3
print nums4
print nums5
print nums6
