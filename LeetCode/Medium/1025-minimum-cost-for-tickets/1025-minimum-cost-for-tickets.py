class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp ={}
        durations=[1, 7, 30]

        def dfs(i):
            if i >=len(days):
                return 0
            if i in dp:
                return dp[i]
            res=float('inf')

            for c, d in zip(costs, durations):
                j=i
                while j < len(days) and  days[j]< days[i]+d :
                    j+=1
                cur = c+dfs(j)
                res= min(res,cur)
            dp[i]= res   
                    
            return dp[i]

        return dfs(0)