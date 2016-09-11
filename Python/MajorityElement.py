class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur = 0
        cnt = 0
        for i in nums:
            if cnt == 0:
                cur = i
                cnt = 1
            elif cur == i:
                cnt += 1
            else:
                cnt -= 1
        return cur