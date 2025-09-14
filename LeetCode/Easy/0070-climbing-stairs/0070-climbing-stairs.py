class Solution:
    def climbStairs(self, n: int) -> int:
        # def rec(i):
        #     if i >= n :
        #         return 1 if i==n else 0
        #     return rec(i+1) + rec(i+2)
        # return rec(0)
        # cache = [-1] * n
        # def dfs(i):
        #     if i >= n:
        #         return i == n
        #     if cache[i] != -1:
        #         return cache[i]
        #     cache[i] = dfs(i + 1) + dfs(i + 2)
        #     return cache[i]

        # return dfs(0)
        dp = [-1 for i in range(n+1)]
        def rec(i):
            if i >= n :
                return 1 if i==n else 0
            if dp[i] != -1:
                return dp[i]
            dp[i] = rec(i+1) + rec(i+2)
            return dp[i]
        return rec(0)