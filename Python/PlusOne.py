class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        digits.insert(0, 1)
        return digits

nums = [1,2,3]
nums2 = [1,2,9]
nums3 = [1,9,9]
nums4 = [9,9,9]
nums5 = [9,9,1]
s = Solution()
ans = s.plusOne(nums5)
print ans