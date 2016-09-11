import sys
class Solution(object):
    def numSquares(self, n):
        dp = [sys.maxint] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            j = 1
            min_value = sys.maxint
            while i - j * j >= 0:
                if dp[i - j * j] < min_value:
                    min_value = dp[i - j * j] + 1
                j += 1
            dp[i] = min_value
        return dp[-1]
    # def numSquares(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     total_list = list()
    #     plist = list()
    #     self.helper(n, plist, total_list)
    #     print total_list
    #     return len(total_list)
    #
    # def helper(self, n, plist, total_list):
    #     if n == 0:
    #         total_list.append(plist)
    #     else:
    #         lower_num = int(math.floor(n ** (0.5)))
    #         for i in range(lower_num, lower_num / 2, -1):
    #             square = i * i
    #             m = n - square
    #             new_plist = list(plist)
    #             new_plist.append(square)
    #             self.helper(m, new_plist, total_list)


s = Solution()
print s.numSquares(13)
