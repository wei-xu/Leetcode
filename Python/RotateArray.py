class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        self.reverse(nums, 0, n - k - 1)
        self.reverse(nums, n - k, n - 1)
        self.reverse(nums, 0, n - 1)

    def reverse(self, nums, i, j):
        mid = (i + j) / 2
        for m in range(0, mid - i + 1):
            nums[i + m], nums[j - m] = nums[j - m], nums[i + m]

s = Solution()
nums = [1,2,3,4,5,6]
s.rotate(nums, 11)
print nums