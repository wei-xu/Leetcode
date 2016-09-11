class Solution:
    def popularNumber(self, nums):
        l = len(nums)
        left, mid, right = nums[l/4], nums[l/2], nums[3*l/4]
        for target, edge in [(left, l/4), (mid, l/2), (right, 3 * l / 2)]:
            start, end = 0, edge - 1
            # find left boundary
            while start <= end:
                m = (start + end) / 2
                if nums[m] == target:
                    end = m - 1
                else:
                    start = m + 1
            left_boundary = start

            start, end = edge, l - 1
            while start <= end:
                m = (start + end) / 2
                if nums[m] == target:
                    start = m + 1
                else:
                    end = m - 1
            right_boundary = end
            if right_boundary - left_boundary + 1 > l / 4:
                return nums[left_boundary]

s = Solution()
nums1 = [1, 2, 4, 4, 4, 4, 4, 8, 9, 10, 11, 12, 13, 14, 15, 16]
nums2 = [1, 2, 3, 4, 5, 5, 5, 5, 5, 10, 11, 12, 13, 14, 15, 16]
nums3 = [1, 2, 3, 4, 5, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16]
nums4 = [4, 4, 4, 4, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
nums5 = [1, 2, 3, 4, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# print s.popularNumber(nums1)
# print s.popularNumber(nums2)
# print s.popularNumber(nums3)
# print s.popularNumber(nums4)
print s.popularNumber(nums5)

