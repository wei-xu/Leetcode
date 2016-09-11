class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1[:m+n] = nums2[:n]
            return
        if n == 0:
            return
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1
        while p >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                if p1 > 0:
                    p1 -= 1
                else:
                    nums1[:p] = nums2[:(p2 + 1)]
            else:
                nums1[p] = nums2[p2]
                if p2 > 0:
                    p2 -= 1
                else:
                    break
            p -= 1
        nums1[0] = min(nums1[0], nums2[0])

s = Solution()
nums1 = []
nums2 = []
s.merge(nums1, 1, nums2, 0)
print nums1