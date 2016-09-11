class Solution(object):
    def summaryRangesShort(self, nums):
        ranges = []
        for n in nums:
            if not ranges or n > ranges[-1][-1] + 1:
                ranges += [],
            ranges[-1][1:] = n,
        return ['->'.join(map(str, r)) for r in ranges]

    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        output = list()
        last_num = nums[0]
        beginning = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            if num == last_num + 1:
                pass
            else:
                if beginning == last_num:
                    output.append(str(last_num))
                else:
                    rg = "%d->%d" % (beginning, last_num)
                    output.append(rg)
                beginning = num
            last_num = num
        if beginning == last_num:
            output.append(str(last_num))
        else:
            rg = "%d->%d" % (beginning, last_num)
            output.append(rg)
        return output

s = Solution()
nums = []
nums2 = [3]
nums3 = [1, 3]
nums4 = [1, 2]
nums5 = [0, 1, 2, 4, 5, 7]
nums6 = [0, 1, 2, 4, 5]
nums7 = [0, 7, 8, 9]
nums8 = [0, 10, 20]
print s.summaryRanges(nums)
print s.summaryRanges(nums2)
print s.summaryRanges(nums3)
print s.summaryRanges(nums4)
print s.summaryRanges(nums5)
print s.summaryRanges(nums6)
print s.summaryRanges(nums7)
print s.summaryRanges(nums8)
