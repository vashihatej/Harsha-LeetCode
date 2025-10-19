class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # this is DP approach where we are using bottom up approach means will calculate like dp[0], dp[1], dp[2]......dp[amount+1] for that we wiil have a array of length amount+1 and iniliazed with amount+1 we can do infinite also then for every dp we will seehow many min coins can be used for like ex dp[2] in ex1 we have 1 and 2 value coins so we can use 2 once and that is best solution do dp[2] will be 1 continuiing for dp[3] it will be 1+dp[2] which is equal to 2 so dp[3] will be also 2 . The min coins is calculated by seeing each type coin and considering and taking minimum number of coins needed to get that amount
        # dp = [amount +1] * (amount+1)
        # dp[0] = 0

        # for a in range(1, amount+1):
        #     for c in coins:               #we re constructing the bottom up DP 
        #         if a-c>=0:
        #             dp[a] = min(dp[a], 1+dp[a-c])
        # return dp[amount] if dp[amount] != amount +1 else -1

# -------------------------------
        # # dp[amount] stores the minimum coins needed to form 'amount'
        # dp = {}

        # def dfs(amount):
        #     """
        #     Returns the minimum number of coins needed to make up 'amount'.
        #     If impossible, returns a large number (treated as infinity).
        #     """
        #     # \U0001f3af Base Case 1: If amount becomes 0 → no coins needed
        #     if amount == 0:
        #         return 0

        #     # \U0001f9f1 Base Case 2: If already computed, return from memo
        #     if amount in dp:
        #         return dp[amount]

        #     # \U0001f6ab Initialize with a large number (acts as infinity)
        #     res = 1e9

        #     # Try every coin
        #     for coin in coins:
        #         if amount - coin >= 0:
        #             # Include this coin → reduce remaining amount
        #             res = min(res, 1 + dfs(amount - coin))

        #     # \U0001f4dd Store result in memo
        #     dp[amount] = res
        #     return res

        # # \U0001f680 Start recursion from the target amount
        # minCoins = dfs(amount)

        # # ⚖️ If the result is infinity (impossible), return -1
        # return -1 if minCoins >= 1e9 else minCoins


        dp = {}  # memoization dictionary: key = (i, amount)

        def dfs(i, amount):
            """
            i -> current index in coins[]
            amount -> remaining amount to form
            Returns -> minimum number of coins to make 'amount' using coins[i:]
            """
            # \U0001f3af Base Case 1: If amount is 0 → no coins needed
            if amount == 0:
                return 0

            # \U0001f6ab Base Case 2: If no coins left or amount < 0 → impossible
            if i == len(coins) or amount < 0:
                return float('inf')  # represent impossible state

            # \U0001f4be If already computed, return cached result
            if (i, amount) in dp:
                return dp[(i, amount)]

            # \U0001f4a1 Option 1: Skip current coin (move to next)
            skip = dfs(i + 1, amount)

            # \U0001f4b0 Option 2: Use current coin (stay at same index since unlimited)
            use = 1 + dfs(i, amount - coins[i])

            # \U0001f9ee Take the minimum between both options
            dp[(i, amount)] = min(skip, use)
            return dp[(i, amount)]

        # \U0001f680 Start recursion from first coin and full amount
        res = dfs(0, amount)

        # ⚖️ If result is infinity, return -1 (no valid combination)
        return -1 if res == float('inf') else res

    