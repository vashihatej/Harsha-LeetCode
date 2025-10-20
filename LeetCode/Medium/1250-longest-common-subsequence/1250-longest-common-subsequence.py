class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M, N = len(text1), len(text2)
        dp = [[-1] * N for _ in range(M)]  # ✅ Fix: M x N grid

        def dfs(s1, s2):
            # Base case — if we reach the end of either string
            if s1 == M or s2 == N:
                return 0

            # Already computed → return from cache
            if dp[s1][s2] != -1:
                return dp[s1][s2]

            # Characters match → take +1 and move both
            if text1[s1] == text2[s2]:
                dp[s1][s2] = 1 + dfs(s1 + 1, s2 + 1)
            else:
                # Characters don't match → try skipping one from either
                dp[s1][s2] = max(dfs(s1 + 1, s2), dfs(s1, s2 + 1))

            return dp[s1][s2]

        return dfs(0, 0)
