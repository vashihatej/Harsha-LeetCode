class Solution:
    def rob(self, nums: List[int]) -> int:
        #Recurssion
        # def dfs(i):
        #     if i >= len(nums):
        #         return 0
        #     rob = nums[i] + dfs(i+2)
        #     skip=dfs(i+1)
        #     return max(rob, skip)
        # return dfs(0)

        #using DP top to bottom
        dp=[-1 for i in range(len(nums)+1)]
        def dfs(i):
            if i >= len(nums):
                return 0
            if dp[i] != -1:
                return dp[i]
            rob = nums[i] + dfs(i+2)           #Here it will be like 0,2,4,6,8
            skip=dfs(i+1)                     #Skipping the current one means first one and going forward like 1,3,5,7
            dp[i]=max(rob, skip)
            return dp[i]
        return dfs(0)

        #using DP bottom to top
        if not nums:
            return 0
        dp = [0 for i in range(len(nums)+1)]
        if len(nums) == 1:
            dp[0]=nums[0]
            return nums[0]
        if len(nums) == 2:
            dp[1]= max(nums[0], nums[1])
            return max(nums[0], nums[1])
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return dp[i]
        

