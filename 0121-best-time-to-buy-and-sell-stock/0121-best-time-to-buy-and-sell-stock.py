class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 #l is buy r is sell
        maxp = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                prof = prices[r] - prices[l]
                maxp = max(prof,maxp)
            else:
                l = r
            r +=1
        return maxp