class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N, M = len(text1), len(text2)
        dp = [[-1]*M for i in range(N)]
        def dfs(s1, s2):
            if s1 == len(text1) or s2 == len(text2):
                return 0
            if dp[s1][s2] != -1:
                return dp[s1][s2]
            if text1[s1] == text2[s2]:
                dp[s1][s2] = 1 + dfs(s1+1, s2+1)
            else:
                dp[s1][s2] = max(dfs(s1+1,s2), dfs(s1,s2+1))
            return dp[s1][s2]
        
            

        


        return dfs(0, 0)