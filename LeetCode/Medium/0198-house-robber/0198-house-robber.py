class Solution:
    def rob(self, nums: List[int]) -> int:
        # def dfs(i):
        #     if i >= len(nums):
        #         return 0
        #     rob = nums[i] + dfs(i+2)
        #     skip=dfs(i+1)
        #     return max(rob, skip)
        # return dfs(0)


        dp=[-1 for i in range(len(nums)+1)]
        def dfs(i):
            if i >= len(nums):
                return 0
            if dp[i] != -1:
                return dp[i]
            rob = nums[i] + dfs(i+2)
            skip=dfs(i+1)
            dp[i]=max(rob, skip)
            return dp[i]
        return dfs(0)
