class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        bound, output = [], []
        for num in nums:
            if lower <= num and num <= upper:
                bound.append(num)
        bound = [lower - 1] + bound + [upper + 1]

        prev = bound[0]
        for i in range(1, len(bound)):
            b = bound[i]
            if prev + 1 < b - 1:
                output.append([prev + 1, b - 1])
            elif prev + 1 == b - 1:
                output.append([prev + 1])
            prev = b

        return ['->'.join(map(str,l)) for l in output]

s = Solution()
nums = [0, 1, 3, 50, 75]
print s.findMissingRanges(nums, 0, 99)
print s.findMissingRanges(nums, -10, 75)
print s.findMissingRanges(nums, -10, 76)
print s.findMissingRanges(nums, 0, 75)
print s.findMissingRanges(nums, 50, 99)
print s.findMissingRanges(nums, 52, 99)
print s.findMissingRanges(nums, -10, 50)
print s.findMissingRanges(nums, -10, 52)
print s.findMissingRanges(nums, 100, 120)
print s.findMissingRanges(nums, -10, -1)
print s.findMissingRanges(nums, 50, 51)
print s.findMissingRanges(nums, 49, 50)