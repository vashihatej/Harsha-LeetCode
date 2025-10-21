class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        rev = s[::-1]   # Reverse of s
        n = len(s)

        # \U0001f9f1 dp[i][j] = length of LCS between s[i:] and rev[j:]
        dp = [[-1] * n for _ in range(n)]

        def dfs(i, j):
            # Base case: if we reach end of either string
            if i == len(s) or j == len(rev):
                return 0

            # Return cached result if already computed
            if dp[i][j] != -1:
                return dp[i][j]

            # \U0001f7e2 If characters match → part of palindrome
            if s[i] == rev[j]:
                dp[i][j] = 1 + dfs(i + 1, j + 1)
            else:
                # \U0001f534 If not match → skip one char from either string
                dp[i][j] = max(dfs(i + 1, j), dfs(i, j + 1))

            return dp[i][j]

        return dfs(0, 0)
