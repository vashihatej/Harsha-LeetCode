class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp = [amount +1] * (amount+1)
        # dp[0] = 0

        # for a in range(1, amount+1):
        #     for c in coins:               #we re constructing the bottom up DP 
        #         if a-c>=0:
        #             dp[a] = min(dp[a], 1+dp[a-c])
        # return dp[amount] if dp[amount] != amount +1 else -1

        dp={}
        def dfs(amount):
            if amount == 0:
                return 0
            if amount in dp:
                return dp[amount]
            res=1e9
            for coin in coins:
                
                if amount-coin >= 0:
                    res = min(res, 1+dfs(amount-coin))
            dp[amount] = res
            return res

        minCoins = dfs(amount)
        return -1 if minCoins >= 1e9 else minCoins



    # this is DP approach where we are using bottom up approach means will calculate like dp[0], dp[1], dp[2]......dp[amount+1] for that we wiil have a array of length amount+1 and iniliazed with amount+1 we can do infinite also then for every dp we will seehow many min coins can be used for like ex dp[2] in ex1 we have 1 and 2 value coins so we can use 2 once and that is best solution do dp[2] will be 1 continuiing for dp[3] it will be 1+dp[2] which is equal to 2 so dp[3] will be also 2 . The min coins is calculated by seeing each type coin and considering and taking minimum number of coins needed to get that amount