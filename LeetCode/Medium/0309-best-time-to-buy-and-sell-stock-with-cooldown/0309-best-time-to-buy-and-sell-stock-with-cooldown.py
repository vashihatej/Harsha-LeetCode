class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo={}
        def dfs(i, canbuy):
            if i>=len(prices):
                return 0
            if (i, canbuy) in memo:
                return memo[(i, canbuy)]
            if canbuy:
                buy=dfs(i+1, not canbuy)-prices[i]
                cooldown=dfs(i+1, canbuy)
                profit=max(buy,cooldown)
            else:
                sell=dfs(i+2, not canbuy)+prices[i]
                cooldown=dfs(i+1, canbuy)
                profit=max(sell,cooldown)
            memo[(i,canbuy)]=profit
            return memo[(i,canbuy)]
        return dfs(0, True)

