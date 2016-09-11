class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        N = len(citations)
        cnts = [0] * (N + 1)
        for c in citations:
            cnts[[c, N][c > N]] += 1
        sum = 0
        for h in range(N, 0, -1):
            if sum + cnts[h] >= h:
                return h
            sum += cnts[h]
        return 0

        # count = 0
        # citations.sort(reverse=True)
        # for num in citations:
        #     if num > count:
        #         count += 1
        #     else:
        #         break
        # return count

s = Solution()
citations = [2, 0, 6, 1, 5]
citations1 = []
print s.hIndex(citations)