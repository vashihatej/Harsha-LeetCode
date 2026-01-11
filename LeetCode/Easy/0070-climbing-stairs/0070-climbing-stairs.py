class Solution:
    def climbStairs(self, n: int) -> int:
        # def rec(i):
        #     if i >= n :
        #         return 1 if i==n else 0
        #     return rec(i+1) + rec(i+2)
        # return rec(0)

        dp = [-1 for i in range(n+1)]
        def rec(i):
            if i >= n :
                return 1 if i==n else 0
            if dp[i] != -1:
                return dp[i]
            dp[i] = rec(i+1) + rec(i+2)
            return dp[i]
        return rec(0)


