class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}
        def dfs(s1, s2):
            if s2 == len(t):
                return 1
            if s1 == len(s):
                return 0
            if (s1, s2) in dp:
                return dp[(s1, s2)]
            if s[s1]==t[s2]:
                dp[(s1, s2)]=dfs(s1+1, s2)+dfs(s1+1, s2+1)
            else:
                dp[(s1, s2)]=dfs(s1+1, s2)
            return dp[(s1, s2)]
        return dfs(0, 0)