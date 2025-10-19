class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}  # memoization cache: key = (i, amount)

        def dfs(i, amount):
            """
            i -> current index in 'coins'
            amount -> remaining amount to form
            returns -> number of ways to form 'amount' using coins[i:]
            """
            # \U0001f3af Base Case 1: Exact amount formed
            if amount == 0:
                return 1

            # \U0001f6ab Base Case 2: Ran out of coins or amount went negative
            if i == len(coins) or amount < 0:
                return 0

            # \U0001f9f1 Check memo
            if (i, amount) in dp:
                return dp[(i, amount)]

            # \U0001f4a1 Choice 1: Skip current coin
            skip = dfs(i + 1, amount)

            # \U0001f4b0 Choice 2: Take current coin (unbounded → stay at i)
            take = dfs(i, amount - coins[i])

            dp[(i, amount)] = skip + take
            return dp[(i, amount)]

        # \U0001f680 Start from first coin and full amount
        return dfs(0, amount)
