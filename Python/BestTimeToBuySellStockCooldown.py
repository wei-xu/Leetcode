class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        N = len(prices)
        if N < 2:
            return 0
        # buys[0], buys[1] = -prices[0], max(-prices[0], -prices[1])
        # sells[0], sells[1] = 0, max(0, prices[1] - prices[0])
        prev_buy, buy = 0, max(-prices[0], -prices[1])
        prev_sell, sell = 0, max(0, prices[1] - prices[0])
        for i in range(2, N):
            # buys[i] = max(sells[i - 2] - prices[i], buys[i - 1])
            # sells[i] = max(buys[i - 1] + prices[i], sells[i - 1])
            prev_buy = buy
            buy = max(prev_sell - prices[i], prev_buy)
            prev_sell = sell
            sell = max(prev_buy + prices[i], prev_sell)
        return sell